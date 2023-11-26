from flask import Flask, request, Blueprint, jsonify
from . import dummy
import sys
sys.path.append('../')

from models import book

book_api =Blueprint("book_api", __name__)

#Initialize the DatabaseAccessLayer
db = DatabaseAccessLayer(config_file='config.ini')

# Get all books
@book_api.route("/", methods=["GET"])
def get_books():
    try:
        # [N] should query from DB to get all books
        select_all_books_query = "SELECT * FROM Book"
        books_data = db.fetch_data(select_all_books_query)
    
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

except Exception as e:
    print(f"Error retrieving books from the database: {e}")
    return jsonify({"error": "Failed to retrieve books"}), 500

# Get a specific book
@book_api.route("/<int:book_id>", methods=["GET"])
def get_book(book_id):
    try:
        # [N] should query from DB to get a book by its id
        select_book_query = "SELECT * FROM Book WHERE _id =%s"
        book_data = db.fetch_data(select_book_query, (book_id,))

        if not book_data:
            return jsonify({"error": "Book not found"}), 404
    
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
        insert_book_query = """
        INSERT INTO Book (title, author, category, is_bestseller, is_available,
                          age_range, technology, awards, challenges, subject, artist)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """
        book_data = (
            title, author, category, is_bestseller, True,
            additional_field.get("Kids"), additional_field.get("ScienceFiction"),
            additional_field.get("Literary"), additional_field.get("Adventure"),
            additional_field.get("Biography"), additional_field.get("Comics")
        )

        db.execute_query(insert_book_query, book_data)

        return jsonify({"message": "Book added successfully"}), 201
         
    except Exception as e:
        print(f"Error creating book: {e}")
        return jsonify({"error": f"Error creating book: {e}"}), 500
    return jsonify({"book":str(new_book)}),200

# delete a book
@book_api.route("/:id", methods=["DELETE"])
def remove_book(book_id):
     try:
        # [N] Delete a book from the database
        delete_book_query = "DELETE FROM Book WHERE _id = %s"
        db.execute_query(delete_book_query, (book_id,))

        return jsonify({"message": f"Book {book_id} deleted successfully"}), 200

    except Exception as e:
        print(f"Error deleting book from the database: {e}")
        return jsonify({"error": "Failed to delete book"}), 500
    #return 


