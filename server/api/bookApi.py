from flask import Flask, request, Blueprint, jsonify
import sys
sys.path.append('../')

from models import book

book_api =Blueprint("book_api", __name__)

# Get all books
@book_api.route("/", methods=["GET"])
def get_books():
    # [N] should query from DB to get all books
    return jsonify( {"books": ["book1", "book2", "book3"]})

# Get a specific book
@book_api.route("/<int:book_id>", methods=["GET"])
def get_book(book_id):
    # [N] should query from DB to get a book by its id
    return jsonify({"message": f"Get book {book_id}"})

# Create a new book
@book_api.route("/", methods=["POST"])
def add_book():
    data=request.get_json()

    name= data.get("name")
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
        new_book = book_creator.create_book(name,title,author,category,is_bestseller,additional_field.get(category))
        # [N] should add new_book to DB, 
        # table includes: _id, title, author, category, is_bestseller, is_available=True, age_range, technology,awards, challenges, subject, artist 
    except Exception as e:
        print(f"Error creating book: {e}")
        return jsonify({"error": f"Error creating book: {e}"}), 500
    return jsonify({"book":str(new_book)}),200

@book_api.route("/:id", methods=["DELETE"])
def remove_book():
    return 

