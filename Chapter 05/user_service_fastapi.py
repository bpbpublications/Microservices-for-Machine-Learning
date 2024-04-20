
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()
user_dao = UserDao()

class User(BaseModel):
    username: str
    password: str

@app.post("/user/add", response_model=User)
def add_user(user: User):
    user_dao.add_user(user.username, user.password)
    return {"username": user.username, "password": user.password}

@app.post("/user/check", response_model=User)
def check_user(user: User):
    if user_dao.check_user(user.username, user.password):
        return {"username": user.username, "password": user.password}
    else:
        raise HTTPException(status_code=401, detail="Unauthorized")
