from urllib.parse import urlparse
import subprocess
import os


def can_handle(url):
    path = urlparse(url).path.lower()
    return path.endswith(".m3u8")


def download(url):
    os.makedirs("downloads", exist_ok=True)

    output_path = os.path.join(
        "downloads",
        "hls_video.mp4"
    )

    command = [
        "ffmpeg",
        "-i", url,
        "-c", "copy",
        output_path
    ]

    subprocess.run(command, check=True)

    return output_path