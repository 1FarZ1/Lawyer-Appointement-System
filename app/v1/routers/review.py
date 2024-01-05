from fastapi import APIRouter,Depends, Request
from typing import List
from app.models import Review
from app.config.database import get_db
from sqlalchemy.orm import Session
from fastapi import HTTPException

import app.repository.review as reviewRepository
from app.schemas import ReviewSchema






router = APIRouter(
    prefix="/api/reviews",
    tags=["reviews"],
)



@router.get("/{id}")
async def get_reviews(request:Request, id , db: Session = Depends(get_db)):    
    result:Review = reviewRepository.get_review_by_id(db,id)
    if not result:
        raise HTTPException(
            status_code=404, detail="Review not found"
        )
    return result


@router.get("/lawyer/")
async def get_lawyer_reviews( request:Request , db: Session = Depends(get_db)):
    if(request.state.role != "lawyer"):
        raise HTTPException(
            status_code=401, detail="Unauthorized"
        )
    id = request.state.user['id']
    result:List[Review] = reviewRepository.get_lawyer_reviews(db,id)
    return result





@router.post("/lawyer/")
async def create_review(reviewSchema:ReviewSchema, request:Request , db: Session = Depends(get_db)):

    if(request.state.role != "user"):
        raise HTTPException(
            status_code=401, detail="you cant do this action"
        )
    





    result:List[Review] = reviewRepository.add_review(db,reviewSchema,user_id)
    return result

## get lawyer rating
# @router.get("/lawyer/{id}/rating")

