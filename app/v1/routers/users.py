from fastapi import APIRouter, Depends,File,UploadFile
from app.models.user import User
from app.config.database import get_db
from app.models.user import User

from typing import List,Annotated,Union
from fastapi import HTTPException
from app.schemas.user import UserDto
import datetime


from app.repository import user as userRepo


db = get_db()

router = APIRouter(
    prefix="/api/users",
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
    db = Depends(get_db)
):
    result:List[User] = userRepo.get_all_users(
        db,page, pageSize
    )
    return result




@router.get("/{id}")
async def get_user(id: int):
    result:User = userRepo.get_user_by_id(id)
    print(result)
    if not result:
        raise HTTPException(
            status_code=404, detail="User not found"
        )
    return result



@router.put("/{id}/email")
async def update_email(id: int,email: str):
    user = userRepo.check_email(email)
    if user:
        raise HTTPException(
            status_code=404, detail="email already used"
        )

    result = userRepo.update_username(id, email)
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
async def update_image(id: int,image: Union[UploadFile, None] = None):
    if not image:
        raise HTTPException(
            status_code=404, detail="No image sent"
        )    
    imagePath = saveFileToUploads(image)['path']

    result = userRepo.update_image(id, imagePath)
    if not result:
        raise HTTPException(
            status_code=404, detail="User not found"
        )
        
    return {
        "message":"image updated successfully",
        "imagePath": imagePath
    }


@router.delete("/{id}")
async def delete_user(id: int):
    result = userRepo.delete_user(id)
    if not result:
        raise HTTPException(
            status_code=404, detail="User not found"
        )
    return {"message":"User deleted successfully"}




