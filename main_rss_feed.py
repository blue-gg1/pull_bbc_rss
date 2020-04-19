import requests
import sys
import re
import wget
from datetime import datetime
import os

feedurl = "https://podcast.voice.api.bbci.co.uk/rss/audio/p002vsmz?api_key=Wbek5zSqxz0Hk1blo5IBqbd9SCWIfNbT"
bbccontent = requests.get(feedurl)
locationmp3 = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\), ]|(?:%[0-9a-fA-F][0-9a-fA-F]))+' ,bbccontent.text)[6]
print(locationmp3)

# now = datetime.now()
# dt_string = now.strftime("%d-%m-%Y_%H-%M-%S")
# filename = dt_string+'.mp3'
# newname = os.path.join('/Users/bluepill/Documents/proj/rss/' , filename)
