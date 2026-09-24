from fastapi import FastAPI
from pydantic import BaseModel

from app.media import get_video_info, download_video


app = FastAPI()


class DownloadRequest(BaseModel):
    url: str
    quality: int


@app.get("/")
def home():
    return {"message": "Video Downloader API is running"}


@app.get("/info")
def video_info(url: str):
    return get_video_info(url)


@app.post("/download")
def download(request: DownloadRequest):
    download_video(request.url, request.quality)

    return {
        "message": "Download complete"
    }