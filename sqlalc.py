from sqlalchemy import creat_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

url = 'mysql+pymysql://root:Li009294@localhost/tokyo_hotels?charset=utf8'
engine = create_engine(url, echo=True)
Base = declarative_base()


class Hotel(Base):
    __tablename__ = "hotels"

    id = Column(Integer, primany_key=True)
    name = Column(String(255))
    name_en = Column(String(255))
    img_src = Column(String(255))
    district_id = Column(Integer)
    address = Column(String(255))
    price = Column(Integer)
    station = Column(String(255))
    summary = Column(String(255))
    introduction = Column(String(255))
    room_size = Column(Integer)
    max_ppl = Column(Integer)
    equipments = Column(String(255))


Session = sessionmaker(bind=engine)
ses = Session()

hotels = ses.query(Hotel).all()
ses.close()
