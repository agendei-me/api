from sqlmodel import SQLModel, Field


class Customer(SQLModel, table=True):
    __tablename__ = 'customers'

    id: str = Field(primary_key=True, max_length=50, nullable=False)
    name: str = Field(max_length=100, nullable=False)
    plan: str = Field(max_length=50, nullable=False)
    whatsapp_number: str = Field(max_length=15, nullable=False)
    is_active: bool = Field(default=True)

    agent_id: str = Field(nullable=False, foreign_key="agents.id")
