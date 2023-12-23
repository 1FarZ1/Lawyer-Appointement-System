from fastapi import APIRouter
from fastapi.responses import JSONResponse
from fastapi import HTTPException
from fastapi import Request
from dto import UserDto



router = APIRouter(
    prefix="/api/auth",
)





##TODO:fix this 
@router.post('/login')
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
@router.post('/register')
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

@router.post("/google-auth")
async def google_auth():
    return JSONResponse({
        "message": "Auth Google",
        "status_code": 200,
    })

