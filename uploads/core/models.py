from __future__ import unicode_literals

from django.db import models
from django.core.files.uploadedfile import InMemoryUploadedFile
from pydub import AudioSegment
import os, sys

class Document(models.Model):
    description = models.CharField(max_length=255, blank=True)
    document = models.FileField(upload_to='documents/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.id:
            self.document = self.compressAudio(self.document)
        super(Document, self).save(*args, **kwargs)   

    def compressAudio(self,document):
    	raw_audio = AudioSegment.from_file(document, format="raw", frame_rate=44100, channels=2, sample_width=2)
        #imageTemproary = Image.open(uploadedImage)
        outputIoStream = raw_audio.export("audio2.mp3", format="mp3")

        print(outputIoStream,raw_audio,document)
        #outputIoStream = BytesIO()
        #imageTemproaryResized = imageTemproary.resize( (1020,573) ) 
        #imageTemproary.save(outputIoStream , format='mp3')
        #outputIoStream.seek(0)
        #document = InMemoryUploadedFile(outputIoStream,'FileField',"audio1.mp3" 'audio/mp3', sys.getsizeof(outputIoStream), None)
        return document

    def get_size(self):
      	return self.document.size

    def __str__(self):
      	return self.description


