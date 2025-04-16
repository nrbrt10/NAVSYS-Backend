from . import Field, SQLModel, Column, text, String, Optional, datetime

class Grids(SQLModel, table=True):
    id: int = Field(primary_key=True)
    name: str
    owner: str
    faction: Optional[str] = Field(default=None) 
    pilot: Optional[str] = Field(default=None)

class Grid_Position(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    grid_id: int = Field(foreign_key="grids.id")
    x: str
    y: str
    z: str
    timestamp: Optional[datetime] = Field(
        sa_column=Column(String, server_default=text("datetime()"))
    )