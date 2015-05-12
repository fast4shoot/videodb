# -*- coding: utf-8 -*-

from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

class Tag(models.Model):
	name = models.CharField(max_length = 256, primary_key = True)
	description = models.TextField(null = True)
	
	def __str__(self):
		return self.name

class Video(models.Model):
	UPLOADED = "0"
	PREPROCESSED = "R"
	PROCESSED = "P"
	PROCESSING_ERROR = "E"
	STATE_CHOICES = (
		(UPLOADED, "Čeká na zpracování"),
		(PREPROCESSED, "Zpracovává se"),
		(PROCESSED, "Zpracováno"),
		(PROCESSING_ERROR, "Chyba zpracování"),
	)

	user = models.ForeignKey(User, related_name = "videos", related_query_name = "video")
	name = models.CharField(max_length = 256)
	description = models.TextField()
	tags = models.ManyToManyField(Tag, related_name = "videos", related_query_name = "video")
	upvotes = models.IntegerField(default = 0)
	state = models.CharField(max_length = 1, choices = STATE_CHOICES, default = UPLOADED)
	duration = models.IntegerField(null = True)
	datetime = models.DateTimeField(auto_now_add = True)
	
	def get_video_url(self):
		return settings.MEDIA_URL + "%d.webm" % self.id
	
	def get_thumbnail_urls(self):
		return [settings.MEDIA_URL + "{0}.{1}.jpg".format(self.id, i) for i in range(3)]
	
	def is_processed(self):
		return self.state == Video.PROCESSED
	
	def has_thumbnails(self):
		return self.state == Video.PREPROCESSED or self.state == Video.PROCESSED


class Comment(models.Model):
	user = models.ForeignKey(User, related_name = "comments", related_query_name = "comment")
	video = models.ForeignKey(Video, related_name = "comments", related_query_name = "comment")
	text = models.TextField()
	upvotes = models.IntegerField(default = 0)
	datetime = models.DateTimeField(auto_now_add = True)
