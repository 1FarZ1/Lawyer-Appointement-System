from sqlalchemy import Column, Integer, String, Float
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
   categories = Column(String(255))  # Assuming a comma-separated string for categories
   schedule = Column(String(255))  # Assuming a serialized format for schedule
   rating = Column(Float)
   comments = Column(String(255))  # Assuming a serialized format for comments
   social = Column(String(255))
   wilaya = Column(String(50))
   longitude = Column(Float)
   latitude = Column(Float)
