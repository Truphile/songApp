from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from models.user import User
from repositories.authDependency import get_current_user
from repositories.database import get_db
from schemas.songSchemas import createSong, deleteSong
from services.songService import create_song, search_songs, delete_song

router = APIRouter(prefix="/songs")

@router.post("/")
def add_song(song: createSong, database: Session = Depends(get_db),current_user: User = Depends(get_current_user)):
    return create_song(database, song, current_user)

@router.get("/search")
def search_song(query: str, database: Session = Depends(get_db),current_user: User = Depends(get_current_user)):
    return search_songs(database, query)

@router.delete("/{song_id}")
def remove_song(song_id: int, database: Session = Depends(get_db),current_user: User = Depends(get_current_user)):
    deleted_song = delete_song(database,song_id,current_user)

    if not deleted_song:
        raise HTTPException(status_code=404, detail="Song not found")
    return {"message": "Song deleted successfully"}

@router.put("/{song_id}")
def update_a_song(song_id: int, song: songUpdate)