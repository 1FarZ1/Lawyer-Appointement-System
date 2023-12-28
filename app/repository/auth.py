
from sqlalchemy.orm import Session
from fastapi import Depends
from app.models.user import User
from app.schemas.user import UserDto

from app.utils.hash import hash_password

# class AuthRepository:
#     def __init__(self, db: Session = Depends(get_db)):
#         self.db = db

def create_user(user: UserDto, db: Session):
        db_user = User(
                fname = user.fname,
                lname = user.lname,
                email=user.email,
                password=user.password,
        )

        print(db_user)
        # db.add(db_user)
        # db.commit()
        # db.refresh(db_user)
        return db_user

def hash_password(password: str):
    return hash_password(password)