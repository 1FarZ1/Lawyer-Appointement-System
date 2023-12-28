from sqlalchemy.orm import Session
from app.models.lawyer import Lawyer

class LawyerRepository:
    def __init__(self, db : Session):
        self.db = db

    def get_lawyer_by_id(self, lawyer_id):  
        return self.db.query(Lawyer).filter(Lawyer.id == lawyer_id).first()
    
    def get_lawyer_by_email(self, email):
        return self.db.query(Lawyer).filter(Lawyer.email == email).first()
    
    def get_lawyer_by_name(self, name):
        return self.db.query(Lawyer).filter(Lawyer.name == name).first()
    
    def get_high_rated_lawyers(self, limit: int = 3):
        return self.db.query(Lawyer).order_by(Lawyer.rating.desc()).limit(limit).all()
    
    def get_all_lawyers(self, skip: int = 0, limit: int = 100):
        return self.db.query(Lawyer).offset(skip).limit(limit).all()
    def create_new_lawyer(self, lawyer):
        self.db.add(lawyer)
        self.db.commit()
        self.db.refresh(db_lawyer)
        return db_lawyer
    
    