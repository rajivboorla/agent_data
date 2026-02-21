from sqlalchemy import Column, Integer, String
from database import Base

class Agent(Base):
    __tablename__ = "t_agents_data"
    __table_args__ = {"schema": "practice"}

    agent_id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    age = Column(Integer, nullable=False)
    city = Column(String(100), nullable=False)
    area = Column(String(100), nullable=False)
    phone = Column(String(15), nullable=True)

    

