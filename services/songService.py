from models.song import Song


def create_song(database, song_data, current_user):
    new_song = Song(
        title=song_data.title,
        artist=song_data.artist,
        owner_id=current_user.id
    )

    database.add(new_song)
    database.commit()
    database.refresh(new_song)

    return new_song

def update_song(database, song_id, song_data, current_user):

    if current_user.role == "admin":
        song = database.query(Song).filter(Song.id == song_id).first()
    else:
        song = database.query(Song).filter(Song.id == song_id, Song.owner_id == current_user).first()

    if not song:
        return False

    database.delete(song)
    database.commit()

    return True

def