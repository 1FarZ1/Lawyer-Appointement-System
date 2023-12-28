from sqlalchemy.orm import Session
from app.models.lawyer import Lawyer
from app.schemas.lawyer import LawyerDto


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
    def create_new_lawyer(self, lawyer_dto : LawyerDto ):
        lawyer:Lawyer = Lawyer()
        lawyer.name = lawyer_dto.name
        lawyer.fname = lawyer_dto.fname
        lawyer.email = lawyer_dto.email
        lawyer.phone = lawyer_dto.phone
        lawyer.address = lawyer_dto.address
        lawyer.description = lawyer_dto.description
        lawyer.avocat_image = lawyer_dto.avocat_image
        lawyer.rating = lawyer_dto.rating
        lawyer.social = lawyer_dto.social
        lawyer.wilaya = lawyer_dto.wilaya
        lawyer.longitude = lawyer_dto.longitude
        lawyer.latitude = lawyer_dto.latitude
        lawyer.categories_id = lawyer_dto.categories_id
        
        
        self.db.add(lawyer)
        self.db.commit()
        self.db.refresh(lawyer)
        return lawyer
    
    