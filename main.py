from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from backend.routers import signals, grids, gps, world

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins (ok for development)
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(grids.router)
app.include_router(gps.router)
app.include_router(world.router)


@app.get("/")
async def root():
    return {"message": "NAVSYS"}

@app.get("/render")
async def render_health_check():
    return {"status": "ok"}