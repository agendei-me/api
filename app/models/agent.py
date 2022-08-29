from sqlmodel import Field, SQLModel


class AgentBase(SQLModel):
    name: str = Field(default=None, max_length=50, nullable=True)
    is_active: bool = Field(default=True, nullable=False)


class Agent(AgentBase, table=True):
    __tablename__ = 'agents'

    id: str = Field(primary_key=True, max_length=50)
