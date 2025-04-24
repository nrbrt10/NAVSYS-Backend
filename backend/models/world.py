from . import Field, SQLModel, Column, text, String, Optional, datetime

class DX_Instance(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str

class Points_Of_Interest(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    x: str
    y: str
    z: str
    size: Optional[float] = None