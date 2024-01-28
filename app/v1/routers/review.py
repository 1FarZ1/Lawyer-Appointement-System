from fastapi import APIRouter,Depends, Request
from typing import List
from app.models import Review
from app.config.database import get_db
from sqlalchemy.orm import Session
from fastapi import HTTPException

import app.repository.review as reviewRepository 
import app.repository.lawyer as lawyerRepo
from app.schemas import ReviewSchema
## import permission
from app.utils.check_permission import check_permission
from app.utils.utils import Utils
from app.enums import RoleEnum






router = APIRouter(
    prefix="/api/reviews",
    tags=["reviews"],
)


def checkIfLawyer(request:Request):
    if(request.state.user['role'] != "lawyer"):
        raise HTTPException(
            status_code=401, detail="you cant do this action"
        )





@router.get("/lawyer")
async def get_lawyer_reviews( request:Request , db: Session = Depends(get_db)):
    # await check_permission(request.state.user, [
    #     RoleEnum.LAWYER,
    # ])
    id = request.state.user['id']
    result:List[Review] = reviewRepository.get_lawyer_reviews(db,id)
    return result


@router.post("/add")
async def create_review(reviewSchema:ReviewSchema, request:Request , db: Session = Depends(get_db)):
    # await check_permission(
    #     request.state.user, [
    #     RoleEnum.USER,
    # ])

    if not lawyerRepo.get_lawyer_by_id(db,reviewSchema.lawyer_id):
        raise HTTPException(
            status_code=404, detail="Lawyer not found"
        )
    
    # if reviewRepository.check_if_user_reviewed_lawyer(db,request.state.user['id'],reviewSchema.lawyer_id):
    #     raise HTTPException(
    #         status_code=401, detail="you already reviewed this lawyer"
    #     )
    
    lawyer_rating:list[Review] =await  reviewRepository.get_lawyer_rating(db,reviewSchema.lawyer_id)
    ratings =[
        review.rating for review in lawyer_rating
    ]
    await lawyerRepo.update_lawyer_rating(db,reviewSchema.lawyer_id,Utils.calculate_rating(ratings,reviewSchema.rating) if len(ratings) > 0 else reviewSchema.rating)
    result:Review = await reviewRepository.add_review(db,reviewSchema,request.state.user['id'])
    return result


@router.get("/lawyer/{id}")
async def get_reviews(request:Request, id , db: Session = Depends(get_db)): 
    if not lawyerRepo.get_lawyer_by_id(db,id):
        raise HTTPException(
            status_code=404, detail="Lawyer not found"
        )   
    result:Review = reviewRepository.get_lawyer_reviews(db,id)
    return result

