from sqlmodel import Field, SQLModel


class AvailabilityGroupService(SQLModel, table=True):
    __tablename__ = 'availability_groups_services'

    id: str = Field(primary_key=True, max_length=50, nullable=False)

    availability_group_id: str = Field(nullable=False,
                                       foreign_key="availability_groups.id",
                                       primary_key=True
                                       )
    service_id: str = Field(nullable=False,
                            foreign_key="services.id",
                            primary_key=True
                            )
