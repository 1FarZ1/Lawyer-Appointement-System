from fastapi import HTTPException

from app.enums import RoleEnum


async def check_permission(user, permission:list(RoleEnum)):
    print(user['role'])
    if user["role"] not in permission:
        raise HTTPException(status_code=401, detail="Unauthorized")
    
    return True