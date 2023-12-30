from fastapi import HTTPException

from app.enums import RoleEnum


def check_permission(user, permission:list(RoleEnum)):
    if user["role"] not in permission:
        raise HTTPException(status_code=401, detail="Unauthorized")
    
    return True