import secrets
from urllib.parse import urlencode
from fastapi import APIRouter, Depends, File, HTTPException, UploadFile,status
from fastapi.responses import JSONResponse
from pydantic import BaseModel
import requests
from app.enums import RoleEnum, StatusEnum
from app.schemas import CheckEmailSchema, LawyerUserSchemaForm, LoginSchema, GoogleUserSchema,LawyerUserSchema,LUserSchema,LawyerInfoSchema
from app.models import User
from authlib.integrations.starlette_client import OAuth, OAuthError  
from starlette.requests import Request
from app.config.database import SessionLocal, get_db
from app.repository import user as userRepo,auth as authRepo, lawyer as lawyerRepo
from app.utils.jwt import JWT
from app.utils.utils import Utils








router = APIRouter(
    prefix="/api/auth",
    tags=["auth"],
)

GOOGLE_CLIENT_ID = '532245387058-56rmhp2p0bfbv628s8n1plvm71oeg5lt.apps.googleusercontent.com'
GOOGLE_CLIENT_SECRET = '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'
GOOGLE_REDIRECT_URL = 'http://localhost:8000/api/auth/google-auth-callback'



oauth = OAuth()
oauth.register(
    name='google',
    client_id=GOOGLE_CLIENT_ID,
    client_secret=GOOGLE_CLIENT_SECRET,
    server_metadata_url='https://accounts.google.com/.well-known/openid-configuration',
    client_kwargs={
        'scope': 'openid email profile',
    },
    
)


@router.post('/login')
async def login(loginSchema: LoginSchema, db = Depends(get_db)):
    print(loginSchema)
    user = userRepo.get_user_by_email(loginSchema.email,db)
    if not user:
        raise HTTPException(
            status_code=401, detail="User With this credentials does not exist "
        )

    if user.role != "lawyer":
        raise HTTPException(
            status_code=401, detail="you need to login with google"
        )
    isMatch  = authRepo.verify_password(loginSchema.password,user.password)
    if not isMatch: 
        raise HTTPException(
            status_code=401, detail="Incorrect password"
        )
    lawyer =  lawyerRepo.get_lawyer_by_user(db,user.id)
    print(lawyer.status)
    if lawyer.status == StatusEnum.PENDING:
            raise HTTPException(
                status_code=401, detail="your account waiting for approvatation"
            )   



    token = JWT.create_token({"id": user.id, "email": user.email , "role": user.role})
    return JSONResponse({
        "message": "lawyer  Logged In Successfully",
        "token": token,
        "status_code": status.HTTP_200_OK,
    })









## function to cast array of numbers  to chosen type
def cast_array(array,type):
    return list(map(type,array))





@router.post('/register-lawyer')
async def register(lawyerSchema: LawyerUserSchemaForm = Depends() ,
                   
                     certificat: UploadFile = File(...), 
                   db = Depends(get_db)):
    # try:
        
        cast_array(
             [
                lawyerSchema.wilaya_id,
                lawyerSchema.city_id,
                lawyerSchema.categorie_id,
             ]
             ,
                int 
        )

        cast_array(
             [
                lawyerSchema.longitude,
                lawyerSchema.latitude,
             ],
                float   
        )

        # ## trim all the fields with  a loop
        # for field in lawyerSchema.__fields_set__:
        #     lawyerSchema[field] = lawyerSchema[field].strip()

        isUserExist =   userRepo.get_user_by_email(lawyerSchema.email,db)   
        if isUserExist :
            raise HTTPException(
                      status_code=401, detail="email already exist"
                  )
        
        lawyerSchema.password = authRepo.hash_password(lawyerSchema.password)

        lUserSchema = LUserSchema(
            email=lawyerSchema.email,
            fname=lawyerSchema.fname,
            lname=lawyerSchema.lname,
            password=lawyerSchema.password,
        )
    
        user = authRepo.register_user(lUserSchema,db,role=RoleEnum.LAWYER)


        path =  Utils.saveFileToUploads(certificat)['path']
        lawyerInfo = LawyerInfoSchema(
            phone = lawyerSchema.phone,
            address = lawyerSchema.address,
            description = lawyerSchema.description,
            social = lawyerSchema.social,
            certificat_url=path,
            wilaya_id =  lawyerSchema.wilaya_id,
            city_id = lawyerSchema.city_id,
            longitude = lawyerSchema.longitude,
            latitude = lawyerSchema.latitude,
            categorie_id = lawyerSchema.categorie_id,
        )
        lawyer = lawyerRepo.create_new_lawyer(db,lawyerInfo,user.id)
        
        token = JWT.create_token({"id": user.id, "email": user.email,
                                  "role": user.role})

        return JSONResponse({
            "message": "User Created",
            "token:": token,
            "status_code": 201,
        })
    # except Exception as e:
    #      return JSONResponse({
    #        "message": "something went wrong",
    #        "status_code": 500,
    #           "error": str(e),
    #      })






