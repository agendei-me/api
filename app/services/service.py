from uuid import uuid4
from app.models.service import Service, ServiceBase

from sqlmodel import select, Session


def get_service(session: Session, service_id: str) -> Service | None:
    service = session.get(Service, service_id)
    return service


def get_services(session: Session, skip: int = 0, limit: int = 100) -> list[Service]:
    services = session.exec(
                select(
                    Service
                ).offset(
                    skip
                ).limit(
                    limit
                )
    ).all()
    return services


def insert_service(session: Session, service: ServiceBase) -> Service:
    db_service = Service(id=str(uuid4()),
                         name=service.name,
                         duration_min=service.duration_min,
                         price=service.price,
                         availability_group_id=service.availability_group_id)
    session.add(db_service)
    session.commit()
    session.refresh(db_service)
    return db_service


def update_service(session: Session, service_id: str, service: ServiceBase) -> Service:
    db_service = session.get(Service, service_id)
    if db_service:
        db_service.name = service.name
        db_service.price = service.price
        db_service.duration_min = service.duration_min

        session.add(db_service)
        session.commit()
        session.refresh(db_service)
    return db_service


def delete_service(session: Session, service_id: str) -> bool:
    db_service = session.get(Service, service_id)
    if db_service:
        db_service.name = "DELETED"

        session.add(db_service)
        session.commit()
        session.refresh(db_service)
    return bool(db_service)
