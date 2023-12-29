

from sqlalchemy.orm import Session
from app.models import Review



def get_lawyer_reviews (db: Session, lawyer_id):
    return db.query(Review).filter(Review.lawyer_id == lawyer_id).all()

def get_review_by_id(db: Session, review_id):
    return db.query(Review).filter(Review.id == review_id).first()
    
def get_review_by_user_id(db: Session, user_id):
    return db.query(Review).filter(Review.user_id == user_id).first()