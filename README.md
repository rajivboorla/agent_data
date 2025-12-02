# agent_data
about all agents data

this is all about getting & storing the agent's data

- ------------ for db table creation  in postgresql 

CREATE DATABASE level1;

CREATE SCHEMA practice;

CREATE TABLE t_agents_data (
    agent_id INT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    age INT NOT NULL,
    city VARCHAR(100) NOT NULL,
    area VARCHAR(100) NOT NULL
);

if autoincrement needed 

adding unique constraint on name (optional)

ALTER TABLE practice.t_agents_data
ADD CONSTRAINT unique_agent_name UNIQUE (name);

- -------------- for example

INSERT INTO practice.t_agents_data (name, age, city, area)
VALUES 
('Rajiv', 28, 'Hyderabad', 'Madhapur'),
('Amit', 32, 'Bangalore', 'HSR Layout'),
('Sneha', 25, 'Chennai', 'Velachery');

SELECT * FROM agents;

- ---------------- FastAPI CRUD connected to PostgreSQL ------------

pip install fastapi uvicorn sqlalchemy psycopg2

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

DATABASE_URL = "postgresql://postgres:yourpassword@localhost:5432/level1"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

autocommit - prevents accidental writes ; ensures the transaction safely 
autoflush - setting it to false givesmore control & prevents unexpected writes during queries
Flushing = sending pending changes to DB without committing. 
bind  -- > this tells SQL Alchemy to “Use this database engine for all sessions.”

Base = declarative_base()

- ----------to access the application apis --
http://0.0.0.0:8000
