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
