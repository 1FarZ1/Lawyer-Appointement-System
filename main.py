from fastapi import FastAPI,HTTPException,Request
from fastapi.middleware import Middleware
from fastapi.responses import JSONResponse
from models import User 
import models

from database import engine , SessionLocal
from dto import UserDto

from app.utils.hash import hash_password

from typing import List
import logging

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)

from app.v1.routers import auth




async def custom_logger(request: Request, call_next):
    logger.info(f"Request received: {request.method} - {request.url}")
    response = await call_next(request)
    logger.info(f"Response status code: {response.status_code}")
    return response


models.Base.metadata.create_all(bind=engine)
db = SessionLocal()

app = FastAPI()

app.include_router(auth.router)

@app.middleware("http")
async def add_logger(request: Request, call_next):
    response = await custom_logger(request, call_next)
    return response


async def auth_middleware(request: Request, call_next):
    if "Authorization" not in request.headers:
        raise HTTPException(status_code=401, detail="Missing token")

    token = request.headers["Authorization"].replace("Bearer ", "")

    # if token not in fake_users_db:
    #     raise HTTPException(status_code=403, detail="Invalid token")
    
    logger.info(f"Token: {token}")
    response = await call_next(request)
    return response

@app.get("/")
async def root():
    return JSONResponse({
        "message": "Welcome to FastAPI",
      
    })
    

# @app.middleware("http")
# async def apply_auth_middleware(request: Request, call_next):
#     if request.url.path.startswith("/users"):
#         return await auth_middleware(request, call_next)
#     return await call_next(request)





