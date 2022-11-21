from fastapi import APIRouter
from app.services.google.events import Events
from datetime import datetime, timedelta
from app.models.timeslot import TimeslotBase
from app.services.timeslot import created_timeslots, create_timeslots, remove_created_timeslots


router = APIRouter(prefix='/timeslots', )


@router.post("/")
async def create_event(timeslot: TimeslotBase):
    events = Events()
    timestamp_from = datetime.strptime(timeslot.timestamp_from[:-6], '%Y-%m-%dT%H:%M:%S') + timedelta(hours=3)
    event_created = events.create_event(timeslot.calendar_id, timeslot.summary, timeslot.description, timestamp_from)
    return event_created


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
