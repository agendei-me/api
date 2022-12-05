from uuid import uuid4
from app.models.appointment import Appointment, States

from sqlmodel import select, Session


def get_appointment(session: Session, appointment_id: str) -> Appointment | None:
    appointment = session.get(Appointment, appointment_id)
    return appointment


def get_appointments_by_client_id(session: Session, client_id: str) -> list[Appointment]:
    appointments = session.exec(
                select(
                    Appointment
                ).where(
                 Appointment.client_id == client_id
                )
    ).all()
    return appointments


def insert_appointment(session: Session, appointment: Appointment) -> Appointment:
    db_appointment = Appointment(id=str(uuid4()),
                                 event_id=appointment.event_id,
                                 client_id=appointment.client_id
                                 )
    session.add(db_appointment)
    session.commit()
    session.refresh(db_appointment)
    return db_appointment


def update_appointment(session: Session, appointment_id: str, state: States) -> Appointment:
    db_appointment = session.get(Appointment, appointment_id)
    if db_appointment:
        db_appointment.state = state

        session.add(db_appointment)
        session.commit()
        session.refresh(db_appointment)
    return db_appointment

