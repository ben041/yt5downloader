# yt5downloaderlink

A simple Python command-line video downloader built with [`yt-dlp`](https://github.com/yt-dlp/yt-dlp).

The script accepts a video URL, downloads the best available video and audio, attempts to merge them into an MP4 file, displays download progress, and can automatically open the downloaded video using your system's default media player.

## Features

* Download videos using `yt-dlp`
* Supports websites supported by `yt-dlp`
* Downloads the best available video and audio
* Automatically merges video and audio into MP4 when necessary
* Live download progress display
* Automatically creates the output directory
* Optional automatic video playback after downloading
* Works on Windows, macOS, and Linux
* Simple command-line interface

## Requirements

* Python 3.8+
* `yt-dlp`
* FFmpeg

### Python

Check that Python is installed:

```bash
python --version
```

or:

```bash
python3 --version
```

### Install yt-dlp

```bash
pip install yt-dlp
```

If your system uses `pip3`:

```bash
pip3 install yt-dlp
```

### Install FFmpeg

FFmpeg is recommended because some websites provide video and audio as separate streams. `yt-dlp` needs FFmpeg to merge them into a single video file.

Check whether FFmpeg is installed:

```bash
ffmpeg -version
```

If the command is not found, install FFmpeg for your operating system and make sure it is available in your system `PATH`.

## Installation

Clone the repository:

```bash
git clone https://github.com/ben041/yt5downloaderlink.git
```

Enter the project directory:

```bash
cd yt5downloaderlink
```

Install the Python dependency:

```bash
pip install yt-dlp
```

You can also install the dependencies from a `requirements.txt` file if one is included in the project:

```bash
pip install -r requirements.txt
```

## Usage

Run the script:

```bash
python your_script.py
```

On some systems:

```bash
python3 your_script.py
```

The program will ask for two values:

```text
enter video link / url(tiktok , facebook, youtube):
enter output name (without extension):
```

### Example

```text
enter video link / url(tiktok , facebook, youtube): https://example.com/video
enter output name (without extension): my_video
```

The downloaded file will be saved using the name:

```text
my_video.mp4
```

## Output

The script displays download progress in the terminal:

```text
[#########################-------------------------] 50.00% - Speed: 2.35 MB/s
```

After the download finishes:

```text
Download completed!!
Video downloaded successfully: ./my_video.mp4
```

If autoplay is enabled, the downloaded video will then be opened automatically.

## How It Works

The script has three main parts.

### 1. Video playback

The `play_video()` function detects the operating system and attempts to open the downloaded video.

* **Windows:** uses `os.startfile()`
* **macOS:** uses `open`
* **Linux/Unix:** looks for `xdg-open`, `vlc`, or `mpv`

### 2. Video downloading

The `download_video()` function uses `yt-dlp` to:

1. Create the output directory if it doesn't exist.
2. Configure the output filename.
3. Select the best available video/audio combination.
4. Download the media.
5. Merge the streams into MP4 when required.
6. Display download progress.
7. Optionally open the downloaded file.

### 3. Progress tracking

The `hook()` function receives progress information from `yt-dlp` and displays:

* Download percentage
* Download speed
* A progress bar
* Completion status

## Custom Usage

The downloader can also be imported into another Python program:

```python
from downloader import download_video

result = download_video(
    "https://example.com/video",
    output_name="my_video",
    output_dir="downloads",
    autoplay=False
)

print(result["title"])
print(result["filepath"])
```

The function returns a dictionary containing information about the downloaded video:

```python
{
    "title": "...",
    "ext": "mp4",
    "filepath": "/path/to/video.mp4"
}
```

> Replace `downloader` with the actual Python filename containing the functions.

## Supported Websites

This project uses `yt-dlp`, which supports a large number of websites and services.

However, website support can change over time. A URL working today does not guarantee that it will continue to work if the website changes its video delivery system or access requirements.

For the current list of supported sites, see the official `yt-dlp` documentation:

https://github.com/yt-dlp/yt-dlp/blob/master/supportedsites.md

## Troubleshooting

### `yt-dlp is not installed`

Install it with:

```bash
pip install yt-dlp
```

Then try running the script again.

### FFmpeg errors

Install FFmpeg and make sure the `ffmpeg` command works from your terminal:

```bash
ffmpeg -version
```

### The video does not download

First update `yt-dlp`:

```bash
pip install -U yt-dlp
```

Then try again.

Website changes, login requirements, geo-restrictions, age restrictions, or other access restrictions can prevent a download.

### Video downloads but does not play automatically

The script depends on a media player being available on your system.

On Linux, it checks for:

```text
xdg-open
vlc
mpv
```

You can still open the downloaded file manually if no compatible player is detected.

## Project Structure

A simple project structure can look like this:

```text
yt5downloaderlink/
│
├── downloader.py
├── README.md
└── requirements.txt
```

Your actual Python filename can be different.

## Dependencies

The main Python dependency is:

* [yt-dlp](https://github.com/yt-dlp/yt-dlp)

The project may also require:

* [FFmpeg](https://ffmpeg.org/)

## Legal and Responsible Use

This software is provided as a technical tool for downloading online media.

Users are responsible for complying with:

* Copyright laws
* The terms of service of the websites they use
* Applicable local laws and regulations
* Any restrictions associated with the content they download

Only download content that you have permission or legal rights to download.

The project does not grant users permission to download copyrighted material.

## Disclaimer

This project is not affiliated with YouTube, TikTok, Facebook, or any other website supported by `yt-dlp`.

Third-party websites may change their systems at any time, which can cause downloading to stop working until `yt-dlp` is updated.

## Contributing

Contributions are welcome.

If you find a bug or have an idea for improving the project:

1. Fork the repository.
2. Create a new branch.
3. Make your changes.
4. Test the changes.
5. Open a pull request.

For bugs, please include:

* Operating system
* Python version
* `yt-dlp` version
* FFmpeg version
* The error message
* Steps to reproduce the problem

Avoid posting private URLs, authentication tokens, cookies, or other sensitive information in issues.

## License

Choose and add a license before making the repository public.

For example, if you want a permissive open-source license, you could use the MIT License.

See GitHub's documentation on choosing an open-source license:

https://docs.github.com/en/communities/setting-up-your-project-for-open-source-contribution/adding-a-license-to-a-repository

---

**Made with Python and yt-dlp.**
