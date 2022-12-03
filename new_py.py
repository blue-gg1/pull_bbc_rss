import os
import re
import requests

# Constants
PODCAST_RSS_URL = "https://podcast.voice.api.bbci.co.uk/rss/audio/p002vsmz?api_key=Wbek5zSqxz0Hk1blo5IBqbd9SCWIfNbT"
AUDIO_FILE_REGEX = re.compile(r"https://open.*[mp3]")

while True:
    # Download the podcast's RSS feed
    try:
        response = requests.get(PODCAST_RSS_URL)
        response.raise_for_status()
    except requests.exceptions.RequestException as error:
        print(f"Error downloading RSS feed: {error}")
        break

    # Extract the URLs of the audio files from the RSS feed
    matches = AUDIO_FILE_REGEX.findall(response.text)
    if not matches:
        print("No audio files found in RSS feed")
        break

    # Download the audio files
    for url in matches:
        try:
            response = requests.get(url, stream=True)
            response.raise_for_status()
        except requests.exceptions.RequestException as error:
            print(f"Error downloading audio file: {error}")
            continue

        # Save the audio file with the original file name
        file_name = response.headers["Content-Disposition"].split("=")[1]
        with open(file_name, "wb") as file:
            for chunk in response.iter_content(chunk_size=8192):
                file.write(chunk)

    # Wait for a minute before downloading the next set of audio files
    time.sleep(60)
