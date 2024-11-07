from django.shortcuts import render
from django.template import RequestContext
from flipbook.models import PdfFlipbook
from django.contrib.auth.forms import UserCreationForm

def flipbook(request):
    documents = PdfFlipbook.objects.all()
    print(documents)

    return render(
        request,
        'index.html',
        {'documents': documents}
    )

def viewer(request):
    flipbook_file = request.GET.get('file', '')
    return render(request, 'viewer.html', {'flipbook_file': flipbook_file})

