from multiprocessing import AuthenticationError
from socket import create_connection
# from urllib import request
from flask import Flask, request, Blueprint, jsonify
import json
import sys
sys.path.append('../')

from models import book

books_api =Blueprint("books_api", __name__)

# Get all books
@books_api.route("/", methods=["GET"])
def get_books():
    return jsonify( {"books": ["book1", "book2", "book3"]})

# Get a specific book
@books_api.route("/<int:book_id>", methods=["GET"])
def get_book(book_id):
    return jsonify({"message": f"Get book {book_id}"})

# Create a new book
@books_api.route("/", methods=["POST"])
def add_book():
    data=request.get_json()

    name= data.get("name")
    title=data.get("title")
    author =data.get("author")
    category =data.get("category")
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
        new_book = book_creator.create_book(name,title,author,category,additional_field.get(category))
    except Exception as e:
        print(f"Error creating book: {e}")
        return jsonify({"error": f"Error creating book: {e}"}), 500
    return jsonify({"book":str(new_book)}),200
