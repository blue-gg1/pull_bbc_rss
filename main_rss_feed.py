import requests
import sys
import re
from datetime import datetime
import os

now = datetime.now()
dt_string = now.strftime("%d-%m-%Y_%H")
print(dt_string)



feedurl = "https://podcast.voice.api.bbci.co.uk/rss/audio/p002vsmz?api_key=Wbek5zSqxz0Hk1blo5IBqbd9SCWIfNbT"
bbccontent = requests.get(feedurl)
locationmp3 = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\), ]|(?:%[0-9a-fA-F][0-9a-fA-F]))+' ,bbccontent.text)[6]
print(locationmp3)

empethree = requests.get(locationmp3)
print("done downloading")


with open('/proj/rss/mp3/'+dt_string+'.mp3','wb') as f:
    f.write(empethree.content) 
