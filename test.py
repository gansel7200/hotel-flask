from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

url = 'mysql+pymysql://root:Li009294@localhost/tokyo_hotels?charset=utf8'
engine = create_engine(url, echo=True)
Base = declarative_base()


class Hotel(Base):
    __tablename__ = "hotels"

    id = Column(Integer, primary_key=True)
    name = Column(String(255))
    name_en = Column(String(255))
    station = Column(String(255))




Session = sessionmaker(bind=engine)
ses = Session()
hotels = ses.query(Hotel).all()

for hotel in hotels:
    print(hotel.name)






