from fastapi import FastAPI

from .routers import signals, grids

app = FastAPI()

app.include_router(signals.router)
app.include_router(grids.router)


@app.get("/")
async def root():
    return {"message": "Hi FastAPI."}