from __future__ import unicode_literals

from django.db import models
# from django.core.files.uploadedfile import InMemoryUploadedFile
# from django.core.files import File
# from pydub import AudioSegment
import os, sys
from django.conf import settings

class Document(models.Model):
    description = models.CharField(max_length=255, blank=True)
    document = models.FileField(upload_to='documents/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    # def save(self, *args, **kwargs):
    #     if not self.id:
    #         self.document = self.compressAudio(self.document)
    #     super(Document, self).save(*args, **kwargs)   

    # def compressAudio(self,document):
    # 	#import ipdb;ipdb.set_trace()
    # 	raw_audio = AudioSegment.from_file(document, format="raw", frame_rate=44100, channels=2, sample_width=2)
        
    #     name = document.name.split(".")[0].encode()
    #     ext = document.name.split(".")[1].encode()

    #     save_path = os.path.join(settings.MEDIA_ROOT, 'documents/')
    #     import ipdb;ipdb.set_trace()
    #     os.chdir(save_path)
    #     outputIoStream = raw_audio.export(name+"a"+"."+ext, format=ext)

    #     #print(outputIoStream,raw_audio,document,outputIoStream.name+"-------------"+save_path+name+"."+ext)
    #     #outputIoStream.seek(0)
    #     import ipdb;ipdb.set_trace()
        
    #     filename = name+"."+ext

    #     document.save(filename, File(outputIoStream))
        
    #     print(document+"-------------")

    #     #<open file u'/home/shekhar/workspace/cloned/simple-file-upload/media/documents/file_example_WAV_2MG', mode 'wb+' at 0x7f343d1a0f60>      
    #     #document = InMemoryUploadedFile(outputIoStream,'FileField',"audio1.mp3" 'audio/mp3', sys.getsizeof(outputIoStream), None)

    #     return document

    def get_size(self):
      	return self.document.size

    def __str__(self):
      	return self.description


