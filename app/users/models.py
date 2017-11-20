from flask import current_app
import jwt
from datetime import datetime, timedelta

from app import db, bcrypt


class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    uname = db.Column(db.String(), unique=True, nullable=False)
    name = db.Column(db.String(), unique=True, nullable=False)
    email = db.Column(db.String(), unique=True, nullable=False)
    pw = db.Column(db.String(), nullable=False)
    checking = db.Column(db.Numeric(), nullable = False)
    trading = db.Column(db.Numeric(), nullable = False)
    gender = db.Column(db.String(6), nullable=False)
    phone = db.Column(db.String(10), nullable=False)
    addr = db.Column(db.String(), nullable=False)
    town = db.Column(db.String(), nullable=False)
    state = db.Column(db.String(2), nullable=False)
    zip = db.Column(db.String(5), nullable=False)
    active = db.Column(db.Boolean(), default=False, nullable=False) #TODO implement this
    email_confirmed = db.Column(db.Boolean(), default=False, nullable=False) #TODO implement this
    last_seen = db.Column(db.TIMESTAMP, default=datetime.now(), nullable=False) #TODO implement this
    updated_at = db.Column(db.TIMESTAMP, default=datetime.now(), onupdate=datetime.now(), nullable=False)
    created_at = db.Column(db.TIMESTAMP, default=datetime.now(), nullable=False)

    def __init__(self, id, uname, name, email, pw, checking, trading, gender, phone, addr, town, state, zip, active, email_confirmed, last_seen, updated_at, created_at):
        self.id = id
        self.uname = uname
        self.name = name
        self.email = email
        self.pw = bcrypt.generate_password_hash(pw).decode()
        self.checking = checking
        self.trading = trading
        self.gender = gender
        self.phone = phone
        self.addr = addr
        self.town = town
        self.state = state
        self.zip = zip
        self.active = active
        self.email_confirmed = email_confirmed
        self.last_seen = last_seen
        self.updated_at = updated_at
        self.created_at = created_at

    @property
    def serialize(self):
        return {
            "id": self.id,
            "uname": self.uname,
            "name": self.name,
            "email": self.email,
            "checking": str(self.checking),
            "trading": str(self.trading),
            "gender": self.gender,
            "phone": self.phone,
            "addr": self.addr,
            "town": self.town,
            "state": self.state,
            "zip": self.zip,
            "active": self.active,
            "email_confirmed": self.email_confirmed,
            "last_seen": self.last_seen,
            "updated_at": self.updated_at,
            "created_at": self.created_at
        }

    @property
    def is_authenticated(self):
        return True

    @property
    def is_active(self):
        return True

    def encode_auth_token(self, user_id):
        try:
            return jwt.encode({
                "exp": datetime.now() + timedelta(days=1, seconds=5),
                "iat": datetime.now(),
                "sub": user_id
                }, "asdf", algorithm="HS256")
        except Exception as e:
            return e

    @staticmethod
    def decode_auth_token(token):
        try:
            payload = jwt.decode(token, current_app.config["SECRET_KEY"])
            return payload["sub"]
        except jwt.ExpiredSignatureError:
            return "Signature expired. Please log in again."
        except jwt.InvalidTokenError:
            return "Invalid token. Please log in again."
