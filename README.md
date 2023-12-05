# YouTube Video Downloader

This Python script allows you to download YouTube videos using the 'pytube' library.

## Prerequisites

Before running the script, make sure you have Python 3 installed. 
You can install 'pytube' using pip:

pip3 install pytube

### Usage / How to run the script

1. clone the repository using:
   
    git clone https://github.com/matsjfunke/youtube_video_downloader.git


2. in ytDownloader.py change line 25 to save the video in desired directory:
    
    stream.download('/path/to/storage/dircetory')


3. termianl into project directory:
    
    cd youtube_video_downloader


4. Run the script in terminal and input the url of the youtube video:
    
    python3 ytDownloader.py "<YouTube_URL>"