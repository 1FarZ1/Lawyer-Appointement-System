
from sqlalchemy.orm import Session
from fastapi import Depends
from app.models import User
from app.schemas import UserSchema

import app.utils.hash as hash_utils
def create_user(user: UserSchema, db: Session):
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