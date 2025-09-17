from fastapi import FastAPI
from app.routers import risk

app = FastAPI()

app.include_router(risk.router, prefix="/api")
