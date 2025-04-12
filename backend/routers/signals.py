from fastapi import APIRouter, HTTPException
from sqlmodel import select
from datetime import datetime

from backend.models.signals import Signals
from backend.schemas.signals import SignalCreate, SignalRead
from backend.db.db_manager import DatabaseHandler

router = APIRouter()
db = DatabaseHandler()

@router.get("/signals/", response_model=list[SignalRead], tags=["signals"])
async def get_signals():
    with db.get_session() as session:
        signals = session.exec(select(Signals)).all()
        return signals

@router.post("/signals/", response_model=SignalRead, tags=["signals"])
async def post_signal(signal_data: SignalCreate):

    signal_dict = signal_data.model_dump(exclude_unset=True)
    signal = Signals(**signal_dict)

    with db.get_session() as session:
        session.add(signal)
        session.commit()
        session.refresh(signal)
        return signal