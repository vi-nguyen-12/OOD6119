from flask import Flask, request, Blueprint, jsonify
from models.adminloggger import AdminLogger

app = Flask(__name__)

admin_api =Blueprint("admin_api", __name__)
# get admin logger
@admin_api.route("/logger", methods=["GET"])
def get_admin_logger():
    # [Singleton Pattern] Get admin logger history 
    admin_logger = AdminLogger()
    return jsonify(admin_logger.get_log_entries())