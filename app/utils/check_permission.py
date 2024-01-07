from fastapi import HTTPException

from app.enums import RoleEnum


async def check_permission(user, permission:list(RoleEnum)):
    if user["role"] not in permission:
        raise HTTPException(status_code=401, detail="you dont have this permission")
    
    return True