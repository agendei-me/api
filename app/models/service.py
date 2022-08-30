from sqlmodel import Field, SQLModel


class Service(SQLModel, table=True):
    __tablename__ = 'services'

    id: str = Field(primary_key=True, max_length=50, nullable=False)
    name: str = Field(max_length=100, nullable=False)
    duration_min: int = Field(default=0, nullable=False)
    price: float = Field(default=0.0, nullable=False)

    availability_group_id: str = Field(nullable=False, foreign_key="availability_groups.id")
