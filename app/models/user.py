from sqlalchemy import Column, Integer, String, Float
from app.config.database import Base
from sqlalchemy.orm import relationship


class User(Base):
    __tablename__ = "user"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    fname = Column(String(25),)
    lname = Column(String(25))
    email = Column(String(20), unique=True)
    hashed_password = Column(String(20))    
    lawyer = relationship("Lawyer", back_populates="user")
    review = relationship("Review", back_populates="user")
#    createdAt = Column(dt.Datetime)