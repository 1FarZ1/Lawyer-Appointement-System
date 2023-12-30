from fastapi import APIRouter, Depends,File,UploadFile
from app.models import User
from app.config.database import get_db
from app.models import User

from typing import List,Annotated, Optional,Union
from fastapi import HTTPException
from app.schemas import UserSchema
import datetime


from app.repository import user as userRepository
    # from main import auth_middleware





router = APIRouter(
    prefix="/api/users",
    tags=["users"],
    responses={404: {"description": "Not found"}},
    # dependencies=[Depends(auth_middleware)],
    )

def saveFileToUploads(image) -> dict:
    import os
    basePath = "uploads/" +  datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S").replace(" ", "_").replace(":", "-").replace(".", "-")
    imagePath = (f"{basePath}/{image.filename}")
    if not os.path.exists(basePath):
        os.makedirs(basePath)    
    with open(imagePath, "wb+") as file_object:
        file_object.write(image.file.read())    
    return {
        "info": f"file '{image.filename}' saved at '{imagePath}'",
        "path": imagePath
    }


@router.get("/")    
async def get_users(
    page: int = 0, pageSize: int = 100,
    sort: Optional[str] = None,  
    db = Depends(get_db),
):
    result:List[User] = userRepository.get_all_users(
        db,page, pageSize
    )
    return result




@router.get("/{id}")
async def get_user(id: int, db = Depends(get_db)):
    result:User = userRepository.get_user_by_id(id, db)
    if not result:
        raise HTTPException(
            status_code=404, detail="User not found"
        )
    return result



@router.put("/{id}/email")
async def update_email(id: int,email: str , db = Depends(get_db)):
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




@router.put("/{id}/image")
async def update_image(id: int,image: Union[UploadFile, None] = None, db = Depends(get_db)):
    if not image:
        raise HTTPException(
            status_code=404, detail="No image sent"
        )    
    imagePath = saveFileToUploads(image)['path']

    result = userRepository.update_image(id, imagePath,db)
    if not result:
        raise HTTPException(
            status_code=404, detail="User not found"
        )
        
    return {
        "message":"image updated successfully",
        "imagePath": imagePath
    }


@router.delete("/{id}")
async def delete_user(id: int, db = Depends(get_db)):
    result = userRepository.delete_user(id, db)
    if not result:
        raise HTTPException(
            status_code=404, detail="User not found"
        )
    return {"message":"User deleted successfully"}




