from fastapi import FastAPI
from app.routers import wallos
from app.routers import auth
from app.database import create_tables

create_tables()

app = FastAPI()

@app.get("/")
async def read_root():
    return {"Hello": "World"}

app.include_router(wallos.router, prefix="/api/wallos", tags=["wallos"])
app.include_router(auth.router, prefix="/api/auth", tags=["auth"])