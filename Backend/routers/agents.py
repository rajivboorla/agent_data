from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from sqlalchemy import asc, desc
from models.agent import Agent
from schemas.agent import AgentCreate, AgentResponse
from database import SessionLocal
from core.rbac import require_roles

router = APIRouter(prefix="/agents", tags=["Agents"])


# DB Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# ✅ GET ALL (Admin + Operator)
@router.get("/", response_model=list[AgentResponse])
def get_agents(
                sort_by: str = Query("agent_id"),
                order: str = Query("asc"),
                limit: int = Query(10),
                offset: int = Query(0),
                current_user: dict = Depends(require_roles(["admin", "operator"])),
                db: Session = Depends(get_db)
           ):

    query = db.query(Agent)

    # Dynamic column sorting
    if hasattr(Agent, sort_by):
        column = getattr(Agent, sort_by)

        if order.lower() == "desc":
            query = query.order_by(desc(column))
        else:
            query = query.order_by(asc(column))

    agents = query.offset(offset).limit(limit).all()

    return agents

# ✅ CREATE (Admin Only)
@router.post("/", response_model=AgentResponse)
def create_agent(
    agent: AgentCreate,
    current_user: dict = Depends(require_roles(["admin"])),
    db: Session = Depends(get_db)
):
    db_agent = Agent(**agent.dict())
    db.add(db_agent)
    db.commit()
    db.refresh(db_agent)
    return db_agent


# ✅ GET ONE (Admin + Operator)
@router.get("/{agent_id}", response_model=AgentResponse)
def get_agent(
    agent_id: int,
    current_user: dict = Depends(require_roles(["admin", "operator"])),
    db: Session = Depends(get_db)
):
    agent = db.query(Agent).filter(Agent.agent_id == agent_id).first()
    if not agent:
        raise HTTPException(status_code=404, detail="Agent not found")
    return agent


# ✅ UPDATE (Admin Only)
@router.put("/{agent_id}", response_model=AgentResponse)
def update_agent(
    agent_id: int,
    updated: AgentCreate,
    current_user: dict = Depends(require_roles(["admin"])),
    db: Session = Depends(get_db)
):
    agent = db.query(Agent).filter(Agent.agent_id == agent_id).first()
    if not agent:
        raise HTTPException(status_code=404, detail="Agent not found")

    for key, value in updated.dict().items():
        setattr(agent, key, value)

    db.commit()
    db.refresh(agent)
    return agent


# ✅ DELETE (Admin Only)
@router.delete("/{agent_id}")
def delete_agent(
    agent_id: int,
    current_user: dict = Depends(require_roles(["admin"])),
    db: Session = Depends(get_db)
):
    agent = db.query(Agent).filter(Agent.agent_id == agent_id).first()
    if not agent:
        raise HTTPException(status_code=404, detail="Agent not found")

    db.delete(agent)
    db.commit()
    return {"message": "Agent deleted successfully"}