import requests
import sys
import re
import xml.etree.ElementTree as ET

feedurl = "https://podcast.voice.api.bbci.co.uk/rss/audio/p002vsmz?api_key=Wbek5zSqxz0Hk1blo5IBqbd9SCWIfNbT"
bbccontent = requests.get(feedurl)

fullxml = bbccontent.text

#print(fullxml)

print(fullxml.find('http',0,100))
print(filter('http', fullxml))
#print(fullxml.split("url")[2])

#root = ET.parse(fullxml).getroot()
#for type_tag in root.findall('rss/channel/item/enclosure'):
#    value = type_tag.get('http')
#    print(value)
