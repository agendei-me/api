from sqlmodel import Field, SQLModel
from datetime import datetime
from pydantic import BaseModel


class Timeslot(SQLModel, table=True):
    __tablename__ = 'timeslots'

    id: str = Field(primary_key=True, max_length=50, nullable=False)
    timestamp_from: datetime = Field(default=None)
    timestamp_to: datetime = Field(default=None)
    is_available: bool = Field(default=True)

    availability_id: str = Field(nullable=False, foreign_key="availabilities.id")


class TimeslotBase(BaseModel):
    calendar_id: str
    summary: str
    description: str
    timestamp_from: str
