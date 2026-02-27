from fastapi import FastAPI
from routers import agents, auth, users
import uvicorn
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="RBAC FastAPI App")

# ✅ Include all routers
app.include_router(auth.router)     # <-- you missed this
app.include_router(users.router)
app.include_router(agents.router)

# ✅ CORS
origins = [
    "http://localhost:5173",  # React frontend
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