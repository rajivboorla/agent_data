from fastapi import APIRouter, Request, Depends
from fastapi.responses import RedirectResponse
from sqlalchemy.orm import Session
from database import SessionLocal
from models.user import User
from core.oauth import oauth
from routers.auth import create_access_token, create_refresh_token
from fastapi.responses import RedirectResponse


router = APIRouter(prefix="/auth", tags=["OAuth"])

# DB Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get("/google/login")
async def google_login(request: Request):
    
    redirect_uri = request.url_for("google_callback")
    
    return await oauth.google.authorize_redirect(
        request,
        redirect_uri
    )


# Google OAuth callback endpoint

@router.get("/google/callback")
async def google_callback(request: Request):

    token = await oauth.google.authorize_access_token(request)
    user = token.get("userinfo")

    email = user["email"]
    name = user["name"]
    role = "operator"  # Default role for OAuth users
    
    # create JWT tokens
    access_token = create_access_token({"sub": email, "role": role})
    refresh_token = create_refresh_token({"sub": email, "role": role})

    redirect_url = f"http://localhost:5173/oauth-success?access_token={access_token}&refresh_token={refresh_token}"

    return RedirectResponse(redirect_url)