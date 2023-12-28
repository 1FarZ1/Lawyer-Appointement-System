from sqlalchemy.orm import Session
from app.models.user import User

# class UserRepository:
#     def __init__(self, db : Session):
#         self.db = db

def get_user_by_id(user_id, db : Session):
    return db.query(User).filter(User.id == user_id).first()
def get_user_by_email( email, db : Session):
    return db.query(User).filter(User.email == email).first()
def get_all_users(db : Session,skip: int = 0, limit: int = 100):
    return db.query(User).offset(skip).limit(limit).all()

def check_username(username, db : Session):
    return db.query(User).filter(User.username == username).first()

def update_username(user_id, username, db : Session):
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        return None
    user.username = username
    db.commit()
    db.refresh(user)
    return user

def update_image(user_id, image, db : Session):
    user : User = db.query(User).filter(User.id == user_id).first()
    if not user:
        return None
    user.profile_picture =  image
    db.commit()
    db.refresh(user)
    return user
def delete_user( user_id, db : Session):
    return db.query(User).filter(User.id == user_id).delete()