from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from jose import jwt, JWTError
from database import config
from core.auth import SECRET_KEY, ALGORITHM

security = HTTPBearer()

VALID_TOKEN = config.get("AUTH", "STATIC_TOKEN", fallback=None)

def verify_token(
    credentials: HTTPAuthorizationCredentials = Depends(security),
): # This is the main auth dependency that will be used in protected routes to verify JWT tokens or static tokens contains scheme & token credentials 

    if credentials.scheme != "Bearer":
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid authentication scheme",
        )

    token = credentials.credentials

    # Static token fallback (optional)
    if token == VALID_TOKEN:
        return {
            "sub": "static_user",
            "role": "admin",
            "auth_type": "static"
        }

    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])

        if payload.get("type") != "access":
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid access token",
            )

        return payload

    except JWTError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid or expired token",
        )


def verify_refresh_token(refresh_token: str):

    try:
        payload = jwt.decode(refresh_token, SECRET_KEY, algorithms=[ALGORITHM])

        if payload.get("type") != "refresh":
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid refresh token",
            )

        return payload

    except JWTError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid or expired refresh token",
        )