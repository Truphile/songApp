from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from models.user import User
from repositories.authDependency import get_current_user
from repositories.database import get_db
from schemas.songSchemas import createSong
from services.songService import create_song

router = APIRouter(prefix="/songs")

@router.post("/")
def add_song(song: createSong, database: Session = Depends(get_db),current_user: User = Depends(get_current_user)):
    return create_song(database, song, current_user)