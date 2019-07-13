from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
from django.conf import settings
from django.http import HttpResponse
import xml.etree.cElementTree as ET

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'uploads.settings')

app = Celery('uploads')
app.config_from_object('django.conf:settings', namespace='CELERY') #, namespace='CELERY'
app.autodiscover_tasks()


@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))

@app.task(bind=True)
def write_xml(name, *args, **kwargs):

	print(args)#<type 'tuple'>
	print(type(name)) # <class 'uploads.celery.write_xml'>

	path = args[0].encode('utf8')
	filename = args[1].encode('utf8')

	root = ET.Element("Response")
	ET.SubElement(root, "Say", voice="alice").text = "Thanks for trying our documentation. Enjoy!"
	ET.SubElement(root, "Play").text="http://127.0.0.1:8000/"+path
	tree = ET.ElementTree(root)

	save_path = os.path.join(settings.MEDIA_ROOT, 'documents/')
	print(save_path)
	tree.write(save_path+filename+".xml")

	print("Celery is working!! {} have implemented it correctly.".format("shekhar"))

	#return HttpResponse('document saved successfully')

	
