
from fastapi import FastAPI

app = FastAPI()

# Simulate a machine learning model
def get_real_time_recommendation(user_id: int):
    # Normally, this function would call a trained ML model
    return f"Recommended song for user {user_id} is Song123"

@app.get("/real-time-recommendation/{user_id}")
async def real_time_recommendation(user_id: int):
    recommendation = get_real_time_recommendation(user_id)
    return {"recommendation": recommendation}
