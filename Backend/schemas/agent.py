from pydantic import BaseModel

class AgentBase(BaseModel):
    name: str
    age: int
    city: str
    area: str
    phone: str | None = None

class AgentCreate(AgentBase):
    agent_id: int

class AgentResponse(AgentBase):
    agent_id: int

    model_config = {"from_attributes": True}  # replaces orm_mode = True
    
    
