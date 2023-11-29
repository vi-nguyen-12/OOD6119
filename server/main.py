# Everytime re-open project, should active vene again
# in flask-server dir, run "source venv/bin/activate"
# then run "python3 server.py"
from flask import Flask
from flask_cors import CORS
from database_handler import DatabaseAccessLayer

app = Flask(__name__)
CORS(app, resources={r"/api/*": {"origins": "http://localhost:3000"}})

db_connection = DatabaseAccessLayer(config_file='config.ini')

# API routes
from api.bookApi import book_api
from api.visitorApi import visitor_api

app.register_blueprint(book_api, url_prefix='/api/books')
app.register_blueprint(visitor_api, url_prefix='/api/visitors')


if __name__ == '__main__':
    app.run(debug=True)
