from fastapi import APIRouter, Depends, HTTPException
from fastapi.responses import JSONResponse
from app.schemas.user import UserDto
from app.models.user import User
from authlib.integrations.starlette_client import OAuth, OAuthError
from starlette.requests import Request
from app.config.database import get_db
from app.repository import user as userRepo,auth as authRepo






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
async def login(UserDto: UserDto, db = Depends(get_db)):
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

@router.post('/register')
async def register(userDto: UserDto, db = Depends(get_db)):
    try :
        isUserExist =   userRepo.check_email(userDto.email,db)
        if (isUserExist) :
            return HTTPException(
                      status_code=401, detail="email already exist"
                  )
        userDto.password = authRepo.hash_password(userDto.password)
        user  =  authRepo.create_user(userDto,db)

        ## jwt token 
        # access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
        # access_token = authRepo.create_access_token(
        #     data={"sub": user.username}, expires_delta=access_token_expires
        # )

        return JSONResponse({
            "message": "User Created",
            "user": user.hashed_password,
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
    