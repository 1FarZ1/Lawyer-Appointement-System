from fastapi import FastAPI,HTTPException,Request,status
from fastapi.responses import JSONResponse
from app.config.database import engine , SessionLocal
import app.models as models
from app.v1.routers import auth, user,lawyer,review,appointement
from starlette.middleware.sessions import SessionMiddleware
from starlette.staticfiles import StaticFiles

models.Base.metadata.create_all(bind=engine)
app = FastAPI()
app.add_middleware(SessionMiddleware, secret_key="!secret")
app.mount("/uploads", StaticFiles(directory="uploads"), name="uploads")
# @app.middleware("http")
# async def auth_middleware(request: Request, call_next):
#     if request.url.path in ["/auth/login", "/auth/login/google", "/auth/redirect", "/auth/register-user"]:
#         response = await call_next(request)
#         return response
#     token = request.headers.get("Authorization")
#     token = token.split(" ")[1] if token else None
#     if token:
#         try:
#             payload = JWT.verify_token(token)
#             request.state.user = payload
#         except:
#             raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid email or password")
#     response = await call_next(request)
#     return response

app.include_router(auth.router)
app.include_router(user.router)
app.include_router(lawyer.router)
app.include_router(review.router)
app.include_router(appointement.router)

@app.get("/")
async def root():
    return JSONResponse({
        "message": "Welcome to FastAPI", 
    })
    




















# @app.middleware("http")
# async def add_logger(request: Request, call_next):
#     response = await custom_logger(request, call_next)
#     return response


@app.middleware("http")
async def apply_auth_middleware(request: Request, call_next):
    if request.url.path.startswith("/users"):
        return await auth_middleware(request, call_next)
    return await call_next(request)




