from flask import Flask, request, Blueprint, jsonify, make_response
import json
from . import dummy
from datetime import datetime
from models.latefeecalculator import calculate_fee
# import sys
# sys.path.append('../')
book_api =Blueprint("book_api", __name__)
import models.book

# Get all books
@book_api.route("/", methods=["GET"])
def get_books():
    try:
        from main import db_connection
        query="SELECT * FROM books"
        books = db_connection.fetch_data(query)
  
        columns =["_id","title","author","category","is_bestseller","is_available","age_range","technology","awards","challenges","subject","artists"]
        json_books =[
           dict(zip(columns,row))
           for row in books
        ]
     
        return jsonify( json_books)

    except Exception as e:
        print(f"Error retrieving books from the database: {e}")
        return jsonify({"error": "Failed to retrieve books"}), 500

# Get all borrow books
@book_api.route("/borrowed", methods=["GET"])
def get_borrowed_books():
    # update late_fee for book which is not returned yet
    try:
        from main import db_connection
        query_fetch_not_returned_books = "SELECT borrow.transaction_id, borrow.borrow_date, visitors.is_member,books.is_bestseller FROM borrow JOIN visitors ON borrow.visitor_email = visitors.email JOIN books ON borrow.book_id = books._id WHERE borrow.return_date IS NULL"
        not_returned_books = db_connection.fetch_data(query_fetch_not_returned_books)
        for b in not_returned_books:
            late_fee=calculate_fee(b[1],datetime.now().strftime("%Y-%m-%d"),b[2],b[3])
            query_update_late_fee = "UPDATE books SET late_fee = %s WHERE transaction_id = %s"
            db_connection.execute_query(query_update_late_fee, (late_fee,b[0]))

    except Exception as e:
        return jsonify({"error": "Failed to update late_fee"}), 500
    try:

        query_fetch_borrowed_books="SELECT borrow.transaction_id,visitors.email, visitors.name, visitors.is_member,borrow.book_id, borrow.borrow_date, borrow.return_date, borrow.late_fee, books.title, books.author, books.category, books.is_bestseller, books.is_available, books.age_range, books.technology, books.awards, books.challenges, books.subject, books.artist  FROM borrow  JOIN visitors ON borrow.visitor_email = visitors.email JOIN books ON borrow.book_id = books._id"
        borrowed_books = db_connection.fetch_data(query_fetch_borrowed_books)
        cols =["transaction_id","visitor_email", "name", "is_member","book_id", "borrow_date", "return_date", "late_fee", "title", "author", "category", "is_bestseller", "is_available", "age_range", "technology","awards", "challenges", "subject", "artist"]
        json_borrowed_books =[
           dict(zip(cols,row))
           for row in borrowed_books
        ]
        return jsonify( json_borrowed_books)
    except Exception as e:
   
        return jsonify({"error": "Failed to retrieve borrowed books"}), 500

# Create a new book
@book_api.route("/add", methods=["POST"], strict_slashes=False)
def add_book():
    try: 
        data=request.get_json(silent=True)
    except Exception as e:
        return jsonify({"Error parsing json":f"{e}"}),400
    

    title, author, category,is_bestseller=data.get("title"),data.get("author"),data.get("category"), data.get("is_bestseller") 
 
    other_fields = {
        "Kids":"age_range",
        "ScienceFiction":"technology",
        "Literary":"awards",
        "Adventure":"challenges",
        "Biography":"subject",
        "Comics":"artists",
    }
    other_field=data.get(other_fields.get(category))
    # Create Concrete Factory based on the category
   
    try:
        book_creator =models.book.BookCreatorFactory.create_creator(category)
    except TypeError as e:
        return jsonify({"error":"Invalid category"}),400
  
    try:
        new_book = book_creator.create_book(title,author,category,is_bestseller,other_field)
    except Exception as e:
        return jsonify({"error": f"Error creating book: {e}"}), 500
    try:
        new_book.save_to_db()
    except Exception as e:
        return jsonify({"error": f"Error saving book: {e}"}), 500
    return jsonify({"message": "Book added successfully"}), 200
# Get a specific book
@book_api.route("/<int:book_id>", methods=["GET"])
def get_book(book_id):
    try:
        # [N] should query from DB to get a book by its id
        select_book_query = "SELECT * FROM Book WHERE book_id =%s"
        book_data = db.fetch_data(select_book_query, (book_id,))

        if not book_data:
            return jsonify({"error": "Book not found"}), 404
        return jsonify({"message": f"Get book {book_id}"})
    
    except Exception as e:
        print(f"Error retrieving book from the database: {e}")
        return jsonify({"error": "Failed to retrieve book"}), 500



# Update a book
@book_api.route("/<int:book_id>", methods=["PUT"])
def update_book(book_id):
    data=request.get_json()

    title=data.get("title")
    author =data.get("author")
    category =data.get("category")
    is_bestseller: data.get("is_bestseller") 
    additional_field = {
        "Kids":data.get("age_range"),
        "ScienceFiction":data.get("technology"),
        "Literary":data.get("awards"),
        "Adventure":data.get("challenges"),
        "Biography":data.get("subject"),
        "Comics":data.get("artists"),
    }

    # [N] should query from DB to get a book by its id
    # [from dummy]
    book=None
    for b in dummy.books:
        if b[0]==book_id:
            book=b
            break
    if book is None:
        return jsonify({"error":"No book found"}), 400
    # [N] should update book in DB, 
    # table includes: _id, title, author, category, is_bestseller, is_available=True, age_range, technology,awards, challenges, subject, artist
    # [from dummy]
    book[1]=title
    book[2]=author
    book[3]=category
    book[4]=is_bestseller
    if category== "Kid":
        book[6]=additional_field.get("Kids")
    elif category == "ScienceFiction":
        book[7]=additional_field.get("ScienceFiction") 
    elif category == "Literary":
        book[8]=additional_field.get("Literary")
    elif category == "Adventure":
        book[9]=additional_field.get("Adventure")
    elif category=="Biography":
        book[10]=additional_field.get("Biography")
    elif category=="Comics":
        book[11]=additional_field.get("Comics")
    return jsonify({"message":"Book updated successfully"}), 200
 
# Get all borrow books
@book_api.route("/borrowed", methods=["GET"])
def get_borrowed_books_dummy():
    # [N] should query from DB to get all borrowed books from Borrowed book table, use join
    # [from dummy]
    borrow_books =list(dummy.borrow_books)
    for e in dummy.borrow_books:
        b= next((x for x in dummy.books if e[1]==x[0]),None)
        v= next((x for x in dummy.visitors if e[0]==x[1]),None)
        # calculate fee of each book
        return_date=e[3]
        if return_date is None:
            return_date = datetime.now().strftime("%Y-%m-%d")
      
        late_fee=calculate_fee(e[2],return_date,v[2],b[4])
        e.extend(b)
        e.append(late_fee)
    borrow_books =[{
        "visitor_email":b[0],
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
    } for b in borrow_books]
    
    return jsonify( borrow_books)


