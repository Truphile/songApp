from pydantic import BaseModel


class createSong(BaseModel):
    title: str
    artist: str

class updateSong(BaseModel):
    title: str
    artist: str

class deleteSong(BaseModel):
    title: str
    artist: str

class findSongs(BaseModel):
    id: int
    title: str
    artist: str

    class config:
        from_attributes = True