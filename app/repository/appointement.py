

from sqlalchemy.orm import Session
from app.models import Appointement
from app.schemas import AppointementSchema


def get_lawyer_appointements(db: Session, lawyer_id, skip: int = 0, limit: int = 100) ->  list[Appointement]:

    return db.query(Appointement).filter(Appointement.lawyer_id == lawyer_id).offset(skip).limit(limit).all()

#.filter(Appointement.status == "Accepted")


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

def accept_appointement(db:Session , id):
    appointement = db.query(Appointement).filter(Appointement.id == id).first()
    appointement.status = "Accepted"
    db.commit()
    db.refresh(appointement)
    return appointement

def reject_appointement(db:Session , id):
    appointement = db.query(Appointement).filter(Appointement.id == id).first()
    appointement.status = "Rejected"
    db.commit()
    db.refresh(appointement)
    return appointement