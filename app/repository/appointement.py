

from sqlalchemy.orm import Session
from app.models import Appointement
from app.schemas import AppointementSchema


def get_lawyer_appointements(db: Session, lawyer_id, skip: int = 0, limit: int = 100) ->  list[Appointement]:
    # return db.query(Appointement).filter(Appointement.lawyer_id == lawyer_id).offset(skip).limit(limit).all()
    return []


def get_appointement_by_id(db: Session, appointement_id: int) -> Appointement:
    return db.query(Appointement).filter(Appointement.id == appointement_id).first()


def create_appointement(db:Session,appointementSchema:AppointementSchema,user_id):
    appointement = Appointement(
        **appointementSchema.model_dump(),
        user_id=1,
        date="23-12-2023"
        )
    db.add(appointement)
    db.commit()
    db.refresh(appointement)
    return appointement

