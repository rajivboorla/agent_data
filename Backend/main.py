from fastapi import FastAPI
from routers import agents, users, auth
from database import config
import uvicorn
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="RBAC FastAPI App")

# ✅ Include all routers
app.include_router(auth.router)     # Include auth router first to ensure /auth routes are registered before others
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