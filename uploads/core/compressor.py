import os
from pydub import AudioSegment
from django.conf import settings

path ="./temp/"
os.makedirs(path)

for root, dirs, files in os.walk(settings.MEDIA_ROOT):  
    for filename in files:
    	name, ext = filename.split(".")
    	AudioSegment.from_file(filename).export(path+filename, format="mp3")
    

