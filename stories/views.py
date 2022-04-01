from django.shortcuts import render
from .models import Image

# Create your views here.
def index(request):
    image = Image.objects.all()
    return render(request, 'index.html', {"image": image})

def home(request):
    return render(request, 'home.html')