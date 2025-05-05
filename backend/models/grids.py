from . import Field, SQLModel, Column, text, String, Optional, datetime

class Grids(SQLModel, table=True):
    uuid: str = Field(primary_key=True)
    entity_id: str
    static_grid: bool = Field(default=False)
    grid_name: str
    owner_id: str
    faction_tag: Optional[str] = Field(default=None)
    pilot: Optional[str] = Field(default=None)
    created_at: Optional[datetime] = Field(
        sa_column=Column(String, server_default=text("datetime()"))
    )
    

class Grid_Positions(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    grid_uuid: str = Field(foreign_key="grids.uuid")
    x: str
    y: str
    z: str
    created_at: Optional[datetime] = Field(
        sa_column=Column(String, server_default=text("datetime()"))
    )