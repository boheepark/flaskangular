from flask import Blueprint, request, jsonify
from sqlalchemy import exc

from app import bcrypt, db
from ..users.models import User

auth_blueprint = Blueprint("auth", __name__, static_folder="static", template_folder="templates")

@auth_blueprint.route("/auth/signup", methods = ["POST"])
def signup():
    data = request.get_json()
    if not data:
        return jsonify({
            "status": "fail",
            "message": "Empty payload."
        }), 400
    try:
        uname = data["uname"]
        name = data["name"]
        email = data["email"]
        pw = data["pw"]
        checking = data["checking"]
        trading = data["trading"]
        gender = data["gender"]
        phone = data["phone"]
        addr = data["addr"]
        town = data["town"]
        state = data["state"]
        zip = data["zip"]
    except KeyError as e:
        return jsonify({
            "status": "fail",
            "message": "Incomplete payload."
        }), 400
    except Exception as e:
        print(e)
    try:
        new_user = User(
            id = None,
            uname = uname,
            name = name,
            email = email,
            pw = pw,
            checking = checking,
            trading = trading,
            gender = gender,
            phone = phone,
            addr = addr,
            town = town,
            state = state,
            zip = zip,
            active = True,
            email_confirmed = False,
            last_seen = None,
            updated_at = None,
            created_at = None
        )
        db.session.add(new_user)
        db.session.commit()
        user = User.query.filter(User.uname == uname).first()
        token = new_user.encode_auth_token(new_user.id)
        return jsonify({
            "status": "success",
            "token": token.decode()
        }), 201
    except exc.IntegrityError as e:
        db.session.rollback()
        return jsonify({
            "status": "fail",
            "message": str(e)
        }), 400

@auth_blueprint.route("/auth/checkUname", methods = ["POST"])
def check_uname():
    data = request.get_json()
    users = User.query.all()
    usernames = [user.uname for user in users]
    if data["value"] in usernames:
        return jsonify({
            "status": "error",
            "message": "username already exists",
            "value": False
        })
    return jsonify({
        "status": "success",
        "value": True
    })

@auth_blueprint.route("/auth/checkEmail", methods = ["POST"])
def check_email():
    data = request.get_json()
    users = User.query.all()
    emails = [user.email for user in users]
    if data["value"] in emails:
        return jsonify({
            "status": "error",
            "message": "email already exists",
            "value": False
        })
    return jsonify({
        "status": "success",
        "value": True
    })
@auth_blueprint.route("/auth/signin", methods = ["POST"])
def signin():
    data = request.get_json()
    user = User.query.filter(User.uname == data["uname"]).first()
    if user and bcrypt.check_password_hash(user.pw, data["pw"]):
        token = user.encode_auth_token(user.id)
        return jsonify({
            "status": "success",
            "token": token.decode()
        }), 200

