from fastapi import APIRouter
from pydantic import BaseModel
from os.path import join

from backend.db.db_manager import DatabaseHandler
from backend.config import DB_DIR, DB_NAME

router = APIRouter()
db = DatabaseHandler(join(DB_DIR, DB_NAME))

class Signal(BaseModel):
    faction_tag: str
    x: str
    y: str
    z: str

@router.get("/signals/", tags=["signals"])
async def read_signals():
    return [{"signal" : "some signal"}, {"signal" : "some other signal"}]

@router.post("/signals/", tags=["signals"])
async def post_signals(signal: Signal):
    try:
        await db.run_query(query=f"insert into signals (faction_tag, x, y, z) values (\"{signal.faction_tag}\", \"{signal.x}\", \"{signal.y}\", \"{signal.z}\");")
    except Exception as e:
        print(e)
    return
