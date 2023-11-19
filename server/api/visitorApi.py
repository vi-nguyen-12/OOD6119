import json
from flask import Flask, request, Blueprint, jsonify
from . import dummy
import sys
# sys.path.append('../')

# from models import visitor

visitor_api =Blueprint("visitor_api", __name__)

@visitor_api.route("/<email>", methods=["GET"])
def get_visitor(email):
    # [N] get visitor with specific email from DB
    # [from dummy]
    visitor=None
    for v in dummy.visitors:
        if v[1]==email:
            visitor=v
            break
    if visitor is None:
        return jsonify({"error":"No visitor found"}), 400
    result={}
    name_cols=dummy.visitors[0]
    for i in range(len(name_cols)):
        result[name_cols[i]]=visitor[i]
    print(result)
    return jsonify(result)


