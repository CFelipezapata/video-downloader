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
                 on_progress_callback=progress_func,
                 on_complete_callback=complete_func)
except:
    print('Connection Error')
    
mp4_files = yt.streams.filter(file_extension='mp4')

yt.title(file_name)

d_video = yt.get(mp4_files[-1].extension,mp4_files[-1].resolution)

try: 
    # downloading the video 
    d_video.download(STORE_PATH) 
except: 
    print("There was an error downloading the video!") 
print('Download completed successfully!') 


