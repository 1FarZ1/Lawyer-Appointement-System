
from fastapi import APIRouter,Depends,HTTPException, Request,status
from typing import List

from app.models import Appointement
from app.config.database import get_db
from sqlalchemy.orm import Session
from app.repository import appointement as appointementRepository

from app.schemas import AppointementSchema



router = APIRouter(
    prefix="/api/appointements",
    tags=["appointements"],
)


@router.get("/")
async def get_appointements(request:Request , db: Session = Depends(get_db)):
    result:List[Appointement] = appointementRepository.get_lawyer_appointements(db,1)
    return result

@router.post("/create")
async def create_appointement(request: Request, 
    appointementSchema:AppointementSchema,
                              db: Session = Depends(get_db) ):
    id = request.state.user['id']

    result = appointementRepository.create_appointement(db,appointementSchema,id)
    return result
    


