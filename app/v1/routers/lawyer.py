

from fastapi import APIRouter, Depends, HTTPException, status
from typing import List
import random
import json
from app.models.lawyer import Lawyer
from app.repository.lawyer import LawyerRepository
from app.config.database import get_db






router = APIRouter(
    prefix="/api/lawyers",
    # tags=["lawyers"],
    # dependencies=[Depends(get_token_header)],
    responses={404: {"description": "Not found"}},
)



db = get_db()
lawyerRepo : LawyerRepository = LawyerRepository(db)


@router.get("/")
async def get_lawyers(page: int = 0, pageSize: int = 10,):
    result:List[Lawyer] = lawyerRepo.get_all_lawyers(page, pageSize)
    return result



@router.get("/reviews")
async def get_reviews():
    return {
        "message":"not implemented yet"
    }


@router.get("/highest_rated")
async def get_highest_rated(limit: int = 4):
    return lawyerRepo.get_high_rated_lawyers(limit)


@router.get("/{id}")
async def get_lawyer(id: int):
    result:Lawyer = lawyerRepo.get_lawyer_by_id(id)
    if not result:
        raise HTTPException(
            status_code=404, detail="Lawyer not found"
        )
    return result


@router.get("/{id}/reviews")
async def get_reviews_lawyer(id: int):
    return {
        "message":"not implemented yet"
    }

