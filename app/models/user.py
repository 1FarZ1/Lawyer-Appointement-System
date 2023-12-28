from sqlalchemy import Column, Integer, String, Float
from app.config.database import Base


class User(Base):
    __tablename__ = "Users"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    username = Column(String(20), unique=True)
    email = Column(String(20), unique=True)
    profile_picture = Column(String(20))
    hashed_password = Column(String(20))