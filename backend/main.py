from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .routers import signals, grids, gps

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins (ok for development)
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(signals.router)
app.include_router(grids.router)
app.include_router(gps.router)


@app.get("/")
async def root():
    return {"message": "Hi FastAPI."}