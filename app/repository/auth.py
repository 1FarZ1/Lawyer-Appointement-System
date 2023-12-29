
from sqlalchemy.orm import Session
from fastapi import Depends
from app.models import User
from app.schemas.user import UserDto

import app.utils.hash as hash_utils

# class AuthRepository:
#     def __init__(self, db: Session = Depends(get_db)):
#         self.db = db

def create_user(user: UserDto, db: Session):
        db_user = User(
              fname = user.fname,       
                lname = user.lname,
                email=user.email,
                hashed_password=user.password
        )

        db.add(db_user)
        db.commit()
        db.refresh(db_user)
        return db_user

def hash_password(password: str):
    return hash_utils.hash_password(password)