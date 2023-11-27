from flask import Flask, request, Blueprint, jsonify
from . import dummy
from datetime import datetime
from models.latefeecalculator import calculate_fee
import sys
sys.path.append('../')

from models import book

book_api =Blueprint("book_api", __name__)

# Get all books
@book_api.route("/", methods=["GET"])
def get_books():
    # [N] should query from DB to get all books
    # result =cursor.fetchall()

    #[from dummy]

    books =[
        {"_id":row[0], "title":row[1],"author":row[2],
         "category":row[3], "is_bestseller":row[4],
         "is_available":row[5], "age_range":row[6],
         "technology":row[7], "awards":row[8],
         "challenges":row[9], "subject":row[10],
         "artists":row[11]
         } for row in dummy.books
    ]
 
    return jsonify( books)

# Get a specific book
@book_api.route("/<int:book_id>", methods=["GET"])
def get_book(book_id):
    # [N] should query from DB to get a book by its id
    return jsonify({"message": f"Get book {book_id}"})

# Create a new book
@book_api.route("/", methods=["POST"])
def add_book():
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

    # Create Concrete Factory based on the category

    try:
        book_creator =book.BookCreatorFactory.create_creator(category)
    except TypeError as e:
        print(f"Error creating creator class: {e}")
        return jsonify({"error":"Invalid category"}),400

    try:
        new_book = book_creator.create_book(title,author,category,is_bestseller,additional_field.get(category))
        # [N] should add new_book to DB, 
        # table includes: _id, title, author, category, is_bestseller, is_available=True, age_range, technology,awards, challenges, subject, artist 
    except Exception as e:
        print(f"Error creating book: {e}")
        return jsonify({"error": f"Error creating book: {e}"}), 500
    return jsonify({"book":str(new_book)}),200

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
def get_borrowed_books():
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


