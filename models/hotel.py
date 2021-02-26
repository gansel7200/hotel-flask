from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from database import db


class Hotel(db.Model):

    __tablename__ = "hotels"

    id = Column(Integer, primary_key=True)
    name = Column(String(255))
    name_en = Column(String(255))
    img_src = Column(String(255))
    address = Column(String(255))
    price = Column(Integer)
    station = Column(String(255))
    summary = Column(String(255))
    introduction = Column(String(255))
    room_size = Column(Integer)
    max_ppl = Column(Integer)
    equipments = Column(String(255))
    created_at = Column(DateTime, default=None)
    updated_at = Column(DateTime, default=None)
    deleted_at = Column(DateTime, default=None)

    district_id = Column(Integer, ForeignKey('districts.id'))
    district = relationship("models.district.District", lazy='subquery')

    reservations = relationship("Reservation", back_populates="hotel")

    def __repr__(self):
        return self.name





