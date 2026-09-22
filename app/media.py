print("Video Downloader")

import yt_dlp

def get_video_info(url):
    ydl_opts = {
        'quiet': True,
        'skip_download': True,
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=False)
        return {
            "title": info.get("title"),
            "duration": info.get("duration"),
            "thumbnail": info.get("thumbnail", None),
            "formats": info.get("formats", []),
        }

def download_video(url, quality):
    ydl_opts = {
        'format': f"bestvideo[height<={quality}]+bestaudio/best[height<={quality}]",
        "merge_output_format": 'mp4',
        'outtmpl': "downloads/%(title)s.%(ext)s",
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])



