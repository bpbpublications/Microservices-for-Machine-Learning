
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()
catalog_dao = CatalogDao()

class Song(BaseModel):
    id: int
    title: str
    artist: str

@app.get("/catalog/song/{song_id}", response_model=Song)
def get_song_by_id(song_id: int):
    song = catalog_dao.get_song_by_id(song_id)
    if song is None:
        raise HTTPException(status_code=404, detail="Song not found")
    return {"id": song[0], "title": song[1], "artist": song[2]}
