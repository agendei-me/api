from sqlmodel import Session, create_engine
import os

POSTGRES_DATABASE_URL = os.getenv("DB_URL")
engine = create_engine(POSTGRES_DATABASE_URL)


def get_session():
    with Session(engine) as session:
        yield session
