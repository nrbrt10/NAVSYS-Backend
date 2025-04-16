from . import Field, SQLModel, Column, text, String, Optional, datetime

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