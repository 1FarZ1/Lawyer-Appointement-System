
from fastapi import APIRouter,Depends,HTTPException, Request,status
from typing import List
from app.enums import RoleEnum

from app.models import Appointement,Lawyer,User
from app.config.database import get_db
from sqlalchemy.orm import Session
from app.repository import appointement as appointementRepository ,user as userRep ,  lawyer as lawyerRep

from app.schemas import AppointementSchema
from app.utils.check_permission import check_permission
from app.v1.routers.lawyer import ApproveSchema



router = APIRouter(
    prefix="/api/appointements",
    tags=["appointements"],
)




@router.get("/")
async def get_appointements(request:Request ,db: Session = Depends(get_db)):
    check_permission(request.state.user,[

])
    result:List[Appointement] = appointementRepository.get_all_appointements(db)
    return result

@router.get("/")
async def get_lawyer_appointements(request:Request ,db: Session = Depends(get_db)):
    check_permission(request.state.user,[
        RoleEnum.LAWYER
])
    id = request.state.user['id']
    result:List[Appointement] = appointementRepository.get_lawyer_appointements(db,lawyer_id=id)
    return result


@router.get('/')
async def get_user_appointements(request:Request ,db: Session = Depends(get_db)):
#     check_permission(request.state.user,[
#         RoleEnum.USER
# ])
    id = request.state.user['id']
    result:List[Appointement] = appointementRepository.get_user_appointements(db,user_id=id)
    return result



@router.post("/create")
async def create_appointement(request: Request, 
    appointementSchema:AppointementSchema,
                              db: Session = Depends(get_db) ):
        id = request.state.user['id']



        lawyer =  lawyerRep.get_lawyer_by_id(db,appointementSchema.lawyer_id)
        if not lawyer:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Lawyer not found"
            )

        result = appointementRepository.create_appointement(db,appointementSchema,id)
        return result 
  
    

@router.post("/lawyer/respond/")
async def respond_appointement(request: Request, approaveSchema:ApproveSchema , db: Session = Depends(get_db)):
    check_permission(request.state.user,[
        RoleEnum.LAWYER
])
    if not appointementRepository.get_appointement_by_id(db,id):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Appointement not found"
        )
    lawyer_id = request.state.user['id']
    if  not appointementRepository.appointement_belong_to_lawyer(db,approaveSchema.id,lawyer_id=lawyer_id):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="you cant respond to this appointement"
        )

    result = appointementRepository.respond_appointement(db,lawyer_id,approaveSchema.id,"Accepted" if approaveSchema.isApproved else "Rejected")
    return result


