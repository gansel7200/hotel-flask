from sqlalchemy import Column, Integer, String, DateTime
from database import db
from sqlalchemy.orm import relationship


class User(db.Model):

    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    name = Column(String(255))
    katakana_name = Column(String(255))
    mail = Column(String(255))
    password = Column(String(255))
    telephone = Column(Integer)
    created_at = Column(DateTime, default=None)
    updated_at = Column(DateTime, default=None)
    deleted_at = Column(DateTime, default=None)

    reservations = relationship("Reservation", back_populates="user")

    def __repr__(self):
        return self.name

