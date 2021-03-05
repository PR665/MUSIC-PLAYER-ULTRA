from youtube_dl import YoutubeDL

from config import DURATION_LIMIT
from helpers.errors import DurationLimitError

ydl_opts = {
    "format": "bestaudio/best",
    "geo-bypass": True,
    "nocheckcertificate": True,
    "outtmpl": "downloads/%(id)s.%(ext)s",
}
ydl = YoutubeDL(ydl_opts)


def download(url: str) -> str:
    info = ydl.extract_info(url, False)
    duration = round(info["duration"] / 60)

    if duration > DURATION_LIMIT:
        raise DurationLimitError(
            f"😡🥺 VIDEOS LONGER THAN {DURATION_LIMIT} minute(s) AREN'T ALLOWED , THE PROVIDED VIDEO IS  {duration} minute(s)"
        )

    ydl.download([url])
    return f"downloads/{info['id']}.{info['ext']}"
