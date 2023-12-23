import logging

from fastapi import Request

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)

async def custom_logger(request: Request, call_next):
    logger.info(f"Request received: {request.method} - {request.url}")
    response = await call_next(request)
    logger.info(f"Response status code: {response.status_code}")
    return response