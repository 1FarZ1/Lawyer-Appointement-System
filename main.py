from fastapi import FastAPI,HTTPException
from passlib.context import CryptContext

from models import User 
import models

from database import engine , SessionLocal
from dto import UserDto



models.Base.metadata.create_all(bind=engine)


db = SessionLocal()

app = FastAPI()

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

@app.get("/")
async def root():
    return {
        "message": "Project Gl Entry Point !"
  }

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

    return {
        "message": "User Logged In",
        "username": isUserExist.username,
        "email": isUserExist.email    
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

## get User By Id
@app.get("/users/{id}")
async def get_user(id: int):
    result:User = db.query(User).filter(User.id == id).first()
    if not result:
        raise HTTPException(
            status_code=404, detail="User not found"
        )
    return result
  




def hash_password(password):
    return pwd_context.hash(password)

def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)