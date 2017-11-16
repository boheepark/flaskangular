from datetime import datetime

from asdf import db

class Trade(db.Model):
    __tablename__ = "trades"
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, nullable=False)
    company = db.Column(db.String(), nullable=False)
    price = db.Column(db.Numeric(), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    total = db.Column(db.Numeric(), nullable=False)
    created_at = db.Column(db.TIMESTAMP, default=datetime.now(), nullable=False)

    def __init__(self, id, user_id, company, price, quantity, total, created_at):
        self.id = id
        self.user_id = user_id
        self.company = company
        self.price = price
        self.quantity = quantity
        self.total = total
        self.created_at = created_at

    @property
    def serialize(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "company": self.company,
            "price": str(self.price),
            "quantity": self.quantity,
            "total": str(self.total),
            "created_at": self.created_at
        }
