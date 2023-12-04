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

async def custom_logger(request: Request, call_next):
    logger.info(f"Request received: {request.method} - {request.url}")
    response = await call_next(request)
    logger.info(f"Response status code: {response.status_code}")
    return response


models.Base.metadata.create_all(bind=engine)
db = SessionLocal()

app = FastAPI()

@app.middleware("http")
async def add_logger(request: Request, call_next):
    response = await custom_logger(request, call_next)
    return response

@app.get("/")
async def root():
    return JSONResponse({
        "message": "Welcome to FastAPI",
      
    })
    

async def auth_middleware(request: Request, call_next):
    if "Authorization" not in request.headers:
        raise HTTPException(status_code=401, detail="Missing token")

    token = request.headers["Authorization"].replace("Bearer ", "")

    # if token not in fake_users_db:
    #     raise HTTPException(status_code=403, detail="Invalid token")
    
    logger.info(f"Token: {token}")
    response = await call_next(request)
    return response


@app.middleware("http")
async def apply_auth_middleware(request: Request, call_next):
    if request.url.path.startswith("/users"):
        return await auth_middleware(request, call_next)
    return await call_next(request)

@app.post('/api/auth/login')
async def login(UserDto: UserDto):
    isUserExist = db.query(User).filter(User.username == UserDto.username).first()
    if not isUserExist:
        raise HTTPException(
            status_code=401, detail="Incorrect username"
        )
    # isPasswordCorrect = pwd_context.verify(UserDto.password, isUserExist.hashed_password)
    isPasswordCorrect = UserDto.password == isUserExist.hashed_password
    if not isPasswordCorrect:
        raise HTTPException(
            status_code=401, detail="Incorrect password"
        )

    return JSONResponse({
        "message": "User Logged In",
        "email": isUserExist.email,
        "username": isUserExist.username,
        "status_code": 200,
    })

## Register User
@app.post('/api/auth/register')
async def register(UserDto: UserDto):
   try :
       user = User(
           username=UserDto.username,
           email=UserDto.username,
           hashed_password=UserDto.password)
       db.add(user)
       db.commit()
       db.refresh(user)
       return JSONResponse({
           "message": "User Created",
           "email": user.email,
           "username": user.username,
           "status_code": 201,
       })
   except Exception as e:
         return JSONResponse({
           "message": "something went wrong",
           "status_code": 500,
              "error": str(e),
         })

## get All Users
@app.get("/users")
async def get_users():
    result:List[User] = db.query(User).all() 
    return result

@app.get("/users/{id}")
async def get_user(id: int):
    result:User = db.query(User).filter(User.id == id).first()
    if not result:
        raise HTTPException(
            status_code=404, detail="User not found"
        )
    return result
  



