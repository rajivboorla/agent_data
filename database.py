from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

DATABASE_URL = "postgresql://postgres:password123@localhost:5432/level1"
 
engine = create_engine(DATABASE_URL)

# sessionmaker creates a factory (a class) that can generate database sessions.
# A session = a connection to the database used for CRUD operations.

# “Create a session factory for connecting to the PostgreSQL database.
# Do not auto-commit or auto-flush. Use the engine we defined.”

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine) 

Base = declarative_base()

