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

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

## Entry Point
@app.get("/")
async def root():
    return {
        "message": "Hello world!"
  }

## Login User
@app.post('/api/auth/login')
async def login(UserDto: UserDto):
    isUserExist = db.query(User).filter(User.username == UserDto.username).first()
    if not isUserExist:
        return {"error": "Invalid User"}
    
    # isPasswordCorrect = pwd_context.verify(UserDto.password, isUserExist.hashed_password)
    isPasswordCorrect = UserDto.password == isUserExist.hashed_password
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
   try :
       user = User(
           username=UserDto.username,
           email=UserDto.username,
           hashed_password=UserDto.password)
       db.add(user)
       db.commit()
       db.refresh(user)
       return {
           "message": "User Created",
           "username": user.username,
           "email": user.email,
           
       }
   except Exception as e:
         return {"error": str(e)}



## get All Users
@app.get("/users")
async def get_users():
    result:List[User] = db.query(User).all() 
    return result





def hash_password(password):
    return pwd_context.hash(password)

def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)