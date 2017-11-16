from sqlalchemy import Column, Integer, Numeric, String, Boolean, TIMESTAMP, func

import jwt
from datetime import datetime, timedelta

from asdf import db, bcrypt


class User(db.Model):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    uname = Column(String(), unique=True, nullable=False)
    name = Column(String(), unique=True, nullable=False)
    email = Column(String(), unique=True, nullable=False)
    pw = Column(String(), nullable=False)
    checking = Column(Numeric(), nullable = False)
    trading = Column(Numeric(), nullable = False)
    gender = Column(String(6), nullable=False)
    phone = Column(String(10), nullable=False)
    addr = Column(String(), nullable=False)
    town = Column(String(), nullable=False)
    state = Column(String(2), nullable=False)
    zip = Column(String(5), nullable=False)
    active = Column(Boolean(), default=False, nullable=False) #NOTE implement this
    last_seen = Column(TIMESTAMP, default=datetime.now(), server_default=func.now(), nullable=False)
    updated_at = Column(TIMESTAMP, default=datetime.now(), server_default=func.now(), nullable=False)
    created_at = Column(TIMESTAMP, default=datetime.now(), server_default=func.now(), nullable=False)

    def __init__(self, id, uname, name, email, pw, checking, trading, gender, phone, addr, town, state, zip, active, last_seen, updated_at, created_at):
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
            # payload = jwt.decode(token, app.config["SECRET_KEY"])
            payload = jwt.decode(token, "asdf")
            return payload["sub"]
        except jwt.ExpiredSignatureError:
            return "Signature expired. Please log in again."
        except jwt.InvalidTokenError:
            return "Invalid token. Please log in again."
