from uuid import uuid4
from app.models.client import Client

from sqlmodel import select, Session


def get_client(session: Session, client_id: str) -> Client | None:
    client = session.get(Client, client_id)
    if client.is_active:
        return client


def get_client_by_whatsapp_number(session: Session, whatsapp_number: str) -> Client:
    client = session.exec(
                select(
                    Client
                ).where(
                 Client.whatsapp_number == whatsapp_number, Client.is_active == True
                ).limit(1)
    ).first()
    return client


def get_clients(session: Session, skip: int = 0, limit: int = 100) -> list[Client]:
    clients = session.exec(
                select(
                    Client
                ).where(
                 Client.is_active == True
                ).offset(
                    skip
                ).limit(
                    limit
                )
    ).all()
    return clients


def insert_client(session: Session, client: Client) -> Client:
    db_client = Client(id=str(uuid4()),
                       name=client.name,
                       whatsapp_number=client.whatsapp_number)
    session.add(db_client)
    session.commit()
    session.refresh(db_client)
    return db_client


def delete_client(session: Session, client_id: str) -> bool:
    db_client = session.get(Client, client_id)
    if db_client:
        db_client.is_active = False

        session.add(db_client)
        session.commit()
        session.refresh(db_client)
    return bool(db_client)
