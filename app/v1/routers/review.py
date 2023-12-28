from fastapi import APIRouter,Depends
from typing import List
from app.models.review import Review
from app.config.database import get_db
from sqlalchemy.orm import Session






router = APIRouter(
    prefix="/api/reviews",
)



@router.get("/{id}")
async def get_reviews( id , db: Session = Depends(get_db)):
    result:List[Review] = db.query(Review).filter(Review.id == id).all()
    return result


@router.get("/lawyer/{id}")
async def get_reviews_by_lawyer( id , db: Session = Depends(get_db)):
    result:List[Review] = db.query(Review).filter(Review.lawyer_id == id).all()
    return result

## get lawyer rating
# @router.get("/lawyer/{id}/rating")
