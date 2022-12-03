import requests
import re
import time
import os

# Constants
PODCAST_RSS_URL = "https://podcast.voice.api.bbci.co.uk/rss/audio/p002vsmz?api_key=Wbek5zSqxz0Hk1blo5IBqbd9SCWIfNbT"
AUDIO_FILE_REGEX = re.compile(r"https://open.*[mp3]")
FILE_NAME_FORMAT = "%d-%m-%Y_%H"

# Download the podcast's RSS feed
try:
    response = requests.get(PODCAST_RSS_URL)
    response.raise_for_status()
except requests.exceptions.RequestException as error:
    print(f"Error downloading RSS feed: {error}")
    sys.exit(1)

# Extract the URL of the audio file from the RSS feed
matches = AUDIO_FILE_REGEX.findall(response.text)
if not matches:
    print("No audio files found in RSS feed")
    sys.exit(1)

# Download the audio file
try:
    response = requests.get(matches[0], stream=True)
    response.raise_for_status()
except requests.exceptions.RequestException as error:
    print(f"Error downloading audio file: {error}")
    sys.exit(1)

# Generate a filename using the current date and time
file_name = time.strftime(FILE_NAME_FORMAT)
file_path = os.path.join("/proj/rss/mp3/", file_name + ".
