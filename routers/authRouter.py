from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from repositories.database import get_db
from schemas.userSchemas import userRegister, userLogin
from services.authService import register_user, authenticate_user

router = APIRouter()

@router.post("/register")
def register(user: userRegister, database: Session = Depends(get_db)):
    new_user = register_user(database, user)

    if not new_user:
        raise HTTPException(status_code=400, detail="User already exists")

    return {"message": "User registered"}

@router.post("/login")
def login(user: userLogin, database: Session = Depends(get_db)):
    auth_user = authenticate_user(database, user)

    if not auth_user:
        raise HTTPException(status_code=400, detail="Incorrect username or password")
    return {"message": "Login successful"}