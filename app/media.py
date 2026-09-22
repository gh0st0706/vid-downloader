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
        'outtmpl': "download\%(title)s.%(ext)s",
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

url = input("Enter the video URL: ")

quality = int(input("Enter the desired quality (e.g., 720, 1080): "))

download_video(url, quality)


print("Video downloaded successfully!")

info = get_video_info(url)

print(f"Title: {info['title']}")
print(f"Duration: {info['duration']} seconds")
print(f"Number of formats: {len(info['formats'])}")

