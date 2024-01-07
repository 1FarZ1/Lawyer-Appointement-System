

from sqlalchemy.orm import Session
from app.models import Review
from app.schemas import ReviewSchema



def get_lawyer_reviews(db: Session, lawyer_id):
    return db.query(Review).filter(Review.lawyer_id == lawyer_id).all()

def get_review_by_id(db: Session, review_id):
    return db.query(Review).filter(Review.id == review_id).first()
    
def get_user_reviews(db: Session, user_id):
    return db.query(Review).filter(Review.user_id == user_id).first()

def check_if_user_reviewed_lawyer(db: Session, user_id, lawyer_id):
    return db.query(Review).filter(Review.user_id == user_id).filter(Review.lawyer_id == lawyer_id).first()


async def add_review(db:Session,reviewSchema:ReviewSchema,user_id):
    review = Review(
        **reviewSchema.model_dump(),
        user_id=user_id

    )
    db.add(review)
    db.commit()
    db.refresh(review)
    return review


async def get_lawyer_rating(
    db: Session, lawyer_id
):
## calculate the lawyer rating 
    reviews = db.query(Review).filter(Review.lawyer_id == lawyer_id).all()
    return reviews