from sqlalchemy import Column, Integer, String
from database import Base

class User(Base):
    __tablename__ = "t_users_data"
    __table_args__ = {"schema": "practice"}

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    email = Column(String, unique=True, index=True)
    role = Column(String, nullable=False)  # admin / operator