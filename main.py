from fastapi import FastAPI,HTTPException,Request
from fastapi.middleware import Middleware
from fastapi.responses import JSONResponse
from app.config.database import engine , SessionLocal
import app.models.user as models
from app.v1.routers import auth,users,lawyer
from app.utils.logger import logger,custom_logger
from starlette.middleware.sessions import SessionMiddleware
from starlette.staticfiles import StaticFiles

models.Base.metadata.create_all(bind=engine)
app = FastAPI()
app.add_middleware(SessionMiddleware, secret_key="!secret")
app.mount("/uploads", StaticFiles(directory="uploads"), name="uploads")

app.include_router(auth.router)
app.include_router(users.router)
app.include_router(lawyer.router)

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




