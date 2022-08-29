from fastapi import Depends, APIRouter, HTTPException
import app
from app.database.postgres_connection import engine, get_session
from app.services.agent import insert_agent, get_agent, get_agents, update_agent, delete_agent
from app.models.agent import Agent, AgentBase
from sqlmodel import Session

app.models.agent.SQLModel.metadata.create_all(bind=engine)

router = APIRouter(prefix='/agents', )


@router.post("/", response_model=Agent)
def create_agent(agent: AgentBase, session: Session = Depends(get_session)):
    return insert_agent(session=session, agent=agent)


@router.get("/", response_model=list[Agent])
def read_agents(skip: int = 0, limit: int = 100, session: Session = Depends(get_session)):
    agents = get_agents(session=session, skip=skip, limit=limit)
    return agents


@router.get("/{agent_id}", response_model=Agent)
def read_agent(agent_id: str, session: Session = Depends(get_session)):
    agent = get_agent(session=session, agent_id=agent_id)
    if agent is None:
        raise HTTPException(status_code=404, detail='Agent not found')
    return agent


@router.put("/{agent_id}", response_model=Agent)
def change_agent(agent_id: str, agent: AgentBase, session: Session = Depends(get_session)):
    agent = update_agent(session=session, agent_id=agent_id, agent=agent)
    return agent


@router.delete("/{agent_id}")
def remove_agent(agent_id: str, session: Session = Depends(get_session)):
    agent = delete_agent(agent_id=agent_id, session=session)
    return f'success: {agent}'
