import app
from fastapi import Depends, APIRouter
from app.models.client import Client
from app.services.google.events import Events
from datetime import datetime, timedelta
from app.models.timeslot import TimeslotBase
from app.models.appointment import Appointment
from app.services.timeslot import created_timeslots, create_timeslots, remove_created_timeslots
from app.services.client import get_client_by_whatsapp_number, insert_client
from app.services.appointment import insert_appointment, get_appointment_by_client_id
from app.database.postgres_connection import engine, get_session
from sqlmodel import Session

app.models.client.SQLModel.metadata.create_all(bind=engine)

router = APIRouter(prefix='/timeslots', )


@router.post("/")
async def create_event(timeslot: TimeslotBase, session: Session = Depends(get_session)):
    events = Events()
    timestamp_from = datetime.strptime(timeslot.timestamp_from, '%Y-%m-%dT%H:%M:%S') + timedelta(hours=3)
    event_created = events.create_event(timeslot.calendar_id, timeslot.summary, timeslot.description, timestamp_from)
    client = get_client_by_whatsapp_number(session=session, whatsapp_number=timeslot.whatsapp_number)

    if not client:
        client = Client(name=timeslot.summary, whatsapp_number=timeslot.whatsapp_number)
        client = insert_client(session=session, client=client)
    appointment = Appointment(calendar_id=timeslot.calendar_id, client_id=client.id, event_id=event_created)
    insert_appointment(session=session, appointment=appointment)
    return event_created


@router.get("/last-event")
async def get_event(whatsapp_number: str,  session: Session = Depends(get_session)):
    events = Events()
    client = get_client_by_whatsapp_number(session=session, whatsapp_number=whatsapp_number)
    appointment = get_appointment_by_client_id(session=session, client_id=client.id)
    last_event = events.get_event(appointment.calendar_id, appointment.event_id)
    last_event["information"] = True

    return last_event


@router.get("/")
async def get_events(calendar_id: str, when: str):
    events = Events()
    date = datetime.strptime(when, '%Y-%m-%d')
    created_events = events.get_events(calendar_id, date)
    return created_events


@router.get("/free")
async def get_events(calendar_id: str, when: str):
    events = Events()
    date = datetime.strptime(when, '%Y-%m-%d')
    start = date + timedelta(hours=9)
    end = date + timedelta(hours=23)

    created_events = events.get_events(calendar_id, date)

    created = created_timeslots(created_events)
    to_create = create_timeslots(start, end)

    free = remove_created_timeslots(to_create, created)

    return free


@router.delete("/")
async def delete_events(calendar_id: str, event_id: str):
    events = Events()
    deleted_event = events.cancel_event(calendar_id, event_id)
    return deleted_event
