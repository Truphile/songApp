from fastapi import Header, Depends, HTTPException
from sqlalchemy.orm import Session
from models.user import User
from repositories.database import get_db


def get_current_user():
    email: str = Header(...)
    database: Session = Depends(get_db())

    user = database.query(User).filter(User.email == email).first()

    if not user:
        raise HTTPException(status_code=401,detail="UNAUTHORIZED")
    return user