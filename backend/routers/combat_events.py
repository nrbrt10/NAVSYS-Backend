from fastapi import APIRouter, HTTPException
from sqlmodel import select

from backend.models.combat_events import Events, Event_Log
from backend.schemas.combat_events import EventsCreate, EventsRead, Event_LogCreate, Event_LogRead
from backend.db.db_manager import DatabaseHandler

router = APIRouter()
db = DatabaseHandler()

@router.get("/api/v1/events/", response_model=list[EventsRead], tags=["events"])
async def get_signals():
    with db.get_session() as session:
        events = session.exec(select(Events)).all()
        return events
