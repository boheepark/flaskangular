from flask import request, jsonify
from app.models.user import User
from app.models.trade import Trade
from app import app, db


@app.route("/api/user", methods = ["POST"])
def get_user_by_token():
    data = request.get_json()
    user_id = User.decode_auth_token(data["token"])
    if "Signature expired. Please log in again." == user_id:
        return jsonify({
            "status": "fail",
            "message": "Signature expired."
        })
    else:
        user = User.query.filter(User.id == user_id).first()
        if not user:
            return jsonify({
                "status": "fail"
            })
        serialized_user = user.serialize
        serialized_user["sum"] = str(user.checking + user.trading)
        return jsonify({
            "status": "success",
            "data": serialized_user
        }), 200

@app.route("/api/user/trades", methods = ["POST"])
def get_trades_by_token():
    data = request.get_json()
    user_id = User.decode_auth_token(data["token"])
    trades = Trade.query.filter(Trade.user_id == user_id).all()
    return jsonify({
        "status": "success",
        "data": [trade.serialize for trade in trades]
    })

#NOTE how to make more secure?
# should i send token?
@app.route("/api/user/unames", methods = ["GET"])
def get_unames():
    users = User.query.all()
    return jsonify({
        "status": "success",
        "data": [user.username for user in users]
    })

@app.route("/api/user/emails", methods = ["GET"])
def get_emails():
    users = User.query.all()
    return jsonify({
        "status": "success",
        "data": [user.email for user in users]
    })
