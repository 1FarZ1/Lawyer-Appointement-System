import datetime
from operator import and_, or_
from typing import List
from sqlalchemy.orm import Session
from app.enums import StatusEnum
from app.models import Categorie, Lawyer, User
from app.schemas import LawyerUserSchema
from app.v1.routers.lawyer import LawyersSearchFilter









def get_lawyer_by_id(db:Session, lawyer_id):  
    return db.query(Lawyer).filter(Lawyer.id == lawyer_id).first()

def get_lawyer_by_email( db: Session, email):
    return  db.query(Lawyer).filter(Lawyer.email == email).first()

def get_lawyer_by_user(
    db: Session, user_id
):
    return  db.query(Lawyer).filter(Lawyer.user_id == user_id).first()


def get_all_pending_lawyers(
    db: Session, skip: int = 0, limit: int = 100
):
    return  db.query(Lawyer).filter(
        Lawyer.status == StatusEnum.PENDING
    ).offset(skip).limit(limit).all()

def get_lawyer_by_name(db : Session, name):
    return db.query(Lawyer).filter(Lawyer.name == name).first()

def get_high_rated_lawyers(db :Session, limit: int = 3):
    return db.query(Lawyer).filter(
        Lawyer.status == StatusEnum.APPROVED
    ).order_by(Lawyer.rating.desc()).limit(limit).all()

def get_all_lawyers(db :Session, skip: int = 0, limit: int = 100):
    return db.query(Lawyer).offset(skip).limit(limit).all()

async def get_all_accepted_lawyers(db :Session, skip: int = 0, limit: int = 100,
    filters:LawyersSearchFilter = None
                             ):
    query =  db.query(Lawyer).filter(Lawyer.status == StatusEnum.APPROVED)

    if filters:
        if filters.specialty:
            query =  query.join(Lawyer.categorie).filter(Categorie.id == filters.specialty)

        if filters.name:          
            query =  query.join(Lawyer.user).filter(
                or_(
                    User.fname.ilike(f"%{filters.name}%"),  
                    User.lname.ilike(f"%{filters.name}%")   
                )
            )

        if filters.wilaya_id:
            query = query.filter(Lawyer.wilaya_id == filters.wilaya_id)
            if filters.city_id:
                query = query.filter(Lawyer.city_id == filters.city_id)
    

        if filters.adress:
            query = query.filter(Lawyer.address.ilike(f"%{filters.adress}%"))

        if filters.isTopRated:
            query = query.order_by(Lawyer.rating.desc())

    return query.offset(skip).limit(limit).all();   
    
def create_new_lawyer(db : Session, lawyerSchema : LawyerUserSchema ,
                      user_id):
    lawyer:Lawyer = Lawyer(
       **lawyerSchema.model_dump(),
       user_id= user_id,

    )
    db.add(lawyer)
    db.commit()
    db.refresh(lawyer)
    return lawyer

async def change_status(db:Session,lawyer_id,status):
    lawyer = db.query(Lawyer).filter(Lawyer.id == lawyer_id).first()
    lawyer.status = status
    db.commit()
    db.refresh(lawyer)
    return lawyer

async def update_lawyer_rating(db:Session,lawyer_id,new_rating):
    lawyer = db.query(Lawyer).filter(Lawyer.id == lawyer_id).first()
    lawyer.rating = new_rating 
    lawyer.n_reviews += 1
    db.commit()
    db.refresh(lawyer)
    return lawyer


## get lawyer schedules
def get_lawyer_schedules(db:Session,lawyer_id):
    lawyer:Lawyer = db.query(Lawyer).filter(Lawyer.id == lawyer_id).first()
    return lawyer.lawyer_schedule

