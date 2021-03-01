from sqlalchemy import Column, Integer, DateTime, ForeignKey
from database import db
from sqlalchemy.orm import relationship


class Reservation(db.Model):

    __tablename__ = "reservations"

    id = Column(Integer, primary_key=True)
    check_in = Column(DateTime, default=None)
    check_out = Column(DateTime, default=None)
    status = Column(Integer)
    created_at = Column(DateTime, default=None)
    updated_at = Column(DateTime, default=None)
    deleted_at = Column(DateTime, default=None)

    user_id = Column(Integer, ForeignKey('users.id'))
    user = relationship("models.user.User", lazy='subquery')

    hotel_id = Column(Integer, ForeignKey('hotels.id'))
    hotel = relationship("models.hotel.Hotel", lazy='subquery')

    def __repr__(self):
        return "ID:" \
               + str(self.id) \
               + " UserId:" \
               + self.user_id + \
               " HotelId:" \
               + self.hotel_id \
               + self.check_in \
               + self.check_out \
               + self.status


