# Everytime re-open project, should active vene again
# in flask-server dir, run "source venv/bin/activate"
# then run "python3 server.py"
from flask import Flask
from flask_cors import CORS
from database_handler import DatabaseAccessLayer
# [tutorial] Set up server (Flask) and client (React) and how to connect Api between them:
# https://www.youtube.com/watch?v=7LNl2JlZKHA


app = Flask(__name__)
CORS(app, resources={r"/api/*": {"origins": "http://localhost:3000"}})

db_connection = DatabaseAccessLayer(config_file='config.ini')

# API routes
from api.bookApi import book_api
from api.visitorApi import visitor_api
from api.adminApi import admin_api

app.register_blueprint(book_api, url_prefix='/api/books')
app.register_blueprint(visitor_api, url_prefix='/api/visitors')
app.register_blueprint(admin_api, url_prefix='/api/admins')


if __name__ == '__main__':
    app.run(debug=True)
