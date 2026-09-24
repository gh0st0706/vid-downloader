import app.handlers.ytdlp_handler as ytdlp_handler
import app.handlers.direct_handler as direct_handler


def get_video_info(url):
    if direct_handler.can_handle(url):
        return {
            "title": url.split("/")[-1],
            "duration": None,
            "thumbnail": None,
            "formats": []
        }

    info = ytdlp_handler.get_info(url)

    return {
        "title": info.get("title"),
        "duration": info.get("duration"),
        "thumbnail": info.get("thumbnail"),
        "formats": info.get("formats", [])
    }


def download_video(url, quality):
    if direct_handler.can_handle(url):
        return direct_handler.download(url)

    return ytdlp_handler.download(url, quality)