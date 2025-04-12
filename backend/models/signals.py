from sqlmodel import Field, SQLModel
from typing import Optional

class Signals(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    faction_tag: str
    x: str
    y: str
    z: str
    dt: str | None = None