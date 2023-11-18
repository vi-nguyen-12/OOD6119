# Everytime re-open project, should active vene again
# in flask-server dir, run "source venv/bin/activate"
# then run "python3 server.py"
from flask import Flask
from flask_cors import CORS
from flask_cors import cross_origin
from api.bookApi import books_api

app = Flask(__name__)
CORS(app, resources={r"/api/*": {"origins": "http://localhost:3000"}})


# Books API routes
app.register_blueprint(books_api, url_prefix='/api/books')


if __name__ == '__main__':
    app.run(debug=True)
