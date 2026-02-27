from datetime import datetime, timedelta
from jose import jwt
from database import config

SECRET_KEY = config.get("JWT", "SECRET_KEY", fallback="supersecret")
ALGORITHM = config.get("JWT", "ALGORITHM", fallback="HS256")

ACCESS_TOKEN_EXPIRE_MINUTES = config.getint(
    "JWT", "ACCESS_TOKEN_EXPIRE_MINUTES", fallback=15
)

REFRESH_TOKEN_EXPIRE_MINUTES = config.getint(
    "JWT", "REFRESH_TOKEN_EXPIRE_MINUTES", fallback=10080
)


def create_access_token(data: dict):
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)

    to_encode.update({
        "exp": expire,
        "type": "access"
    })

    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)


def create_refresh_token(data: dict):
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=REFRESH_TOKEN_EXPIRE_MINUTES)

    to_encode.update({
        "exp": expire,
        "type": "refresh"
    })

    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)