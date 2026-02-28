from pydantic import BaseModel, ConfigDict

class AgentBase(BaseModel):
    name: str
    age: int
    city: str
    area: str
    phone: str | None = None

class AgentCreate(AgentBase):
    agent_id: int

class AgentResponse(AgentBase):
    """
    👉 Allows Pydantic to read object attributes instead of only dictionaries.
    👉 Required when returning SQLAlchemy models in FastAPI.
    """

    agent_id: int

    model_config = ConfigDict(from_attributes=True)  # replaces orm_mode = True
    
    
