from . import views
from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from multiurl import multiurl

urlpatterns = [
    url(r'^$',views.HomeView.as_view(),name='home'),
    url(r'^valorant/',views.ValorantArticleView.as_view(),name='valorant'),
    url(r'^csgo/',views.CsgoArticleView.as_view(),name='csgo'),
    url(r'^mobileesports/',views.MobileEsportsArticleView.as_view(),name='mobileesports'),
    url(r'^about/',views.AboutView.as_view(),name='about'),
    url(r'^carrer/',views.CarrerView.as_view(),name='carrer'),
    url(r'^contact/',views.ContactView.as_view(),name='contact'),
    url(r'^valorant/(?P<pk>[-\w]+)/$',views.ArticleDetailView.as_view(),name='valorant_detail'),
    url(r'^csgo/(?P<pk>[-\w]+)/$',views.ArticleDetailView.as_view(),name='csgo_detail'),
    url(r'^mobileesports/(?P<pk>[-\w]+)/$',views.ArticleDetailView.as_view(),name='mobile_detail'),
    url(r'^(?P<pk>[-\w]+)/$',views.ArticleDetailView.as_view(),name='detail'),
    url(r'^trending/(?P<pk>[-\w]+)/$',views.CarouselArticleDetailView.as_view(),name='detail_carousel'),
]
urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)