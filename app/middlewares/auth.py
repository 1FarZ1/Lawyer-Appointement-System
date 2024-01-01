# from fastapi import Request, HTTPException
# from app.utils.logger import logger

# async def auth_middleware(request: Request, call_next):
#     if "Authorization" not in request.headers:
#         raise HTTPException(status_code=401, detail="Missing token")

#     token = request.headers["Authorization"].replace("Bearer ", "")

#     ##TODO:check db if token is valid and user is active
#     # user = db.query(User).filter(User.token == token).first()
#     logger.info(f"Token: {token}")
#     response = await call_next(request)
#     return response
