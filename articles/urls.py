from . import views
from django.conf.urls import url

urlpatterns = [
    url(r'^$',views.home_view,name='home'),
]