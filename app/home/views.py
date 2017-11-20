from flask import Blueprint


home_blueprint = Blueprint("home", __name__, static_folder="static", template_folder="templates")