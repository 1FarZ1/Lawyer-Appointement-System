

from fastapi import APIRouter, Depends, HTTPException, status


def getLawyers(index):
    return {
        "id": index,
        "name": "Fares",
        "email": f"Fares{index}@gmail.com",
        "rating": index % 5 + 0.5,
        "reviews": index % 10000,
        }


db_lawyers = [ getLawyers(i) for i in range(100)]


router = APIRouter(
    prefix="/api/lawyers",
    # tags=["lawyers"],
    # dependencies=[Depends(get_token_header)],
    responses={404: {"description": "Not found"}},
)



@router.get("/")
async def get_lawyers(
    page: int = 0, pageSize: int = 10,
):
    return db_lawyers[page * pageSize : (page + 1) * pageSize]

@router.get("/{id}")
async def get_lawyer(id: int):
    if id < 0 or id >= len(db_lawyers):
        raise HTTPException(
            status_code=404, detail="invalid id"
        )
    lawyer = db_lawyers[id]
    if not lawyer:
        raise HTTPException(
            status_code=404, detail="lawyer not found"
        )
    return lawyer     

   