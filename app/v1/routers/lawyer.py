

from fastapi import APIRouter, Depends, HTTPException, status


def getLawyers(index):
    return {
        "id": index,
        "name": "Ahmed",
        "email": f"ahmed{index}@gmail.com",
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