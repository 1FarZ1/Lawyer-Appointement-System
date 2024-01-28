from fastapi import APIRouter, Depends,File, Request,UploadFile
from app.enums import RoleEnum
from app.models import Lawyer, User
from app.config.database import get_db
from app.models import User

from typing import List,Annotated, Optional,Union
from fastapi import HTTPException
from app.schemas import GoogleUserSchema
import datetime


from app.repository import user as userRepository
from app.utils.check_permission import check_permission
from app.utils.utils import Utils





router = APIRouter(
    prefix="/api/users",
    tags=["users"],
    responses={404: {"description": "Not found"}},
    # dependencies=[Depends(auth_middleware)],
    )






@router.get("/")       
async def get_users(
    request: Request,
    page: int = 0, pageSize: int = 100,
    sort: Optional[str] = None,  
    db = Depends(get_db),
):
    # await check_permission(user= request.state.user,permission=[RoleEnum.USER,RoleEnum.LAWYER,RoleEnum.ADMIN])
    result:List[User] = userRepository.get_all_users(
        db,page, pageSize, sort
    )
    return result




@router.get("/lawyer/me")
async def get_lawyer_info(request:Request, db = Depends(get_db)):

    await check_permission(
        user= request.state.user,permission=[RoleEnum.LAWYER]
    )
    id = request.state.user['id']
    result = userRepository.get_user_by_id(id, db)
    # print(result.lawyer)
    if not result:
        raise HTTPException(
            status_code=404, detail="User not found"
        )
    return result



@router.put("/email")
async def update_email(request:Request,email: str , db = Depends(get_db)):
    id = request.state.user['id']
    user = userRepository.get_user_by_email(email, db)
    if user:
        raise HTTPException(
            status_code=404, detail="email already used"
        )

    result = userRepository.update_email(id, email, db)
    if not result:
        raise HTTPException(
            status_code=404, detail="User not found"
        )
        
    return result



@router.post("/uploadfile")
async def create_upload_file(file: Union[UploadFile, None] = None):
    if not file:
        return {"message": "No upload file sent"}
    file_location = f"uploads/{file.filename}"
    with open(file_location, "wb+") as file_object:
        file_object.write(file.file.read())    
    return {"info": f"file '{file.filename}' saved at '{file_location}'"}




@router.put("/image")
async def update_image(request:Request,image: Union[UploadFile, None] = None, db = Depends(get_db)):
    if not image:
        raise HTTPException(
            status_code=404, detail="No image sent"
        )    
    id = request.state.user['id']
    imagePath = Utils.saveFileToUploads(image)['path']
    result = userRepository.update_image(id, imagePath,db)
    if not result:
        raise HTTPException(
            status_code=404, detail="User not found"
        )
        
    return {
        "message":"image updated successfully",
        "imagePath": imagePath
    }





@router.patch('/update-password')
async def update_password(request:Request, password: str, current_password:str, db = Depends(get_db)):
    id = request.state.user['id']
    result = userRepository.update_password(id, password, current_password,db)
    if not result:
        raise HTTPException(
            status_code=404, detail="User not found"
        )
    return {"message":"Password updated successfully"}


@router.delete("/user")
async def delete_user(request:Request, db = Depends(get_db)):
    id = request.state.user['id']
    result = userRepository.delete_user(id, db)
    if not result:
        raise HTTPException(
            status_code=404, detail="User not found"
        )
    return {"message":"User deleted successfully"}




