# Import the necessary libraries
from pytube import YouTube
import sys

# Check for the correct number of command-line arguments
if len(sys.argv) != 2:
    print("Usage: python3 ytDownloader.py <YouTube_URL>")
    sys.exit(1)

# Get the YouTube URL from the command-line argument
link = sys.argv[1]

try:
    # Create a YouTube object
    yt = YouTube(link)

    # Video information
    print("Title: ", yt.title)
    print("Views: ", yt.views)
    print(f"Length: {yt.length} min")

    # Download the video in the highest resolution
    stream = yt.streams.get_highest_resolution()
    print("Downloading video...")
    stream.download('/path/to/storage/dircetory')
    print("Video downloaded successfully.")

#check for error
except Exception as e:
    print("An error occurred:", str(e))