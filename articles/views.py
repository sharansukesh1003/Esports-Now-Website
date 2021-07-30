from django.shortcuts import render
from .models import HomePageArtcile,HomePageCarousel

def home_view(request):
    article = HomePageArtcile.objects.all()
    carousel = HomePageCarousel.objects.all()
    context = {'heading_1':'Top Stories','articles': article, 'carousel_data': carousel,'heading_2':'Featured'}
    return render(request,'home.html',context=context)