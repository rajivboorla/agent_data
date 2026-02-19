from database import config
import uvicorn
from fastapi import FastAPI, Depends, HTTPException
from loguru import logger
from sqlalchemy.orm import Session
from jose import jwt, JWTError
from database import SessionLocal, engine
from models import Base, Agent
from schemas import AgentCreate, AgentResponse
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from fastapi import status
from auth import ALGORITHM, create_access_token, create_refresh_token, SECRET_KEY
from loguru import logger

app = FastAPI()
security = HTTPBearer()

# Ideally fetch this from DB / ENV / JWT

VALID_TOKEN = config.get('TOKEN','AUTH_TOKEN')

# def verify_token(credentials: HTTPAuthorizationCredentials = Depends(security)):
#     # logger.info(f"Received token: {credentials.credentials}")
#     if credentials.scheme != "Bearer":
#         raise HTTPException(
#             status_code=status.HTTP_401_UNAUTHORIZED,
#             detail="Invalid authentication scheme"
#         )

#     if credentials.credentials != VALID_TOKEN:
#         raise HTTPException(
#             status_code=status.HTTP_401_UNAUTHORIZED,
#             detail="Invalid or expired token"
#         )

#     return credentials.credentials

def verify_token(credentials: HTTPAuthorizationCredentials = Depends(security)):

    if credentials.scheme != "Bearer":
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid authentication scheme"
        )

    token = credentials.credentials

    # ✅ 1. Allow old static token
    if token == VALID_TOKEN:
        return {"auth_type": "static"}

    # ✅ 2. Try JWT validation
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        logger.info(f"Decoded JWT payload: {payload}")
        if payload.get("type") != "access":
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid access token"
            )

        return payload

    except JWTError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid or expired token"
        )


# Create tables if not present
Base.metadata.create_all(bind=engine)

# Dependency
def get_db():
    """
    Yield a database session.
    Create a new database session for a request and close it after the request is done
    this prevents memory leaks and ensures that connection errors.
    """ 
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/login")
def login():
    user_data = {"sub": "agent_user"}

    access_token = create_access_token(user_data)
    refresh_token = create_refresh_token(user_data)

    return {
        "access_token": access_token,
        "refresh_token": refresh_token,
        "token_type": "bearer"
    }


@app.post("/refresh")
def refresh_token(refresh_token: str):
    try:
        payload = jwt.decode(refresh_token, SECRET_KEY, algorithms=[ALGORITHM])

        if payload.get("type") != "refresh":
            raise HTTPException(status_code=401, detail="Invalid refresh token")

        new_access_token = create_access_token({"sub": payload["sub"]})

        return {
            "access_token": new_access_token,
            "token_type": "bearer"
        }

    except JWTError:
        raise HTTPException(status_code=401, detail="Invalid or expired refresh token")



@app.post("/agents", response_model=AgentResponse)
def create_agent(agent: AgentCreate, token: str = Depends(verify_token), db: Session = Depends(get_db)):
    db_agent = Agent(**agent.dict())
    db.add(db_agent)
    db.commit()
    db.refresh(db_agent)
    return db_agent


@app.get("/agents", response_model=list[AgentResponse])
def get_agents(token: str = Depends(verify_token), db: Session = Depends(get_db)):
    return db.query(Agent).all()


@app.get("/agents/{agent_id}", response_model=AgentResponse)
def get_agent(agent_id: int, db: Session = Depends(get_db)):
    agent = db.query(Agent).filter(Agent.agent_id == agent_id).first()
    if not agent:
        raise HTTPException(status_code=404, detail="Agent not found")
    return agent


@app.put("/agents/{agent_id}", response_model=AgentResponse)
def update_agent(agent_id: int, updated: AgentCreate, db: Session = Depends(get_db)):
    agent = db.query(Agent).filter(Agent.agent_id == agent_id).first()
    if not agent:
        raise HTTPException(status_code=404, detail="Agent not found")

    for key, value in updated.dict().items():
        setattr(agent, key, value)

    db.commit()
    db.refresh(agent)
    return agent


@app.delete("/agents/{agent_id}")
def delete_agent(agent_id: int, db: Session = Depends(get_db)):
    agent = db.query(Agent).filter(Agent.agent_id == agent_id).first()
    if not agent:
        raise HTTPException(status_code=404, detail="Agent not found")

    db.delete(agent)
    db.commit()
    return {"message": "Agent deleted successfully"}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
