


from fastapi import APIRouter


router = APIRouter(
    prefix="/api/admin",
    tags=["admin"],
)


## approave lawyer
@router.get("/lawyer/{id}/approve")
async def approve_lawyer(id:int):
    return []

@router.get("/lawyer/{id}/reject")
async def reject_lawyer(id:int):
    return []
