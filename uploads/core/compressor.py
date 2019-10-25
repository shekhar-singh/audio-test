import os
from pydub import AudioSegment
from django.conf import settings

path ="./temp/"
os.makedirs(path)

for root, dirs, files in os.walk(settings.MEDIA_ROOT):  
    for filename in files:
    	name, ext = filename.split(".")
    	AudioSegment.from_file(filename).export(path+filename, format="mp3")
#some usefule code for image processing
response = client.text_detection(image=image)

for text in response.text_annotations:
    print('=' * 79)
    print('"{}"'.format(text.description))

    vertices = (['({},{})'.format(v.x, v.y)
                 for v in text.bounding_poly.vertices])

    print('bounds: {}'.format(','.join(vertices)))
    

