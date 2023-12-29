from sqlalchemy.orm import Session
from app.models.lawyer import Lawyer
from app.schemas.lawyer import LawyerDto

# class LawyerRepository:
#     def __init__(self, db :Session = Depends(get_db)):
#         self.db = db

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
def create_new_lawyer(db : Session, lawyer_dto : LawyerDto ):
    lawyer:Lawyer = Lawyer(
        phone = lawyer_dto.phone,
        address = lawyer_dto.address,
        description = lawyer_dto.description,
        avocat_image = lawyer_dto.avocat_image,
        rating = lawyer_dto.rating,
        social = lawyer_dto.social,
        wilaya = lawyer_dto.wilaya,
        longitude = lawyer_dto.longitude,
        latitude = lawyer_dto.latitude, 
        #categories_id = lawyer_dto.categories_id,
        user_id = lawyer_dto.user_id
    )
    print(str(lawyer))

    db.add(lawyer)
    db.commit()
    db.refresh(lawyer)
    print(lawyer)
    return lawyer

