
from typing import Optional
from sqlalchemy.orm import Session
from fastapi import Depends
from app.models import User
from app.schemas import UserSchema
from app.utils.jwt import JWT
from datetime import datetime

import app.utils.hash as hash_utils

def create_user(userSchema: UserSchema, db: Session,isGoogleUser:Optional[bool]=False ):
        db_user = User(
                     **userSchema.model_dump(),
                    createdAt = datetime.now(), 
        )
        db.add(db_user)
        db.commit()
        db.refresh(db_user)
        return db_user


def hash_password(password: str):
    return hash_utils.hash_password(password)

def verify_password(plain_password, hashed_password):
    return hash_utils.verify_password(plain_password, hashed_password)