from django.shortcuts import render, redirect
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from uploads.core.models import Document
from uploads.core.forms import DocumentForm 
from django.contrib.staticfiles.templatetags.staticfiles import static
from celery.decorators import task
from .tasks import save_document_model
from uploads.celery import write_xml


def home(request):
    documents = Document.objects.all()


    return render(request, 'core/home.html', { 'documents': documents })


def simple_upload(request):
    if request.method == 'POST' and request.FILES['document']:
        myfile = request.FILES['document']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        print(filename,"-----"+myfile)
        uploaded_file_url = fs.url(filename)
        return render(request, 'core/simple_upload.html', {
            'uploaded_file_url': uploaded_file_url
        })
    return render(request, 'core/simple_upload.html')



def model_form_upload(request):
    if request.method == 'POST':
        
        form = DocumentForm(request.POST, request.FILES)
        url = settings.MEDIA_URL+'documents/'+request.FILES['document'].name
        url=url.encode('utf8')
        
        print(request.FILES,"======",type(request.FILES['document']),url.encode('utf8'))

        #(<MultiValueDict: {u'document': [<InMemoryUploadedFile: file_example_WAV_2MG.wav (audio/wav)>]}>, '======', <class 'django.core.files.uploadedfile.InMemoryUploadedFile'>, <type 'unicode'>)


        if form.is_valid():

            write_xml.delay(url,request.FILES['document'].name)

            #print(form)
            #save_document_model.delay(url, request.FILES['document'].name)
            #handle_uploaded_file(request.FILES['file'])
            form.save()
            #return render(request, 'core/home.html', { 'urls': url })
            return redirect('home')
    else:
        form = DocumentForm()
    return render(request, 'core/model_form_upload.html', {
        'form': form
    })
