import datetime
import os.path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

SCOPES = ["https://www.googleapis.com/auth/calendar"]


def create(name, date, timeStart, timeEnd):
    creds = None

    if os.path.exists("secrets/token.json"):
        creds = Credentials.from_authorized_user_file("secrets/token.json", SCOPES)

    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                "secrets/credentials.json", SCOPES
            )
            creds = flow.run_local_server(port=0)

        with open("secrets/token.json", "w") as token:
            token.write(creds.to_json())

    try:
        service = build("calendar", "v3", credentials=creds)

        event = {
            "summary": f"{name}",
            "location": "45 Stokes Hill Road, Stokes Hill NT 0800",
            "description": "RFDS Working Shift",
            "colorId": 1,
            "start": {
                "dateTime": f"{date}T{timeStart}+09:30",  # "2024-05-22T10:00:00+09:30",
                "timeZone": "Australia/Darwin",
            },
            "end": {
                "dateTime": f"{date}T{timeEnd}+09:30",
                "timeZone": "Australia/Darwin",
            },
            "reminders": {"usedefault": True},
        }

        event = service.events().insert(calendarId="primary", body=event).execute()
        print(f"Event Created {event.get('htmlLink')}")

    except HttpError as error:
        print("An Error Occurred:", error)


if __name__ == "__SendToGoogle__":
    create()
