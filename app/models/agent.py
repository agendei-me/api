from sqlmodel import Field, SQLModel, Relationship
from typing import Optional, List
from datetime import datetime


class AgentBase(SQLModel):
    name: str = Field(default=None, max_length=50, nullable=True, sa_column_kwargs={'unique': True})


class Agent(AgentBase, table=True):
    __tablename__ = 'agents'

    id: str = Field(primary_key=True, max_length=50, nullable=False)
    is_active: bool = Field(default=True, nullable=False)
    created_at: Optional[datetime] = Field(default=datetime.now())
