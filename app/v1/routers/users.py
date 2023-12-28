from fastapi import APIRouter
from app.models.user import User
from app.config.database import get_db
from app.models.user import User

from typing import List
from fastapi import HTTPException
from app.schemas.user import UserDto

from app.repository.user import UserRepository


db = get_db()

router = APIRouter(
    prefix="/api/users",
)


userRepo = UserRepository(db)


# get All Users
@router.get("/")
async def get_users():
    result:List[User] = userRepo.get_all_users()
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



## how to make username from the body
@router.put("/{id}/username")
async def update_user(id: int,username: str):
    user = userRepo.check_username(username)
    if user:
        raise HTTPException(
            status_code=404, detail="Username already taken"
        )

    result = userRepo.update_username(id, username)
    if not result:
        raise HTTPException(
            status_code=404, detail="User not found"
        )
        
    return result

@router.delete("/{id}")
async def delete_user(id: int):
    result = userRepo.delete_user(id)
    if not result:
        raise HTTPException(
            status_code=404, detail="User not found"
        )
    return {"message":"User deleted successfully"}




