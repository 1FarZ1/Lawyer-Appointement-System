
from typing import Optional
from sqlalchemy.orm import Session
from fastapi import Depends
from app.enums import RoleEnum
from app.models import User
from app.schemas import GoogleUserSchema
from app.utils.jwt import JWT
from datetime import datetime

import app.utils.hash as hash_utils

def register_user(googleUserSchema, db: Session,isGoogleUser:Optional[bool]=False ,role:Optional[RoleEnum] = None):
        db_user = User(
                     **googleUserSchema.model_dump(),
                    createdAt = datetime.now(), 
                    **({"role":role} if role else {}),
        )
        db.add(db_user)
        db.commit()
        db.refresh(db_user)
        return db_user





def hash_password(password: str):
    return hash_utils.hash_password(password)

def verify_password(plain_password, hashed_password):
    return hash_utils.verify_password(plain_password, hashed_password)