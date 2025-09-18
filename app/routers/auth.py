from fastapi import APIRouter

router = APIRouter()

@router.post("/login")
def login(user: dict):
    # Dummy login logic
    if user.get("email") and user.get("password"):
        return {"access_token": "fake-jwt-token", "user": {"email": user["email"]}}
    return {"error": "Invalid credentials"}

