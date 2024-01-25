from fastapi import APIRouter
import json


router = APIRouter(
    prefix="/api/location",
    tags=["location"],
)


@router.get('/wilaya')
async def get_wilaya():
    with open('app/data/wilayas.json',encoding="utf8") as json_file:
        data = json.load(json_file)
        return data
    

@router.get('/cities/{id}')
async def get_cities(id:int):
    with open('app/data/cities.json',encoding="utf8") as json_file:
        data = json.load(json_file)
        return list(filter(
            lambda x: x['wilaya_id'] == str(id),
            data
        ))