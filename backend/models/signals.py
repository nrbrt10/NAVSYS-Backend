from sqlmodel import Field, SQLModel
from sqlalchemy import Column, text, String
from typing import Optional

class Signals(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    faction_tag: str
    x: str
    y: str
    z: str
    dt: Optional[str] = Field(
        default=None,
        sa_column=Column(String, server_default=text("datetime()"))
    )