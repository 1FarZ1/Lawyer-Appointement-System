from sqlalchemy import Column, Integer, String, Float,ForeignKey
from app.config.database import Base

from sqlalchemy.orm import relationship

class Lawyer(Base):
   __tablename__ = "lawyer"
   id = Column(Integer, primary_key=True, index=True, autoincrement=True)
   phone = Column(String(20))
   address = Column(String(255))
   description = Column(String(255))
   avocat_image = Column(String(255))
   rating = Column(Float)
   social = Column(String(255))
   wilaya = Column(String(50))
   longitude = Column(Float)
   latitude = Column(Float)   
   categories_id = Column(Integer, ForeignKey('categorie.id') )
   cateogorie = relationship("Category", back_populates="lawyer")
   user_id = Column(Integer, ForeignKey('user.id'))
   user = relationship("User", back_populates="lawyer")
   review = relationship("Review", back_populates="lawyer")


class Category(Base):
   __tablename__ = "categorie"
   id = Column(Integer, primary_key=True, index=True, autoincrement=True)
   name = Column(String(50))
   lawyers = relationship("Lawyer", back_populates="cateogorie")
## description = Column(String(255))
## image = Column(String(255))
## icon = Column(String(255))
## parent_id = Column(Integer,ForeignKey('Categories.id'),nullable=True)
## parent = relationship("Category", backref="children", remote_side=[id])
## children = relationship("Category")
## lawyers = relationship("Lawyer", back_populates="category")
