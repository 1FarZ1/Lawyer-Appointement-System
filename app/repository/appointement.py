

from sqlalchemy.orm import Session
from app.models import Appointement


def get_lawyer_appointements(db: Session, lawyer_id, skip: int = 0, limit: int = 100) ->  list[Appointement]:
    # return db.query(Appointement).filter(Appointement.lawyer_id == lawyer_id).offset(skip).limit(limit).all()
    return []


def get_appointement_by_id(db: Session, appointement_id: int) -> Appointement:
    return db.query(Appointement).filter(Appointement.id == appointement_id).first()


