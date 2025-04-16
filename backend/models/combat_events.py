from . import Field, SQLModel, Column, text, String, Optional, datetime

class Events(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    event_name: str

class Event_Log(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    event_id: int = Field(foreign_key="events.id")
    timestamp: Optional[datetime] = Field(
        sa_column=Column(String, server_default=text("datetime()"))
    )