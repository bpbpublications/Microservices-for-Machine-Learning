
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()
recommendation_dao = RecommendationDao()

class Recommendation(BaseModel):
    user_id: int
    recommendation: str  # Could be a list of song IDs, genres, etc.

@app.post("/recommendation/add", response_model=Recommendation)
def add_recommendation(rec: Recommendation):
    recommendation_dao.add_log(rec.user_id, rec.recommendation)
    return {"user_id": rec.user_id, "recommendation": rec.recommendation}

@app.get("/recommendation/user/{user_id}", response_model=Recommendation)
def get_recommendation(user_id: int):
    recommendation = recommendation_dao.get_user_preferences(user_id)
    if recommendation is None:
        raise HTTPException(status_code=404, detail="Recommendation not found")
    return {"user_id": user_id, "recommendation": recommendation}
