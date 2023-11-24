from flask import Flask, request, Blueprint, jsonify
from . import dummy
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

# delete a book
@book_api.route("/:id", methods=["DELETE"])
def remove_book():
    return 


