from fastapi import APIRouter, Depends, HTTPException, Request, status
from typing import List, Optional

from pydantic import BaseModel
from app.models import Lawyer
import app.repository.lawyer as lawyerRepo 
import app.repository.category as categoryRepo
from app.config.database import get_db

from app.utils.check_permission import check_permission
from app.schemas import LawyerSchema    

from app.enums import RoleEnum, StatusEnum
router = APIRouter(
    prefix="/api/lawyers",
    tags=["lawyers"],
    # dependencies=[Depends(get_token_header)],
    responses={404: {"description": "Not found"}},
)



class ApproveSchema(BaseModel):
    id: int
    is_Approved: bool
    rejection_reason: Optional[str] = None 



    




@router.get("/")
async def get_lawyers(request:Request,page: int = 0, pageSize: int = 100, db = Depends(get_db)):
    # check_permission(request.state.user, [
    #     RoleEnum.ADMIN,
    # ])
    result:List[Lawyer] = lawyerRepo.get_all_lawyers(db,page, pageSize)
    return result

@router.get('/schedule')
async def get_lawyer_schedule(request:Request,db = Depends(get_db)):
    check_permission(request.state.user, [
        RoleEnum.LAWYER,
    ])
    id = request.state.user['id']

    laywer :Lawyer = lawyerRepo.get_lawyer_by_user(db,id)


    result = lawyerRepo.get_lawyer_schedules(db,lawyer_id=laywer.id)
    ## add a field  , because in result i  have start time : 8:00:00 and end time 10:00:00 , make the new field like 8am-10am

    

    return result



class LawyersSearchFilter(BaseModel):
    specialty: Optional[int] = None
    wilaya_id: Optional[int] = None
    city_id: Optional[int] = None
    adress: Optional[str] = None
    name : Optional[str] = None
    isTopRated : Optional[bool] = None

    
@router.get("/user")
async def get_accepted_lawyers(request:Request,page: int = 0, pageSize: int = 100, 
    filters:LawyersSearchFilter = Depends(),
                               db = Depends(get_db)):
    print("Filters:", filters)
    result:List[Lawyer] = await lawyerRepo.get_all_accepted_lawyers(db,page, pageSize,filters=filters)
    return result

   
@router.get("/highest_rated")
async def get_highest_rated(limit: int = 4, db = Depends(get_db)):
    return lawyerRepo.get_high_rated_lawyers(db,limit)

@router.get('/pending')
async def get_pending_lawyers(request:Request,page: int = 0, pageSize: int = 100, db = Depends(get_db)):
    # check_permission(request.state.user, [
    #     RoleEnum.USER,
    # ])
    result:List[Lawyer] = lawyerRepo.get_all_pending_lawyers(db,page, pageSize)
    return result


@router.get('/categories')
async def get_lawyer_categories(
    db = Depends(get_db),
):
    return categoryRepo.get_lawyer_categories(db=db)




@router.patch("/lawyer/response")
async def approve_lawyer(request:Request,approaveSchema:ApproveSchema,db=Depends(get_db)):

    check_permission(request.state.user,[
        RoleEnum.ADMIN
])
    lawyer:Lawyer = lawyerRepo.get_lawyer_by_id(db,lawyer_id=approaveSchema.id)
    if not lawyer:
        raise HTTPException(
            status_code=404, detail="Lawyer not found"
        )
    result =  await lawyerRepo.change_status(db,approaveSchema.id, StatusEnum.APPROVED if approaveSchema.is_Approved else StatusEnum.REJECTED)
    return result


class LawyerUpdateSchema(BaseModel):
    name: Optional[str] = None
    email: Optional[str] = None
    phone: Optional[str] = None
    address: Optional[str] = None
    password: Optional[str] = None
    image: Optional[str] = None
    experience: Optional[str] = None

@router.patch("/lawyer/update")
def update_lawyer_profile(request:Request,lawyer:LawyerUpdateSchema,db=Depends(get_db)):
    check_permission(request.state.user,[
        RoleEnum.LAWYER
])
    

    result =  lawyerRepo.update_lawyer_profile(db,lawyer)
    return result






@router.get("/{id}")
async def get_lawyer(id: int, db = Depends(get_db)):
    result:Lawyer = lawyerRepo.get_lawyer_by_id(db,id)
    if not result:
        raise HTTPException(
            status_code=404, detail="Lawyer not found"
        )
    return result
