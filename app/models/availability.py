from sqlmodel import Field, SQLModel
from datetime import datetime


class Availability(SQLModel, table=True):
    __tablename__ = 'availabilities'

    id: str = Field(primary_key=True, max_length=50, nullable=False)
    timestamp_from: datetime = Field(default=None)
    timestamp_to: datetime = Field(default=None)
    is_active: bool = Field(default=True)

    availability_group_id: str = Field(nullable=False, foreign_key="availability_groups.id")
