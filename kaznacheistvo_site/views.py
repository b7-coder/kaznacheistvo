from django.shortcuts import render
from .models import *
# Create your views here.

def index(request):
    print('test')
    return render(request, 'kaznacheistvo_site/main.html')



def news(request):

    rows = News.objects.all()
    
    context = {
        'news': rows
    }

    return render(request, 'kaznacheistvo_site/news.html', context)


def newsDetails(request, id):

    mainNews = News.objects.get(id=id) # новость

    details = NewsDetails.objects.all().filter(newsObject__id=id)# множество текстов новостя
    images = NewsImages.objects.all().filter(newsObject__id=id) # множество картинок новостя

    context = {
        'mainNews': mainNews,
        'images':images,
        'details': details,
    }

    return render(request, 'kaznacheistvo_site/newsDetails.html', context)