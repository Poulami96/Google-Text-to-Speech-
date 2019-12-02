from gtts import gTTS

import os

import json
from pprint import pprint

with open('/media/poulami/Storage/Old_System/Data.json') as data_file:
    data = json.load(data_file)

data=str(data)

language = 'en'

myobj = gTTS(text=data, lang=language, slow=False)


myobj.save("appropriate_data.mp3")

