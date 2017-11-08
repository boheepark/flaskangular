from sqlalchemy import Column, Integer, Numeric, String, ForeignKey, TIMESTAMP, func

from datetime import datetime

from asdf import db

class Trade(db.Model):
    __tablename__ = "trades"
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("user.id"), nullable=False)
    company = Column(String(), nullable=False)
    price = Column(Numeric(), nullable=False)
    quantity = Column(Integer, nullable=False)
    total = Column(Numeric(), nullable=False)
    # created_at = Column(TIMESTAMP, default=datetime.utcnow(), server_default=func.now(), nullable=False)
    created_at = Column(TIMESTAMP, default=datetime.now(), server_default=func.now(), nullable=False)

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
