from __future__ import unicode_literals

from django.db import models
from django.core.files.uploadedfile import InMemoryUploadedFile
from pydub import AudioSegment
import os, sys
from django.conf import settings

class Document(models.Model):
    description = models.CharField(max_length=255, blank=True)
    document = models.FileField(upload_to='documents/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.id:
            self.document = self.compressAudio(self.document)
        super(Document, self).save(*args, **kwargs)   

    def compressAudio(self,document):
    	#import ipdb;ipdb.set_trace()
    	raw_audio = AudioSegment.from_file(document, format="raw", frame_rate=44100, channels=2, sample_width=2)
        #imageTemproary = Image.open(uploadedImage)
        name = document.name.split(".")[0].encode()
        ext = document.name.split(".")[1].encode()

        save_path = os.path.join(settings.MEDIA_ROOT, 'documents/')
        outputIoStream = raw_audio.export(save_path+name+"."+ext, format=ext)

        print(outputIoStream,raw_audio,document)
        outputIoStream.seek(0)

        #<open file u'/home/shekhar/workspace/cloned/simple-file-upload/media/documents/file_example_WAV_2MG', mode 'wb+' at 0x7f343d1a0f60>

        #outputIoStream = BytesIO()
        #imageTemproaryResized = imageTemproary.resize( (1020,573) ) 
        #imageTemproary.save(outputIoStream , format='mp3')
        #outputIoStream.seek(0)
        #document = InMemoryUploadedFile(outputIoStream,'FileField',"audio1.mp3" 'audio/mp3', sys.getsizeof(outputIoStream), None)

        # save_path = os.path.join(settings.MEDIA_ROOT, 'documents', outputIoStream)
        # path = default_storage.save(save_path, outputIoStream)
        return outputIoStream.read()


    def get_size(self):
      	return self.document.size

    def __str__(self):
      	return self.description


