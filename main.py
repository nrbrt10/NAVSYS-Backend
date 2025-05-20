from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from backend.routers import signals, grids, gps, world

app = FastAPI()

origins = [
    'https://navsys-frontend.vercel.app', 
    'http://localhost:5173'
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(grids.router)
app.include_router(gps.router)
app.include_router(world.router)


@app.get("/")
async def root():
    return {"message": "OK"}

@app.get("/render")
async def render_health_check():
    return {"status": "ok"}