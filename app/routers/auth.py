from fastapi import APIRouter, HTTPException, Depends
from app.schemas.auth import LoginRequest, RegisterRequest
from app.database import get_db
from app.models.user import User
from app.auth import hash_password, verify_password, create_access_token

router = APIRouter()

@router.post("/register")
def register(request: RegisterRequest, db=Depends(get_db)):
    """Register a new user."""
    existing_user = db.query(User).filter(User.username == request.username).first()
    if existing_user:
        raise HTTPException(status_code=400, detail="Username already exists")
    
    hashed_pw = hash_password(request.password)
    new_user = User(username=request.username, hashed_password=hashed_pw)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    
    return {
        "success": True,
        "message": "User registered successfully",
        "user_id": new_user.id,
        "username": new_user.username
    }