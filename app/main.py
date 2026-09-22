from fastapi import FastAPI
from app.media import get_video_info


app = FastAPI()

@app.get("/")
def home():
    return {"message": "Welcome to the Video Downloader API!"}

@app.get("/info")
def video_info(url: str):
    return get_video_info(url)