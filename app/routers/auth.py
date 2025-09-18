from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

router = APIRouter()

# Request body model
class LoginRequest(BaseModel):
    email: str
    password: str

# Response model
class LoginResponse(BaseModel):
    access_token: str
    user: dict

@router.post("/login", response_model=LoginResponse)
def login(credentials: LoginRequest):
    # ✅ For demo: accept any email + password
    if not credentials.email or not credentials.password:
        raise HTTPException(status_code=400, detail="Email and password required")

    return {
        "access_token": "fake-jwt-token-12345",  # You can swap later with real JWT
        "user": {
            "id": 1,
            "email": credentials.email,
            "name": "Demo User"
        }
    }

@router.post("/logout")
def logout():
    return {"message": "Logged out successfully"}

@router.get("/verify-token")
def verify_token():
    # ✅ Demo: always return valid
    return {"valid": True, "user": {"id": 1, "email": "demo@stratoshield.com"}}
