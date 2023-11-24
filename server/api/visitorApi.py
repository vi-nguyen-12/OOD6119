import json
from flask import Flask, request, Blueprint, jsonify
from . import dummy
from database_handler import DatabaseAccessLayer
import sys
# sys.path.append('../')

# from models import visitor

app = Flask(__name__)
db = DatabaseAccessLayer(config_file='config.ini')

visitor_api =Blueprint("visitor_api", __name__)

@visitor_api.route("/<email>", methods=["GET"])
def get_visitor(email):
    select_query_visitor = "SELECT * FROM Visitor WHERE email = %s"
    visitor_data = db.fetch_data(select_query_visitor, (email,))

    if not visitor_data:
        return jsonify({"error": "No visitor found"}), 400

    visitor = visitor_data[0]

    result = {}
    name_cols =v["user_id", "username", "password", "email", "total_late_fees", "subscription"]
    for i in range(len(name_cols)):
        result[name_cols[i]] = visitors[i]

    return jsonify(result)

if __name__ == "__main__":
    app.register_blueprint(visitor_api)
    app.run(debug=True)

    # [N] get visitor with specific email from DB
    # [from dummy]
    #visitor=None
    #for v in dummy.visitors:
    #    if v[1]==email:
    #        visitor=v
    #        break
    #if visitor is None:
    #    return jsonify({"error":"No visitor found"}), 400
    #result={}
    #name_cols=dummy.visitors[0]
    #for i in range(len(name_cols)):
    #    result[name_cols[i]]=visitor[i]
    #print(result)
    #return jsonify(result)


