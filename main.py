from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Dict

app = FastAPI()

# ---- Pydantic Schema ----
class Agent(BaseModel):
    agent_id: int
    name: str
    age: int
    city: str
    area: str


# ---- In-Memory DB (Dict) ----
agents_db: Dict[int, Agent] = {}


# -----------------------------
#          CREATE (POST)
# # -----------------------------
# @app.post("/agents")
# def create_agent(agent: Agent):
#     if agent.agent_id in agents_db:
#         raise HTTPException(status_code=400, detail="Agent ID already exists")

#     agents_db[agent.agent_id] = agent
#     return {"message": "Agent created successfully", "agent": agent}


# # -----------------------------
# #          READ (GET)
# # -----------------------------
# @app.get("/agents")
# def get_all_agents():
#     return list(agents_db.values())


# @app.get("/agents/{agent_id}")
# def get_agent(agent_id: int):
#     if agent_id not in agents_db:
#         raise HTTPException(status_code=404, detail="Agent not found")
#     return agents_db[agent_id]


# # -----------------------------
# #          UPDATE (PUT)
# # -----------------------------
# @app.put("/agents/{agent_id}")
# def update_agent(agent_id: int, updated_agent: Agent):
#     if agent_id not in agents_db:
#         raise HTTPException(status_code=404, detail="Agent not found")

#     agents_db[agent_id] = updated_agent
#     return {"message": "Agent updated successfully", "agent": updated_agent}


# # -----------------------------
# #          DELETE (DELETE)
# # -----------------------------
# @app.delete("/agents/{agent_id}")
# def delete_agent(agent_id: int):
#     if agent_id not in agents_db:
#         raise HTTPException(status_code=404, detail="Agent not found")

#     del agents_db[agent_id]
#     return {"message": "Agent deleted successfully"}
