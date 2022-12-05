from sqlmodel import Field, SQLModel
from enum import Enum
from datetime import datetime


class States(str, Enum):
    scheduled = "SDD"
    canceled = "CLC"
    finished = "FNS"


class Appointment(SQLModel, table=True):
    __tablename__ = 'appointments'

    id: str = Field(primary_key=True, max_length=50, nullable=False)
    state: States = Field(default=States.scheduled, max_length=20)
    observation: str = Field(default=None, max_length=255)

    calendar_id: str = Field(nullable=False)
    event_id: str = Field(nullable=False)
    client_id: str = Field(nullable=False, foreign_key="clients.id")
    created_at: datetime = Field(nullable=False, default=datetime.now())
