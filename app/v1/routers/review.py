from fastapi import APIRouter,Depends, Request
from typing import List
from app.models import Review
from app.config.database import get_db
from sqlalchemy.orm import Session
from fastapi import HTTPException

import app.repository.review as reviewRepository






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





# @router.post("/lawyer/{id}")
# async def create_review( id , db: Session = Depends(get_db)):
#     result:List[Review] = reviewRepository.get_lawyer_reviews(db,id)
#     return result

## get lawyer rating
# @router.get("/lawyer/{id}/rating")

