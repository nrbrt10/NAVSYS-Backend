from . import BaseModel, Optional, datetime

class EventsCreate(BaseModel):
    event_name: str

class EventsRead(BaseModel):
    id: int
    event_name: str

class Event_LogCreate(BaseModel):
    event_id: int

class Event_LogRead(BaseModel):
    id: int
    type_id: int
    timestamp: Optional[datetime]