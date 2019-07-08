from uploads.core.models import Document
from django.core import serializers
from django.core.files import File


def my_xml(request):
    

    data = serializers.serialize("xml", Document.objects.all())

    #data = serializers.serialize('xml', Student.objects.filter(Q(name__startswith='A')), fields=('name','dob'))

    f = open('content.xml', 'w')
    myfile = File(f)
    myfile.write(data)
    myfile.close()
