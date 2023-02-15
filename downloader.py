import sys
import os
from dotenv import load_dotenv
from pytube import YouTube

load_dotenv()

STORE_PATH = os.getenv('VIDEO_STORE_PATH')

def progress_func(stream, bytes, bytes_remaining):
    total = stream.filesize
    downloaded = total - bytes_remaining
    completed = int(downloaded / total * 100)
    end = '\r' if completed < 100 else '\n'
    print(f"Downloading... [{'#' * completed}{'.' * (100 - completed)}] {completed}%", end=end)

def download_video(video_link: str, file_name: str) -> None:
    try:
        yt = YouTube(video_link,
                     on_progress_callback=progress_func,
                    )
    except:
        print('Connection Error')
        
    video = yt.streams.filter(file_extension='mp4').get_highest_resolution()

    try: 
        # downloading the video 
        video.download(STORE_PATH, f'{file_name}.mp4') 
    except Exception as e: 
        print("There was an error downloading the video!", e) 
    print('Download completed successfully!')

def main() -> None:
    video_link = sys.argv[1]
    file_name = sys.argv[2]
    download_video(video_link, file_name)

if __name__ == '__main__':
    main()


