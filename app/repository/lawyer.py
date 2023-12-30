from sqlalchemy.orm import Session
from app.models import Lawyer
from app.schemas import LawyerSchema

def get_lawyer_by_id(db:Session, lawyer_id):  
        return db.query(Lawyer).filter(Lawyer.id == lawyer_id).first()

def get_lawyer_by_email( db: Session, email):
    return db.query(Lawyer).filter(Lawyer.email == email).first()

def get_lawyer_by_name(db : Session, name):
    return db.query(Lawyer).filter(Lawyer.name == name).first()

def get_high_rated_lawyers(db :Session, limit: int = 3):
    return db.query(Lawyer).order_by(Lawyer.rating.desc()).limit(limit).all()


def get_all_lawyers(db :Session, skip: int = 0, limit: int = 100):
    return db.query(Lawyer).offset(skip).limit(limit).all()
def create_new_lawyer(db : Session, lawyerSchema : LawyerSchema ):
    lawyer:Lawyer = Lawyer(
       **lawyerSchema.model_dump()
    )
    

    db.add(lawyer)
    db.commit()
    db.refresh(lawyer)
    return lawyer

