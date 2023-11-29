import json
from flask import Flask, request, Blueprint, jsonify
from . import dummy
from datetime import datetime
# import sys
# sys.path.append('../')
# from models import visitor
from models.latefeecalculator import calculate_fee
from database_handler import DatabaseAccessLayer

app = Flask(__name__)
# db = DatabaseAccessLayer(config_file='config.ini')

visitor_api =Blueprint("visitor_api", __name__)

# get a visitor by email
@visitor_api.route("/<email>", methods=["GET"])
def get_visitor(email):
    # [N] get visitor with specific email from DB
    # [from dummy]
    visitor=None
    for v in dummy.visitors:
        if v[1]==email:
            visitor=v
            break
    if visitor is None:
        return jsonify({"error":"No visitor found"}), 400
    result={}
    name_cols=dummy.visitors_cols
    for i in range(1, len(name_cols)):
        result[name_cols[i]]=visitor[i]
    print(result)
    return jsonify(result)

# get all borrowed books of a visitor
@visitor_api.route("/<email>/books/borrowed", methods=["GET"])
def get_borrowed_books(email):

    # [N] get all borrowed books of a visitor from DB, along with details of each book, used "join"
    try:
        from main import db_connection
        query_fetch_borrow_books = "SELECT borrow.transaction_id, borrow.book_id, borrow.borrow_date, borrow.return_date, borrow.late_fee, books.title, books.author, books.category, books.is_bestseller, books.is_available, books.age_range, books.technology, books.awards, books.challenges, books.subject, books.artist FROM borrow JOIN books ON borrow.book_id = books._id WHERE borrow.visitor_email = %s "
        borrow_books = db_connection.fetch_data(query_fetch_borrow_books, (email,))
    except (Exception) as e:
        return jsonify({"error": "Failed to retrieve book"}), 500
    cols =["transaction_id","_id","borrow_date", "return_date", "late_fee","title","author", "category", "is_bestseller","is-available","age_range","technology","awards","challenges","subject","artist"]

    json_borrow_books = [dict(zip(cols, row)) for row in borrow_books]
 
    print(json_borrow_books)
    return jsonify(json_borrow_books), 200


# borrow a book
@visitor_api.route("/borrow", methods=["POST"])
def borrow_book():
    data=request.get_json()
    visitor_email=data.get("visitor_email")
    book_id=data.get("book_id")
    print(type(book_id))
    try:
        from main import db_connection
        # check if the book is available:
        query_get_book_availability= "SELECT is_available FROM books WHERE _id = %s"
        book_availability=db_connection.fetch_data(query_get_book_availability, (book_id,))
     
        if book_availability[0][0] ==0:
            return jsonify({"error":"Book is not available to borrow"}), 500
        # [N] update is_available to False in the Book table
        query_update_book_availability= "UPDATE books SET is_available = False WHERE _id = %s"
        db_connection.execute_query(query_update_book_availability, (book_id,))

        # [N] add visitor_email and book_id to borrow table
        query_insert_borrow_books = "INSERT INTO borrow (visitor_email, book_id, borrow_date) VALUES (%s, %s, %s)"
        db_connection.execute_query(query_insert_borrow_books, (visitor_email, book_id, datetime.now().strftime("%Y-%m-%d")))
    except (Exception) as e:
        return jsonify({"Error updating database":str(e)}), 500
    return jsonify({"message":"Book borrowed successfully"}), 200

# visitor return a book (and pay late fee in case)
@visitor_api.route("/return", methods=["POST"])
def return_book():
    data=request.get_json()
    visitor_email=data.get("visitor_email")
    book_id=data.get("book_id")
    # [N] get borrowed book in Borrowed book table with specific visitor_email and book_id and update payment = 0
    # [from dummy]
    borrowed_book=None
    for b in dummy.borrow_books:
        if b[0]==visitor_email and b[1]==book_id:
            borrowed_book=b
            break
    if borrowed_book is None:
        return jsonify({"error":"No borrowed book found"}), 400
    print(datetime.now().strftime("%Y-%m-%d"))
    borrowed_book[3]=datetime.now().strftime("%Y-%m-%d")
     # [N] get book with specific id from Book table, and update is_available to True;
     # [from dummy]
    for b in dummy.books:
        if b[0]==book_id:
            b[5]=True
            break
    return jsonify({"message":"Return successfully"}), 200
   