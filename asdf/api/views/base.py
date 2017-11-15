from flask import Blueprint, send_file


base_blueprint = Blueprint("base", __name__)
@base_blueprint.route("/")
def index():
    return send_file("templates/index.html")