@router.post('/check-email')
async def check_email(chekEmailSchema: CheckEmailSchema, db = Depends(get_db)):

    ## check if it has email schema




    user = userRepo.get_user_by_email(chekEmailSchema.email,db)
    if not user:
        return JSONResponse({
            "message": "email not exist",
            "status_code": 200,
        })
    return JSONResponse({
        "message": "email already exist",
        "status_code": 401,
    })

















@router.get("/google-auth")
async def login_google():
    return {
        "url": f"https://accounts.google.com/o/oauth2/auth?response_type=code&client_id={GOOGLE_CLIENT_ID}&redirect_uri={GOOGLE_REDIRECT_URL}&scope=openid%20profile%20email&access_type=offline"
    }

@router.get("/google-auth-callback")
async def auth_google(code: str, db: SessionLocal = Depends(get_db)):
    token_url = "https://accounts.google.com/o/oauth2/token"
    data = {
        "code": code,
        "client_id": GOOGLE_CLIENT_ID,
        "client_secret": GOOGLE_CLIENT_SECRET,
        "redirect_uri": GOOGLE_REDIRECT_URL,
        "grant_type": "authorization_code",
    }
    response = requests.post(token_url, data=data)
    access_token = response.json().get("access_token")
    user_info = requests.get("https://www.googleapis.com/oauth2/v1/userinfo", headers={"Authorization": f"Bearer {access_token}"})
    user_info = user_info.json()
    # create user if not exists
    # userExists = user.get_by_email(db, user_info["email"])
    # if not userExists:
    #     newUser = user.create(db, UserRegisterSchema(email=user_info["email"], nom=user_info["family_name"], prenom=user_info["given_name"]))
    #     token = JWT.create_token({"id": newUser.id, "email": newUser.email, "role": f"{newUser.role}"})
    #     return {"token": token}
    # token = JWT.create_token({"id": userExists.id, "email": userExists.email, "role": f"{userExists.role}"})
    # return RedirectResponse(f"http://localhost:5173/login?token={token}")

    return user_info


@router.get("/google-auth")
async def google_auth(request: Request):
    # state = secrets.token_urlsafe(16)
    # params = {
    #     "response_type": "code",
    #     "client_id": GOOGLE_CLIENT_ID,
    #     "redirect_uri": GOOGLE_REDIRECT_URL,
    #     "scope": "openid https://www.googleapis.com/auth/userinfo.profile https://www.googleapis.com/auth/userinfo.email",
    #     "state": state,
    #     "access_type": "offline"
    # }

    # auth_url = f"https://accounts.google.com/o/oauth2/auth?{urlencode(params)}"

    return await oauth.google.authorize_redirect(request, GOOGLE_REDIRECT_URL)


@router.get("/google-auth-callback")
async def google_auth_callback(request: Request,db=Depends(get_db)):
    try : 
        token = await oauth.google.authorize_access_token(request)
        googleUser:dict = token['userinfo']
        email = googleUser['email']
        user = userRepo.get_user_by_email(db=db,email=email)           
        if user:
            token = JWT.create_token({"id": user.id, "email": user.email,
                                  "role": user.role})
            return JSONResponse({
            "message": "Welcome to FastAPI from google login ",
            "token:": token,
                    "status_code": status.HTTP_200_OK, })
        

        fname = googleUser['given_name']        
        lname = googleUser['family_name'] if googleUser.get('family_name') else googleUser['name']
        
        userSchema = GoogleUserSchema(
                email=email,
                fname=fname,
                lname=lname,
            )
        user = authRepo.register_user(userSchema,db)
        token = JWT.create_token({"id": user.id, "email": user.email,
                                  "role": user.role})

        return JSONResponse({
        "message": "Welcome to FastAPI from google register",
        "token:": token,
                "status_code": status.HTTP_200_OK,
             })
    except (OAuthError) as e:
        return JSONResponse({
            "message": "something went wrong",
            "status_code": 500,
            "error": str(e),
        })    
    