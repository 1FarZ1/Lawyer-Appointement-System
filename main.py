from fastapi import FastAPI,HTTPException,Request,status
from fastapi.responses import JSONResponse
from app.config.database import engine , SessionLocal
import app.models as models
from app.utils.jwt import JWT
from app.v1.routers import auth, user,lawyer,review,appointement,location
from starlette.middleware.sessions import SessionMiddleware
from starlette.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware


models.Base.metadata.create_all(bind=engine)
app = FastAPI()
app.add_middleware(SessionMiddleware, secret_key="!itsasecret")
origins = [
    "*",
    "http://192.168.43.176:8001/",
    ##"http://127.0.0.1:5500/",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["POST", "GET", "PUT","PATCH","DELETE","OPTIONS"],
    allow_headers=["*"],

)



app.mount("/uploads", StaticFiles(directory="uploads"), name="uploads")


non_authenticated_routes = [
    "/","/docs",'/openapi.json',
    "/api/lawyers/user",    
    "/api/lawyers/pending",
    "/api/lawyers/categories",
    "/api/lawyers/highest_rated",
    
]
@app.middleware("http")
async def auth_middleware(request: Request, call_next):
    print(request.url.path)
    if request.url.path in non_authenticated_routes or request.url.path.startswith(
        (
            "/api/location/",
            "/api/auth/",
            "/uploads/",
            "/api/lawyers/lawyer",
            "/api/reviews/",

        )
    ) :
        response = await call_next(request)
        return response
    token = request.headers.get("Authorization")
    print(token)
    token = token.split(" ")[1] if token else None
    if token:
        try:
            payload = JWT.verify_token(token)
            request.state.user = payload
        except:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid email or password")
    else:
        return JSONResponse({
            "message": "Unauthorized",
            "status_code": 401,
        }, status_code=status.HTTP_401_UNAUTHORIZED)
    response = await call_next(request)
    return response

app.include_router(auth.router)
app.include_router(user.router)
app.include_router(lawyer.router)
app.include_router(review.router)
app.include_router(appointement.router)
app.include_router(location.router)

@app.get("/")
async def root():
    return JSONResponse({
        "message": "Welcome to FastAPI", 
    })
    





















# @app.middleware("http")
# async def add_logger(request: Request, call_next):
#     response = await custom_logger(request, call_next)
#     return response


# @app.middleware("http")
# async def apply_auth_middleware(request: Request, call_next):
#     if request.url.path.startswith("/users"):
#         return await auth_middleware(request, call_next)
#     return await call_next(request)




