from django.http import Http404
from django.shortcuts import render
from .models import Image
from django.core.exceptions import ObjectDoesNotExist


# Create your views here.
def index(request):
    image = Image.objects.all()
    return render(request, 'index.html', {"image": image})

def home(request):
    image = Image.objects.all()
    return render(request, 'home.html', {"image": image})


def search(request):
    if 'image' in request.GET and request.GET['image']:
        searchname = request.GET.get('image')
        searchimage= Image.search_by_img_name(searchname)
        message = f"{searchname}"

        return render(request, 'search.html', {"message": message, "image": searchimage})
    else:
        message ="You havent searched any images "
        return render(request, 'search.html',{"message": message})






