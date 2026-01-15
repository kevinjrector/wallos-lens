from fastapi import FastAPI
from app.routers import wallos

app = FastAPI()

@app.get("/")
async def read_root():
    return {"Hello": "World"}

app.include_router(wallos.router, prefix="/api/wallos", tags=["wallos"])