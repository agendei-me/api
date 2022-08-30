from sqlmodel import Field, SQLModel
from enum import Enum


class States(str, Enum):
    scheduled = "SDD"
    canceled = "CLC"
    finished = "FNS"


class Appointment(SQLModel, table=True):
    __tablename__ = 'appointments'

    id: str = Field(primary_key=True, max_length=50, nullable=False)
    state: States = Field(default=States.scheduled, max_length=20)
    observation: str = Field(default=None, max_length=255)

    timeslot_id: str = Field(nullable=False, foreign_key="timeslots.id")
    client_id: str = Field(nullable=False, foreign_key="clients.id")
