from pydantic import BaseModel, ConfigDict


class UserCreate(BaseModel):
    username: str
    password: str
    role: str


class UserLogin(BaseModel):
    username: str
    password: str


class UserResponse(BaseModel):
    """
    👉 Allows Pydantic to read object attributes instead of only dictionaries.
    👉 Required when returning SQLAlchemy models in FastAPI.
    """
    id: int
    username: str
    role: str

    model_config = ConfigDict(from_attributes=True) # Enable ORM mode for SQLAlchemy models
