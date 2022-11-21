from __future__ import print_function

import json
from dataclasses import dataclass
import datetime
import os.path
from datetime import timedelta

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError


SCOPES = ['https://www.googleapis.com/auth/calendar']


@dataclass
class Events:
    creds = None
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file('credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        with open('token.json', 'w') as token:
            token.write(creds.to_json())

    service = build('calendar', 'v3', credentials=creds)

    def get_events(self, calendar_id: str, date: datetime.date = datetime.date.today()):
        try:
            start = (datetime.datetime.combine(date, datetime.datetime.min.time()) + timedelta(hours=3)).isoformat() + 'Z'
            end = (datetime.datetime.combine(date, datetime.datetime.max.time()) + timedelta(hours=3)).isoformat() + 'Z'

            events_result = self.service.events().list(calendarId=calendar_id,
                                                       timeMin=start, timeMax=end,
                                                       singleEvents=True,
                                                       orderBy='startTime').execute()
            events = events_result.get('items', [])
            response: list[dict] = []

            for event in events:
                response.append({
                "calendar_id": event['organizer']['email'],
                "event_id": event['id'],
                "summary": event['summary'],
                "description": event['description'],
                "timestamp_from": event['start']['dateTime'],
                "timestamp_to": event['end']['dateTime'],
                "status": event['status']
                })

            return response
        except HttpError as error:
            print('An error occurred: %s' % error)

    def create_event(self, calendar_id: str, summary: str, description: str, timestamp_from: datetime.datetime):
        start = timestamp_from.isoformat() + 'Z'
        end = (timestamp_from + timedelta(hours=1)).isoformat() + 'Z'

        try:
            body = {
                'summary': summary,
                'description': description,
                'start': {
                    'dateTime': start,
                    'timeZone': 'America/Sao_Paulo',
                },
                'end': {
                    'dateTime': end,
                    'timeZone': 'America/Sao_Paulo',
                }
            }

            event = self.service.events().insert(calendarId=calendar_id, body=body).execute()
            return event.get('id')
        except HttpError as error:
            print('An error occurred: %s' % error)

    def cancel_event(self, calendar_id: str, event_id: str):
        try:
            self.service.events().delete(calendarId=calendar_id, eventId=event_id).execute()
            return True
        except HttpError as error:
            print('An error occurred: %s' % error)
