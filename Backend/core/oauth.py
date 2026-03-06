import os
from authlib.integrations.starlette_client import OAuth
from dotenv import load_dotenv
from database import config
load_dotenv()

oauth = OAuth()

oauth.register(
    name="google",
    # client_id=os.getenv("GOOGLE_CLIENT_ID"),
    # client_secret=os.getenv("GOOGLE_CLIENT_SECRET"),
    client_id=config.get('CORS','client_id'),
    client_secret=config.get('CORS','client_secret'),
    server_metadata_url="https://accounts.google.com/.well-known/openid-configuration",
    client_kwargs={
        "scope": "openid email profile"
    }
)