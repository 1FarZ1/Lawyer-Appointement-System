


from typing import Optional
from fastapi import APIRouter, Depends, Request
from pydantic import BaseModel
from app.config.database import get_db

from app.repository import lawyer as lawyerRepo
from utils.check_permission import check_permission
from enums import RoleEnum

router = APIRouter(
    prefix="/api/admin",
    tags=["admin"],
)

class ApproveSchema(BaseModel):
    id: int
    isApproved: bool
    rejection_reason: Optional[str] = None 

## approave lawyer
@router.patch("/lawyer/response")
async def approve_lawyer(request:Request,approaveSchema:ApproveSchema,db=Depends(get_db)):
    check_permission(request.state.user,[
        RoleEnum.ADMIN
])
    result =  await lawyerRepo.changeStatus(db,approaveSchema.id, "Approved" if approaveSchema.isApproved else "Rejected")
    return result






