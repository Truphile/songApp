from fastapi import Depends, HTTPException

from models.user import User
from repositories.authDependency import get_current_user


def admin(current_user: User = Depends(get_current_user)):
    if current_user.role != "admin":
        raise HTTPException(status_code=403, detail="Admin privilege required")
    return current_user