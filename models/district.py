from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from database import db


class District(db.Model):
    __tablename__ = "districts"

    id = Column(Integer, primary_key=True)
    name = Column(String(255))

    hotels = relationship("Hotel", back_populates="district")

    def __repr__(self):
        return self.name

