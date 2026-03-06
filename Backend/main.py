from fastapi import FastAPI
from routers import agents, users, auth, oauth
from database import config
import uvicorn
from fastapi.middleware.cors import CORSMiddleware
from starlette.middleware.sessions import SessionMiddleware # 


app = FastAPI(title="RBAC FastAPI App")

app.add_middleware(
    SessionMiddleware,
    secret_key="super-secret-key"  # change this in production
)

# ✅ Include all routers
app.include_router(auth.router)     # Include auth router first to ensure /auth routes are registered before others
app.include_router(oauth.router)    # Include OAuth router to ensure OAuth routes are registered
app.include_router(users.router)    # Include users router after auth to ensure it can use auth dependencies
app.include_router(agents.router)   # Include agents router last to ensure it can use auth and user dependencies

# ✅ CORS
origins = [
    config.get("CORS", "ORIGIN", fallback="http://localhost:5173"),  # React frontend
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ✅ Run
if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)