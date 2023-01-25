import sys
from pytube import YouTube


STORE_PATH = '/mnt/c/Users/CFZ/Videos/misc/'
video_link = sys.argv[1]
file_name = sys.argv[2]

# TODO: Complete functions for progress and completion to display a progress bar...
def progress_func():
    pass

def complete_func():
    pass

try:
    yt = YouTube(video_link,
                #  on_progress_callback=progress_func,
                #  on_complete_callback=complete_func
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


