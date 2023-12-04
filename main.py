from fastapi import FastAPI
from passlib.context import CryptContext

from models import User

from pydantic import BaseModel
from database import engine


class UserDto(BaseModel):
    username: str
    password: str

# from database import Base, engine

app = FastAPI()


# Base.metadata.create_all(bind=engine)


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
async def index():
    # result = engine.execute("select * from Users")
    # for row in result:
    #     print(row)
    return {
        "message": "Hello, world!"
  }


@app.get




## Login User
@app.post('/api/auth/login')
async def login(UserDto: UserDto):
    ## check if user exist in our fake users db
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
    fake_Users_db.append(User(
        username=UserDto.username,
        email=UserDto.username,
        hashed_password=password
    ))
    return  {
        "message": "User Created",
        "User": fake_Users_db[-1]
    }



## get All Users
@app.get("/users")
async def get_users():
    result = engine.execute("select * from Users")
    for row in result:
        print(row)
    return fake_Users_db



### Item API
# @app.post("/items/")
# async def create_item(item: Item):
#     return item
# @app.get("/api/sum")
# async def sum(a: int, b: int):
#     return {
#         "result": a + b
#     }
## give me a fucntion to inverse a string 
# def inverse_string(string):
#     return string[::-1]


# @app.get("/api/inverse")
# async def inverse(string: str):
#     return inverse_string(string)
