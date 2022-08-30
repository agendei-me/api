from sqlmodel import Field, SQLModel


class AvailabilityGroup(SQLModel, table=True):
    __tablename__ = 'availability_groups'

    id: str = Field(primary_key=True, max_length=50, nullable=False)
    name: str = Field(max_length=100, nullable=False)
    description: str = Field(max_length=255, nullable=False)

    place_id: str = Field(nullable=False, foreign_key="places.id")
