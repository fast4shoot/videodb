# -*- coding: utf-8 -*-

from django.conf.urls import url
from . import views

urlpatterns = [
	#url(r'^$', views.index, name='index'),
	url(r'^search$', views.search, name='search'),
	url(r'^upload$', views.upload, name='upload'),
	url(r'^video/(?P<video_id>[0-9]+)$', views.video, name='video'),
	url(r'^video/(?P<video_id>[0-9]+)/post_comment$', views.post_comment, name='post_comment'),
	url(r'^video/(?P<video_id>[0-9]+)/edit$', views.edit_video, name='edit_video'),
	url(r'^tags$', views.tags, name='tags'),
	url(r'^tag/(?P<tag_name>.+)$', views.tag, name='tag'),
	url(r'^profile/(?P<user_id>[0-9]+)$', views.profile, name='profile'),
	url(r'^register$', views.register, name='register'),
]
