from pydantic import BaseModel, field_validator

class RegisterRequest(BaseModel):
    username: str
    password: str
    
    @field_validator("username")
    def username_must_not_be_empty(cls, v):
        if not v or v.strip() == "":
            raise ValueError("Username must not be empty")
        if len(v) > 50:
            raise ValueError("Username must be less than50 characters long")
        return v
    
    @field_validator("password")
    def password_must_meet_criteria(cls, v):
        if len(v) < 8:
            raise ValueError("Password must be at least 8 characters long")
        if len(v) > 128:
            raise ValueError("Password must be less than 128 characters long")
        return v
    
class LoginRequest(BaseModel):
    username: str
    password: str
        
        