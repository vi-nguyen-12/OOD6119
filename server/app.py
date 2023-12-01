from flask import Flask, jsonify, request
from flask_cors import CORS
import mysql.connector
from configparser import ConfigParser

app = Flask(__name__)
CORS(app, resources={r"/api/*": {"origins": "http://localhost:3000"}})

config = ConfigParser()
config.read('config.ini')


mysql = mysql.connector.connect(
    host=config['Database']['host'],
    user=config['Database']['user'],
    password=config['Database']['password'],
    database=config['Database']['database'],
    
)


cursor =mysql.cursor(buffered=True)

@app.route("/api/books", methods=["GET"])
def get_books():
    try:
        cursor.execute("SELECT * FROM books")
        books = cursor.fetchall()
        return jsonify(transform_books(books))
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route("/api/books/borrowed", methods=["GET"])
def get_borrowed_books():
    try:
        cursor.execute("SELECT * FROM borrowed_books")
        borrowed_books = cursor.fetchall()
        return jsonify(transform_borrowed_books(borrowed_books))
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route("/api/books/add", methods=["POST"])
def add_book():
    data = request.get_json()
    title = data.get("title")
    author = data.get("author")
    category = data.get("category")
    is_available = data.get("is_available", True)
    is_bestseller = data.get("is_bestseller", False)

    try:
        cursor = mysql.connection.cursor()
        cursor.execute(
            "INSERT INTO books (title, author, category, is_available, is_bestseller) VALUES (%s, %s, %s, %s, %s)",
            (title, author, category, is_available, is_bestseller),
        )
        mysql.connection.commit()
        return jsonify({"message": "Book added successfully"})
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route("/api/visitors/return", methods=["POST"])
def return_book():
    data = request.get_json()
    visitor_email = data["visitor_email"]
    book_id = data["book_id"]

    try:
        cursor.execute(
            "UPDATE borrowed_books SET return_date = CURDATE() WHERE visitor_email = %s AND book_id = %s",
            (visitor_email, book_id),
        )
        mysql.commit()
        return jsonify({"message": "Book returned successfully"})
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    

def transform_books(input_data):
  result = []
  for item in input_data:
      transformed_item = {
          "_id": item[0],
          "author": item[2],
          "category": item[3],
          "is_available": bool(item[4]),
          "is_bestseller": bool(item[5]),
          "title": item[1]
      }
      result.append(transformed_item)
  return result


def transform_borrowed_books(data):
    result = []
    for item in data:
        transformed_item = {
          "visitor_email": item[0],
          "book_id": item[1],
        
          "borrow_date": item[2],
          "return_date": item[3],
          "late_fee": item[4]
        
        }
        result.append(transformed_item)
    return result


if __name__ == "__main__":
    app.run(debug=True)