from fastapi import APIRouter, Depends, HTTPException, status
from typing import List
from app.models.lawyer import Lawyer
import app.repository.lawyer as lawyerRepo
from app.config.database import get_db

from app.schemas.lawyer import LawyerDto    

router = APIRouter(
    prefix="/api/lawyers",
    # tags=["lawyers"],
    # dependencies=[Depends(get_token_header)],
    responses={404: {"description": "Not found"}},
)





@router.get("/")
async def get_lawyers(page: int = 0, pageSize: int = 100, db = Depends(get_db)):
    result:List[Lawyer] = lawyerRepo.get_all_lawyers(db,page, pageSize)
    return result


@router.post("/")
async def create_lawyer(lawyer: LawyerDto, db = Depends(get_db)):
    try: 
        result  = lawyerRepo.create_new_lawyer(db,lawyer)
        if not result:
            raise HTTPException(
                status_code=500, detail="Internal server error"
            )
        return result

    except Exception as e:
        return {
            "message": e
        }
    
  





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




# @router.get("/reviews")
# async def get_reviews():
#     return {
#         "message":"not implemented yet"
#     }



# @router.get("/{id}/reviews")
# async def get_reviews_lawyer(id: int):
#     return {
#         "message":"not implemented yet"
#     }

