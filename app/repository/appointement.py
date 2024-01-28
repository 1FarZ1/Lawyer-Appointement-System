

from sqlalchemy.orm import Session
from app.models import Appointement
from app.schemas import AppointementSchema




## get all appointements
def get_all_appointements(db: Session, skip: int = 0, limit: int = 100) ->  list[Appointement]:
    return db.query(Appointement).offset(skip).limit(limit).all()



def get_lawyer_appointements(db: Session, lawyer_id, skip: int = 0, limit: int = 100) ->  list[Appointement]:
    return db.query(Appointement).filter(Appointement.lawyer_id == lawyer_id).offset(skip).limit(limit).all()

#.filter(Appointement.status == "Accepted")

def get_lawyer_pending_appointements(
    db: Session, lawyer_id, skip: int = 0, limit: int = 100
) ->  list[Appointement]:
    return db.query(Appointement).filter(Appointement.lawyer_id == lawyer_id).filter(Appointement.status == "Pending").offset(skip).limit(limit).all()



def get_lawyer_accepted_appointements(db: Session, lawyer_id, skip: int = 0, limit: int = 100) ->  list[Appointement]:

    return db.query(Appointement).filter(Appointement.lawyer_id == lawyer_id).filter(Appointement.status == "Approved").offset(skip).limit(limit).all()

def get_user_appointements(db: Session, user_id, skip: int = 0, limit: int = 100) ->  list[Appointement]:
        return db.query(Appointement).filter(Appointement.user_id == user_id).offset(skip).limit(limit).all()



def check_appointement_with_user(db: Session, lawyer_id, user_id) ->  bool:
    return db.query(Appointement).filter(Appointement.lawyer_id == lawyer_id).filter(Appointement.user_id == user_id).first() != None

def check_appointement_with_lawyer(db: Session,appointementSchema:AppointementSchema) ->  bool:
    return db.query(Appointement).filter(Appointement.lawyer_id == appointementSchema.lawyer_id).filter(Appointement.date == appointementSchema.date).filter(Appointement.time == appointementSchema.time).first() != None

def get_appointement_by_id(db: Session, appointement_id: int) -> Appointement:
    return db.query(Appointement).filter(Appointement.id == appointement_id).first()


def create_appointement(db:Session,appointementSchema:AppointementSchema,user_id):
    appointement = Appointement(
        **appointementSchema.model_dump(),
        user_id=user_id,
        )
    db.add(appointement)
    db.commit()
    db.refresh(appointement)
    return appointement


def get_appointement_by_id(db:Session , id):
    appointement = db.query(Appointement).filter(Appointement.id == id).first()
    return appointement

def appointement_belong_to_lawyer(db:Session,id,lawyer_id):
    appointement = db.query(Appointement).filter(Appointement.id == id).first()
    if not appointement:
        return False
    return appointement.lawyer_id == lawyer_id
def respond_appointement(db:Session,appointement_id,status):
    appointement = db.query(Appointement).filter(Appointement.id == appointement_id).first()
    appointement.status = status
    db.commit()
    db.refresh(appointement)
    return appointement
