from flask import request, jsonify
from sqlalchemy import exc
from asdf import app, bcrypt, db
from asdf.models.user import User


@app.route("/auth/signin", methods = ["POST"])
def signin():
    data = request.get_json()
    user = User.query.filter(User.uname == data["uname"]).first()
    if user and bcrypt.check_password_hash(user.pw, data["pw"]):
        token = user.encode_auth_token(user.id)
        return jsonify({
            "status": "success",
            "token": token.decode()
        }), 200

@app.route("/auth/signup", methods = ["POST"])
def signup():
    data = request.get_json()
    try:
        new_user = User(
            id=None,
            uname=data["uname"],
            name=data["name"],
            email=data["email"],
            pw=data["pw"],
            checking=data["checking"],
            trading=data["trading"],
            gender=data["gender"],
            phone=data["phone"],
            addr=data["addr"],
            town=data["town"],
            state=data["state"],
            zip=data["zip"],
            last_seen=None,
            updated_at=None,
            created_at=None
        )
        db.session.add(new_user)
        db.session.commit()
        user = User.query.filter(User.uname == data["uname"]).first()
        token = new_user.encode_auth_token(new_user.id)
        return jsonify({
            "status": "success",
            "token": token.decode()
        }), 201
    except exc.IntegrityError as e:
        session.rollback()
        return jsonify({
            "status": "fail",
            "message": str(e)
        }), 400

@app.route("/auth/checkUname", methods = ["POST"])
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

@app.route("/auth/checkEmail", methods = ["POST"])
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
