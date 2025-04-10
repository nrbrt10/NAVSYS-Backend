from fastapi import FastAPI

from .routers import signals

app = FastAPI()

app.include_router(signals.router)

@app.get("/")
async def root():
    return {"message": "Hi FastAPI."}