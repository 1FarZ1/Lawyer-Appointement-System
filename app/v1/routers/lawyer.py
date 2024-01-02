from fastapi import APIRouter, Depends, HTTPException, Request, status
from typing import List
from app.models import Lawyer
import app.repository.lawyer as lawyerRepo
from app.config.database import get_db

from utils.check_permission import check_permission
from app.schemas import LawyerSchema    

from app.enums import RoleEnum
router = APIRouter(
    prefix="/api/lawyers",
    tags=["lawyers"],
    # dependencies=[Depends(get_token_header)],
    responses={404: {"description": "Not found"}},
)





@router.get("/")
async def get_lawyers(request:Request,page: int = 0, pageSize: int = 100, db = Depends(get_db)):
    check_permission(request.state.user, [
        RoleEnum.ADMIN,
    ])
    result:List[Lawyer] = lawyerRepo.get_all_lawyers(db,page, pageSize)
    return result


@router.post("/")
async def create_lawyer(lawyer: LawyerSchema, db = Depends(get_db)):
        result  = lawyerRepo.create_new_lawyer(db,lawyer)
        if not result:
            raise HTTPException(
                status_code=500, detail="Internal server error"
            )
        return result

   
@router.get("/highest_rated")
async def get_highest_rated(limit: int = 4, db = Depends(get_db)):
    return lawyerRepo.get_high_rated_lawyers(db,limit)



@router.get("/{id}")
async def get_lawyer(id: int, db = Depends(get_db)):
    result:Lawyer = lawyerRepo.get_lawyer_by_id(db,id)
    if not result:
        raise HTTPException(
            status_code=404, detail="Lawyer not found"
        )
    return result


