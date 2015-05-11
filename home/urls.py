from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^search$', views.search, name='search'),
    url(r'^upload$', views.upload, name='upload'),
    url(r'^video/(?P<video_id>[0-9]+)$', views.upload, name='upload'),
]
