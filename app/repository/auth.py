
from sqlalchemy.orm import Session
from fastapi import Depends
from app.models.user import User

class AuthRepository:
    def __init__(self, db: Session = Depends(get_db)):
        self.db = db

    def create_user(self, user: UserCreate):
        db_user = User(
            email=user.email,
            hashed_password=get_password_hash(user.password),
            is_active=True,
        )
        self.db.add(db_user)
        self.db.commit()
        self.db.refresh(db_user)
        return db_user
