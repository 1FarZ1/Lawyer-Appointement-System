
from fastapi import APIRouter
from typing import List



router = APIRouter(
    prefix="/api/appointements",
)


@router.get("/")
async def get_appointements():
    return "reviews"

