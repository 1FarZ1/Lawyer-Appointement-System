from fastapi import APIRouter, Depends, HTTPException,status
from fastapi.responses import JSONResponse
from app.schemas import LoginSchema, UserSchema
from app.models import User
from authlib.integrations.starlette_client import OAuth, OAuthError
from starlette.requests import Request
from app.config.database import get_db
from app.repository import user as userRepo,auth as authRepo
from app.utils.jwt import JWT






router = APIRouter(
    prefix="/api/auth",
    tags=["auth"],
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


@router.post('/login')
async def login(loginSchema: LoginSchema, db = Depends(get_db)):
    user = userRepo.get_user_by_email(loginSchema.email,db)
    if not user:
        raise HTTPException(
            status_code=401, detail="Incorrect email"
        )
    isMatch  = authRepo.verify_password(loginSchema.password,user.hashed_password)
    if not isMatch: 
        raise HTTPException(
            status_code=401, detail="Incorrect password"
        )
    
    token = JWT.create_token({"id": user.id, "email": user.email})


    return JSONResponse({
        "message": "User Logged In",
        "token:": token,
        "status_code": status.HTTP_200_OK,
    })

@router.post('/register')
async def register(userSchema: UserSchema, db = Depends(get_db)):
    try :
        isUserExist =   userRepo.get_user_by_email(userSchema.email,db)
        if isUserExist :
            return HTTPException(
                      status_code=401, detail="email already exist"
                  )
        userSchema.password = authRepo.hash_password(userSchema.password)
        user  =  authRepo.create_user(userSchema,db)

        token = JWT.create_token({"id": user.id, "email": user.email})

     
        return JSONResponse({
            "message": "User Created",
            "token:": token,
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
    