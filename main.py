from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routers import sensor, auth, dashboard

app = FastAPI()

# ✅ Allow frontend to talk with backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # You can replace "*" with your frontend URL later
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ✅ Attach routers
app.include_router(sensor.router, prefix="/api")
app.include_router(auth.router, prefix="/api/auth")
app.include_router(dashboard.router, prefix="/api")

@app.get("/")
def read_root():
    return {"message": "Welcome to StratoShield Backend"}
