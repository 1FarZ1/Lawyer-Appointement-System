from fastapi import APIRouter
from fastapi.responses import JSONResponse
from fastapi import HTTPException
# from fastapi import Request
from app.schemas.user import UserDto
from app.models.user import User
from authlib.integrations.starlette_client import OAuth, OAuthError
from fastapi.middleware import Middleware
from starlette.requests import Request
from starlette.middleware.sessions import SessionMiddleware






router = APIRouter(
    prefix="/api/auth",
)



oauth = OAuth()
oauth.register(
    name='google',
    client_id='532245387058-56rmhp2p0bfbv628s8n1plvm71oeg5lt.apps.googleusercontent.com',
    client_secret='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',
    server_metadata_url='https://accounts.google.com/.well-known/openid-configuration',
    client_kwargs={
        'scope': 'openid email profile',
    },
    
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




@router.get("/google-auth")
async def google_auth(request: Request):
    redirect_uri = request.url_for('google-auth-callback')
    return await oauth.google.authorize_redirect(request, redirect_uri)


@router.get("/google-auth-callback")
async def root(request: Request):
    try : 
        token = await oauth.google.authorize_access_token(request)
        return JSONResponse({
        "message": "Welcome to FastAPI from google",
        "token": token
      
             })
    except (OAuthError) as e:
        return JSONResponse({
            "message": "something went wrong",
            "status_code": 500,
            "error": str(e),
        })
    