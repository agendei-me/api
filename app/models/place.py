from sqlmodel import Field, SQLModel


class Place(SQLModel, table=True):
    __tablename__ = 'places'

    id: str = Field(primary_key=True, nullable=False, max_length=50)
    name: str = Field(max_length=100, nullable=False)
    place_url: str = Field(max_length=100, nullable=False)

    customer_id: str = Field(nullable=False, foreign_key="customers.id")
