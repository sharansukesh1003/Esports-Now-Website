from django.core import paginator
from django.shortcuts import get_object_or_404, render
from django.views.generic.base import TemplateView
from .models import HomePageArtcile,HomePageCarousel
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.core.paginator import Paginator

# def home_view(request):
#     article = HomePageArtcile.objects.filter(category__icontains= 'general')
#     paginator = Paginator(article, 5)
#     carousel = HomePageCarousel.objects.all()[:3]
#     context = {'heading_1':'Top Stories','articles': article, 'carousel_data': carousel,'heading_2':'Featured'}
#     return render(request,'home.html',context=context)

class HomeView(ListView):
    model = HomePageArtcile
    context_object_name = 'articles'
    queryset = HomePageArtcile.objects.filter(category__icontains= 'general')
    paginate_by = 5
    template_name = 'home.html'
    carousel = HomePageCarousel.objects.all()[:3]
    extra_context = {'heading_1':'Top Stories','carousel_data': carousel,'heading_2':'Featured'}

class ArticleDetailView(DetailView):
    model = HomePageArtcile
    context_object_name = 'detail_article_view'
    template_name = 'detail.html'

class ValorantArticleView(ListView):
    model = HomePageArtcile
    queryset = HomePageArtcile.objects.filter(category__icontains = 'valorant')
    paginate_by = 5
    context_object_name = 'article_list'
    template_name = 'listview.html'
    extra_context={'title': 'Valorant'}
        
class CsgoArticleView(ListView):
    model = HomePageArtcile
    queryset = HomePageArtcile.objects.filter(category__icontains = 'csgo')
    paginate_by = 5
    context_object_name = 'article_list'
    template_name = 'listview.html'
    extra_context={'title': 'CS GO'}
        
class MobileEsportsArticleView(ListView):
    model = HomePageArtcile
    queryset = HomePageArtcile.objects.filter(category__icontains = 'mobile esports')
    paginate_by = 5
    context_object_name = 'article_list'
    template_name = 'listview.html'
    extra_context={'title': 'Mobile Esports'}

class AboutView(TemplateView):
    template_name = 'about.html'

class ContactView(TemplateView):
    template_name = 'contact.html'

class CarrerView(TemplateView):
    template_name = 'carrer.html'
