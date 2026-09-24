import yt_dlp


def get_info(url):
    options = {
        "quiet": True,
        "skip_download": True
    }

    with yt_dlp.YoutubeDL(options) as ydl:
        return ydl.extract_info(url, download=False)

def download(url, quality):
    options = {
        "format": f"bestvideo[height<={quality}]+bestaudio/best[height<={quality}]",
        "merge_output_format": "mp4",
        "outtmpl": "downloads/%(title)s.%(ext)s"
    }

    with yt_dlp.YoutubeDL(options) as ydl:
        ydl.download([url])