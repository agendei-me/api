from uuid import uuid4
from app.models.agent import Agent, AgentBase

from sqlmodel import select, Session


def get_agent(session: Session, agent_id: str) -> Agent | None:
    agent = session.get(Agent, agent_id)
    if agent.is_active:
        return agent


def get_agents(session: Session, skip: int = 0, limit: int = 100) -> list[Agent]:
    agents = session.exec(
                select(
                    Agent
                ).where(
                 Agent.is_active == True
                ).offset(
                    skip
                ).limit(
                    limit
                )
    ).all()
    return agents


def insert_agent(session: Session, agent: AgentBase) -> Agent:
    db_agent = Agent(id=str(uuid4()),
                     name=agent.name)
    session.add(db_agent)
    session.commit()
    session.refresh(db_agent)
    return db_agent


def update_agent(session: Session, agent_id: str, agent: AgentBase) -> Agent:
    db_agent = session.get(Agent, agent_id)
    if db_agent:
        db_agent.name = agent.name

        session.add(db_agent)
        session.commit()
        session.refresh(db_agent)
    return db_agent


def delete_agent(session: Session, agent_id: str) -> bool:
    db_agent = session.get(Agent, agent_id)
    if db_agent:
        db_agent.is_active = False

        session.add(db_agent)
        session.commit()
        session.refresh(db_agent)
    return bool(db_agent)
