
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()
playback_dao = PlaybackDao()

class PlaybackInfo(BaseModel):
    song_id: int
    user_id: int
    status: str  # Could be "PLAY", "PAUSE", etc.

@app.post("/playback/update", response_model=PlaybackInfo)
def update_playback(info: PlaybackInfo):
    playback_dao.update_playback(info.user_id, info.song_id, info.status)
    return {"song_id": info.song_id, "user_id": info.user_id, "status": info.status}
