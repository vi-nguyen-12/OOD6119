import json
from flask import Flask, request, Blueprint, jsonify
from . import dummy
from datetime import datetime
import sys
sys.path.append('../')
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
    # [N] get borrowed books of a visitor from DB
    visitor=None
    for v in dummy.visitors:
        if v[1]==email:
            visitor=v
            break
    if visitor is None:
        return jsonify({"error":"No visitor found"}), 400
    # [N] get all borrowed books of a visitor from DB, along with details of each book, used "join"
    # [from dummy]
    borrow_books=list(dummy.borrow_books)
    books=list(dummy.books)
    borrow_books=[e for e in borrow_books if e[0]==email]
    select_query_visitor = "SELECT * FROM Visitor WHERE email = %s"
#     visitor_data = db.fetch_data(select_query_visitor, (email,))

#     if not visitor_data:
#         return jsonify({"error": "No visitor found"}), 400

#     visitor = visitor_data[0]

#     result = {}
#     name_cols =v["user_id", "username", "password", "email", "total_late_fees", "subscription"]
#     for i in range(len(name_cols)):
#         result[name_cols[i]] = visitors[i]

#     return jsonify(result)

# if __name__ == "__main__":
#     app.register_blueprint(visitor_api)
#     app.run(debug=True)

    # [N] get visitor with specific email from DB
    # [from dummy]
    #visitor=None
    #for v in dummy.visitors:
    #    if v[1]==email:
    #        visitor=v
    #        break
    #if visitor is None:
    #    return jsonify({"error":"No visitor found"}), 400
    #result={}
    #name_cols=dummy.visitors[0]
    #for i in range(len(name_cols)):
    #    result[name_cols[i]]=visitor[i]
    #print(result)
    #return jsonify(result)


    for e in borrow_books:
        # find details of each book
        b= next((x for x in books if e[1]==x[0]),None)
   
        if b is None:
            return jsonify({"error":"No book found"}), 400
        # calculate late fee of each book
        return_date=e[3]
        if return_date is None:
            return_date = datetime.now().strftime("%Y-%m-%d")
        late_fee=calculate_fee(e[2],return_date,visitor[2],b[4])
        # [N] update late fee to 
        # add details of each book
        e.extend(b)
        e.append(late_fee)

    
    borrow_books =[ {
        "book_id":b[1],
        "borrow_date":b[2],
        "return_date":b[3],
        "title":b[6],
        "author":b[7],
        "category":b[8],
        "age_range":b[11],
        "technology":b[12],
        "awards":b[13],
        "challenges":b[14],
        "subject":b[15],
        "artist":b[16],
        "late_fee":b[17]
    }for b in borrow_books]

    return jsonify(borrow_books)


# borrow a book
@visitor_api.route("/borrow", methods=["POST"])
def borrow_book():
    data=request.get_json()
    visitor_email=data.get("visitor_email")
    book_id=data.get("book_id")

    # [N] update is_available to False in the Book table
    update_query_book_availability = "UPDATE Book SET is_available = False WHERE book_id = %s"
    db.execute_query(update_query_book_availability, (book_id,))

    # [N] add visitor_email and book_id to BorrowBooks table
    insert_query_borrow_books = "INSERT INTO BorrowBooks (visitor_email, book_id, borrow_date) VALUES (%s, %s, %s)"
    db.execute_query(insert_query_borrow_books, (visitor_email, book_id, datetime.now().strftime("%Y-%m-%d")))


    # [N] get book with specific id from Book table, and update is_available to False
    # [from dummy]
    book=None
    for b in dummy.books:
        if b[0]==book_id:
            book=b
            b[5]=False
            break
    if book is None:
        return jsonify({"error":"No book found"}), 400
    
    # [N] add visitor_email and book_id to borrow_books, borrow_date table
    # [from dummy]
    dummy.borrow_books.append([visitor_email,book_id,datetime.now().strftime("%Y-%m-%d"),None,0])
    #[N]
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
   