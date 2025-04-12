from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class SignalCreate(BaseModel):
    faction_tag: str
    x: str
    y: str
    z: str

class SignalRead(BaseModel):
    id: int
    faction_tag: str
    x: str
    y: str
    z: str
    dt: Optional[datetime]