from django.shortcuts import render
from . models import *

# Create your views here.
def image(request, page_id):
    context = ImageModel.objects.get(pk=page_id)
    print(context)
    return render(request, 'imagept/image.html', {'test': context})  

def embed(request):
    pass

def playlist(request):
    pass

def signin(request):
    pass

def signup(request):
    pass
