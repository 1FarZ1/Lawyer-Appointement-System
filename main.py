from fastapi import FastAPI
from passlib.context import CryptContext

from models import User 
import models

from pydantic import BaseModel
from database import engine , SessionLocal

models.Base.metadata.create_all(bind=engine)


db = SessionLocal()
class UserDto(BaseModel):
    username: str
    password: str

app = FastAPI()
## hasher
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


fake_Users_db = [
        User(
            username="user1",
            email= "user1@gmail.com",
            hashed_password= "@user1"
        )
        ,
        User(
            username="user2",
            email= "user2@gmail.com",
            hashed_password= "@user2"),
]

## Entry Point
@app.get("/")
async def root():
    return {
        "message": "Hel!"
  }

## Login User
@app.post('/api/auth/login')
async def login(UserDto: UserDto):
    isUserExist = None
    for user in fake_Users_db:
        if user.username == UserDto.username:
            isUserExist = user
            break
    if not isUserExist:
        return {"error": "Invalid User"}

    isPasswordCorrect = pwd_context.verify(UserDto.password, isUserExist.hashed_password)  
    if not isPasswordCorrect:
        return {"error": "Invalid Password"}

    return {
        "message": "User Logged In",
        "username": isUserExist.username,
        "email": isUserExist.email,
        
    }





## Register User
@app.post('/api/auth/register')
async def register(UserDto: UserDto):
    password  = pwd_context.hash(UserDto.password)
    # fake_Users_db.append(User(
    #     username=UserDto.username,
    #     email=UserDto.username,
    #     hashed_password=password
    # ))
    ## verify if user already exist in database sql
    # isUserExist = db.query(User).filter(User.username == UserDto.username).first()
    
    
    
    newUser = User(
        username=UserDto.username,
        email=UserDto.username,
        hashed_password=password
    )
    db.add(newUser)
    db.commit()
    
    return  {
        "message": "User Created",
        "status": 201,
    }



## get All Users
@app.get("/users")
async def get_users():
    result = db.query(User).all() 
    return result
