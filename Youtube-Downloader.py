

# by Mahdyar Saffari
# https://github.com/users/MahdyarSaffari/

# modules
import os
from pytube import YouTube

# screen cleaner
def clear():
    os.system('cls')

# YouTube downloader core 
def Download(link, quality):
    url = YouTube(link)
    if quality == 'high':
        video = url.streams.get_highest_resolution()
    elif quality == 'low':
        video = url.streams.get_lowest_resolution()
    elif quality == 'audio':
        video = url.streams.get_audio_only()
    print("Downloading the video ...")
    video.download()
    clear()
    print("video have been downloaded.")
    
    
# main menu
def main():
    clear()
    video_link = str(input("Youtube video link: "))
    print("\n--- Download Types ---\n(high) download high quality video\n(low) download low quality video\n(audio) download only audio file\n")
    dl_type = str(input("Download type: ").lower())
    Download(video_link, dl_type)
    
if __name__ == "__main__":
    main()