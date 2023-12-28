from sqlalchemy import Column, Integer, String, Float,ForeignKey
from app.config.database import Base


class Lawyer(Base):
   __tablename__ = "Lawyers"
   id = Column(Integer, primary_key=True, index=True, autoincrement=True)
   name = Column(String(50))
   fname = Column(String(50))
   email = Column(String(100), unique=True)
   phone = Column(String(20))
   address = Column(String(255))
   description = Column(String(255))
   avocat_image = Column(String(255))
   rating = Column(Float)
   social = Column(String(255))
   wilaya = Column(String(50))
   longitude = Column(Float)
   latitude = Column(Float)   
   categories_id = Column(Integer)
