from __future__ import absolute_import, unicode_literals
from celery import shared_task
from celery.decorators import task
import os
# from pydub import AudioSegment

# from django.core.files import File
# #from django.conf import DEFAULT_FILE_STORAGE as storage
# from .models import Document


@task(name = "print_msg_with_name")
def print_message(name, *args, **kwargs):
  print("Celery is working!! {} have implemented it correctly.".format(name))

# @task(name="save_document_model")
@shared_task(bind=True, max_retries=3)

def save_document_model(file_path, file_name):

	return None

    # with open(file_path, 'r') as f:
    #     file = File(f)
    #     print(file)
    #     newdoc = Document(upload=file, name=file_name)
    #     newdoc.save()

    #     #logger.info("document saved successfully")

    #     #storage.delete(file_path)
    #     print('deleted temp file') # cleanup temp file

    # return HttpResponse("document saved successfully")