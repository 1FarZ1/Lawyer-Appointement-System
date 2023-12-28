from sqlalchemy.orm import Session
from app.models.user import User

class UserRepository:
    def __init__(self, db : Session):
        self.db = db

    def get_user_by_id(self, user_id):
        return self.db.query(User).filter(User.id == user_id).first()

    def get_user_by_email(self, email):
        return self.db.query(User).filter(User.email == email).first()

    def get_all_users(self):
        return self.db.query(User).all()
    
    def check_username(self, username):
        return self.db.query(User).filter(User.username == username).first()
    
    def update_username(self, user_id, username):
        user = self.db.query(User).filter(User.id == user_id).first()
        if not user:
            return None
        user.username = username
        self.db.commit()
        self.db.refresh(user)
        return user

    def delete_user(self, user_id):
        return self.db.query(User).filter(User.id == user_id).delete()