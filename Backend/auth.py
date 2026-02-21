from datetime import datetime, timedelta
from jose import jwt, JWTError
from database import config
from loguru import logger

SECRET_KEY = config.get("SECRET_KEY", "supersecret")
ALGORITHM = config.get("SECRET_KEY", "algorithm")

ACCESS_TOKEN_EXPIRE_MINUTES = 1
# REFRESH_TOKEN_EXPIRE_DAYS = 1
REFRESH_TOKEN_EXPIRE_MINUTES = 1

def create_access_token(data: dict):
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire, "type": "access"})
    logger.info(f"Creating access token with data: {to_encode}")

    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)


def create_refresh_token(data: dict):
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=REFRESH_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire, "type": "refresh"})
    logger.info(f"Creating refresh token with data: {to_encode}")

    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

