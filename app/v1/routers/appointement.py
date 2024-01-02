
from fastapi import APIRouter,Depends,HTTPException, Request,status
from typing import List

from app.models import Appointement,Lawyer,User
from app.config.database import get_db
from sqlalchemy.orm import Session
from app.repository import appointement as appointementRepository ,user as userRep ,  lawyer as lawyerRep

from app.schemas import AppointementSchema



router = APIRouter(
    prefix="/api/appointements",
    tags=["appointements"],
)


@router.get("/")
async def get_appointements(request:Request ,db: Session = Depends(get_db)):
    id = request.state.user['id']
    lawyer:Lawyer =   db.query(Lawyer).filter(Lawyer.user_id == id).first()
#    lawyer_user:User = lawyer.user
    result:List[Appointement] = appointementRepository.get_lawyer_appointements(db,lawyer_id=lawyer.id)
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
  
    

@router.get("/lawyer/accept/{id}")
async def accept_appointement(request: Request, id , db: Session = Depends(get_db)):
    if not appointementRepository.get_appointement_by_id(db,id):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Appointement not found"
        )

    result = appointementRepository.accept_appointement(db,id)
    return result

@router.get("/lawyer/reject/{id}")
async def reject_appointement(request: Request, id , db: Session = Depends(get_db)):
    if not appointementRepository.get_appointement_by_id(db,id):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Appointement not found"
        )
    result = appointementRepository.reject_appointement(db,id)
    return result


