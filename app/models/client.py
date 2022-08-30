from sqlmodel import Field, SQLModel


class Client(SQLModel, table=True):
    __tablename__ = 'clients'

    id: str = Field(primary_key=True, max_length=50, nullable=False)
    name: str = Field(max_length=100, nullable=False)
    whatsapp_number: str = Field(max_length=15, nullable=False)
    is_active: bool = Field(default=True)
