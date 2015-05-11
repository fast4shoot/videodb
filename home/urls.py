from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^search$', views.search, name='search'),
    url(r'^upload$', views.upload, name='upload'),
    url(r'^video/(?P<video_id>[0-9]+)$', views.video, name='video'),
    url(r'^tag/(?P<tag_name>.+)$', views.tag, name='tag'),
    url(r'^login$', views.search, name='search'),
    url(r'^register$', views.upload, name='upload'),
]
