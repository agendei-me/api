from sqlmodel import Session, create_engine

POSTGRES_DATABASE_URL = "postgresql://postgres:caio123@localhost/agendei"
engine = create_engine(POSTGRES_DATABASE_URL)


def get_session():
    with Session(engine) as session:
        yield session
