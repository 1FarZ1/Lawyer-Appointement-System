from sqlalchemy.orm import Session
from app.models import User

def get_user_by_id(user_id, db : Session):
    return db.query(User).filter(User.id == user_id).first()
def get_user_by_email(email:str, db : Session):
    return db.query(User).filter(User.email == email).first()
def get_all_users(db : Session,skip: int = 0, limit: int = 100, sort: str = None):
    if sort:
        sort_attr = getattr(User, sort.replace("-", ""))
        if sort.startswith("-"):
            sort_attr = sort_attr.desc()
        return db.query(User).order_by(sort_attr).offset(skip).limit(limit).all()
    return db.query(User).offset(skip).limit(limit).all()

def update_email(user_id, email:str, db : Session):
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        return None
    user.email =  email
    db.commit()
    db.refresh(user)
    return user

def update_image(user_id, imageUrl:str, db : Session):
    user : User = db.query(User).filter(User.id == user_id).first()
    if not user:
        return None
    user.profile_picture =  imageUrl
    db.commit()
    db.refresh(user)
    return user

def update_password(user_id,newPassword,current_password,db:Session):
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        return None
    if user.password != current_password:
        return None
    user.password = newPassword
    db.commit()
    db.refresh(user)
    return user

def delete_user( user_id, db : Session):
    return db.query(User).filter(User.id == user_id).delete()