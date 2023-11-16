# Everytime re-open project, should active vene again
# in flask-server dir, run "source venv/bin/activate"
# then run "python3 server.py"
from flask import Flask
from flask_cors import CORS
from flask_cors import cross_origin

app = Flask(__name__)
CORS(app, resources={r"/api/*": {"origins": "http://localhost:3000"}})


@cross_origin()
# Books API routes
@app.route('/api/books', methods=['GET'])
def get_books():
    return {"books": ["book1", "book2", "book3"]}


if __name__ == '__main__':
    app.run(debug=True)
