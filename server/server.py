# Everytime re-open project, should active vene again
# in flask-server dir, run "source venv/bin/activate"
# then run "python3 server.py"
from flask import Flask
from flask_cors import CORS
from api.bookApi import book_api
from api.visitorApi import visitor_api
import mysql.connector

app = Flask(__name__)
CORS(app, resources={r"/api/*": {"origins": "http://localhost:3000"}})

# [Nyeisha] Should connect to database
db = mysql.connector.connect(
    host='host',
    user='user',
    password='password',
    database='database'
)

cursor = db.cursor()

# API routes
app.register_blueprint(book_api, url_prefix='/api/books')
app.register_blueprint(visitor_api, url_prefix='/api/visitors')


if __name__ == '__main__':
    app.run(debug=True)
