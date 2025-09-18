from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routers import sensor, auth

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Routes
app.include_router(sensor.router, prefix="/api")
app.include_router(auth.router, prefix="/api/auth")

@app.get("/")
def read_root():
    return {"message": "Welcome to StratoShield Backend"}

