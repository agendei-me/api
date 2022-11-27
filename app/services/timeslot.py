from datetime import datetime
from datetime import timedelta


def create_timeslots(start: datetime, end: datetime):
    n_timeslots: int = end.time().hour - start.time().hour
    timeslots: list = []

    if n_timeslots < 1:
        return []

    for timeslot in range(n_timeslots):
        timeslots.append(start + timedelta(hours=timeslot))
    return timeslots


def created_timeslots(events: list):
    timeslots: list = []

    if not events:
        return []

    for event in events:
        start_time: str = event['timestamp_from']
        timeslots.append(datetime.strptime(start_time[:-6], '%Y-%m-%dT%H:%M:%S'))
    return timeslots


def remove_created_timeslots(events_to_create: list, events_created: list):
    if not events_to_create:
        return []

    interator: int = 0
    timeslots: list[dict] = []

    for event_created in events_created:
        events_to_create.remove(event_created)

    for event_to_create in events_to_create:
        interator += 1
        timeslots.append({
            "id": interator,
            "dateTime": event_to_create,
            "date": event_to_create.date(),
            "time": event_to_create.time()
        }
        )

    return timeslots
