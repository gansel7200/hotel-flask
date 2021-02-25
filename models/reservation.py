from sqlalchemy import Column, Integer, DateTime
from database import db


class Reservation(db.Model):

    __tablename__ = "reservations"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer)
    hotel_id = Column(Integer)
    check_in = Column(DateTime, default=None)
    check_out = Column(DateTime, default=None)
    created_at = Column(DateTime, default=None)
    updated_at = Column(DateTime, default=None)
    deleted_at = Column(DateTime, default=None)