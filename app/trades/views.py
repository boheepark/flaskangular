from datetime import datetime

from flask import Blueprint, request, jsonify
from sqlalchemy import exc

from app import db
from ..users.models import User
from .models import Trade

trades_blueprint = Blueprint("trades", __name__, static_folder="static", template_folder="templates")

@trades_blueprint.route("/api/trades/buy", methods = ["POST"])
def trading_buy():
    data = request.get_json()
    try:
        user = User.query.filter(User.id == data["user_id"]).first()
        diff = user.trading - data["total"]
        new_trade = Trade(id=None, user_id=data["user_id"], company=data["company"], price=data["price"], quantity=data["quantity"], total=data["total"], created_at=None)
        db.session.add(new_trade)
        User.query.filter(User.id == data["user_id"]).update({"trading": diff, "updated_at": datetime.now()})
        db.session.commit()
        serialized_user = user.serialize
        trades = Trade.query.filter(Trade.user_id == data["user_id"]).all()
        return jsonify({
            "status": "success",
            "data": {
                "user": serialized_user,
                "trades": [trade.serialize for trade in trades]
            }
        })
    except exc.IntegrityError as e:
        session.rollback()
        return jsonify({
            "status": "fail",
            "message": str(e)
        }), 400
