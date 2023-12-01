
from flask import Flask, request, Blueprint, jsonify
from datetime import datetime
from models.adminloggger import AdminLogger

app = Flask(__name__)

visitor_api =Blueprint("visitor_api", __name__)

# get a visitor by email
@visitor_api.route("/<email>", methods=["GET"])
def get_visitor(email):
    # [N] get visitor by email from DB
    try:
        from main import db_connection
        query_fetch_visitor = "SELECT * FROM visitors WHERE email = %s "
        visitor = db_connection.fetch_data(query_fetch_visitor, (email,))
    except (Exception) as e:
        return jsonify({"error": "Failed to retrieve visitor"}), 500
    cols=["email","name", "is_member","is_subscriber"]
    json_visitor = [dict(zip(cols, row)) for row in visitor]
    return jsonify(json_visitor[0])

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
    try:
        from main import db_connection
        # check if the book is available:
        query_get_book= "SELECT title, is_available FROM books WHERE _id = %s"
        book=db_connection.fetch_data(query_get_book, (book_id,))
     
        if book[0][1] ==0:
            return jsonify({"error":"Book is not available to borrow"}), 500
        # [N] update is_available to False in the Book table
        query_update_book_availability= "UPDATE books SET is_available = False WHERE _id = %s"
        db_connection.execute_query(query_update_book_availability, (book_id,))

        # [N] add visitor_email and book_id to borrow table
        query_insert_borrow_books = "INSERT INTO borrow (visitor_email, book_id, borrow_date) VALUES (%s, %s, %s)"
        db_connection.execute_query(query_insert_borrow_books, (visitor_email, book_id, datetime.now().strftime("%Y-%m-%d")))
    except (Exception) as e:
        return jsonify({"Error updating database":str(e)}), 500
    # [Singleton Pattern] Set this activity to logger
    admin_logger = AdminLogger()
    admin_logger.set_log_activity(visitor_email+" successfully borrow "+ book[0][0])
    return jsonify({"message":"Book borrowed successfully"}), 200

# visitor return a book (and pay late fee in case)
@visitor_api.route("/return", methods=["POST"])
def return_book():
    data=request.get_json()
    transaction_id=data.get("transaction_id")
    # Update return date of transaction in borrow table
    try:
        from main import db_connection
        query_update_return_date= "UPDATE borrow SET return_date = %s WHERE transaction_id = %s"
        db_connection.execute_query(query_update_return_date, (datetime.now().strftime("%Y-%m-%d"), transaction_id))
    except (Exception) as e:
        return jsonify({"Error updating borrow book":str(e)}), 500

    #  Update availability of the book in book table
    try:
        from main import db_connection
        query_get_book_id= "SELECT book_id FROM borrow WHERE transaction_id = %s"
        book_id=db_connection.fetch_data(query_get_book_id, (transaction_id,))[0][0]
        query_update_book_availability= "UPDATE books SET is_available = TRUE WHERE _id = %s"
        db_connection.execute_query(query_update_book_availability, (book_id,))
        
        
    except (Exception) as e:
        return jsonify({"Error updating book availability":str(e)}), 500
    # [Singleton Pattern] Set this activity to logger
    admin_logger = AdminLogger()
    admin_logger.set_log_activity(f"Transaction_id {transaction_id}, return book successfully")
    return jsonify({"message":"Return successfully"}), 200
   