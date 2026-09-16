import os
import sys


def play_video(filepath):  # tikupanga zot tipange play the downloded video
    abs_path = os.path.abspath(filepath)  # filepath of our video
    print(f"Opening Video: {abs_path}")

    if sys.platform == "win32":  # checking window os
        os.startfile(abs_path)

    elif sys.platform == "darwin":
        os.system(f"open '{abs_path}'")

    else:
        for player in ["xdg-open", "vlc", "mpv"]:
            if os.system(f"which {player} > /dev/null 2>&1") == 0:
                os.system(f"{player} '{abs_path}' &")
                return
        print("no suitable player found in your system !!!")


def download_video(url, output_name="downloaded_video", output_dir=".", autoplay=True):
    try:
        import yt_dlp
    except ImportError as exc:
        raise RuntimeError("yt-dlp is not installed. Install it with `pip install yt-dlp`.") from exc

    os.makedirs(output_dir, exist_ok=True)
    output_template = os.path.join(output_dir, f"{output_name}.%(ext)s")
    ydl_opts = {
        'outtmpl': output_template,
        'format': 'bestvideo+bestaudio/best',
        'merge_output_format': 'mp4',
        'progress_hooks': [hook],
        'extractor_args': {
            'youtube': {
                'player_client': ['ios', 'android', 'web'],
            }
        },
    }
    print(f"fetching url(kuitapa link):{url}\n")
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=True)
        ext = info.get('ext', 'mp4')
        final_file = os.path.join(output_dir, f"{output_name}.{ext}")

        # merge_output_format forces mp4 when video+audio are merged,
        # so fall back to that if the reported ext doesn't match an existing file
        if not os.path.exists(final_file):
            fallback_file = os.path.join(output_dir, f"{output_name}.mp4")
            if os.path.exists(fallback_file):
                final_file = fallback_file

        print(f"Video downloaded successfully: {final_file}")

        if autoplay:
            play_video(final_file)

        return {
            "title": info.get("title"),
            "ext": ext,
            "filepath": os.path.abspath(final_file),
        }


def hook(d):
    if d["status"] == "downloading":
        downloaded = d.get("downloaded_bytes", 0) / (1024 * 1024)
        total = d.get("total_bytes", 0) or d.get("total_bytes_estimate", 0)
        total_mb = total / (1024 * 1024)
        speed = d.get("speed", 0) or 0
        speed_mb = speed / (1024 * 1024)

        if total_mb:
            percent = (downloaded / total_mb) * 100
            bar = "#" * int(percent // 2) + "-" * (50 - int(percent // 2))
            print(f"[{bar}] {percent:.2f}% - Speed: {speed_mb:.2f} MB/s")

        else:
            print(f"[{'-' * 50}] 0.00% - Speed: 0.00 MB/s")

    elif d["status"] == "finished":
        print("Download completed!!")


if __name__ == "__main__":
    url = input("enter video link / url(tiktok , facebook, youtube): ").strip()
    name = input("enter output name (without extension): ").strip()
    download_video(url, name)