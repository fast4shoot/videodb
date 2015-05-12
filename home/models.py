# -*- coding: utf-8 -*-

from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

class Tag(models.Model):
	name = models.CharField(max_length = 256, primary_key = True, verbose_name = "název")
	description = models.TextField(null = True, verbose_name = "popis")
	
	def __str__(self):
		return self.name
	
	def __unicode__(self):
		return self.name
		
	class Meta:
		verbose_name = "Tag"
		verbose_name_plural = "Tagy"

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

	user = models.ForeignKey(User, related_name = "videos", related_query_name = "video", verbose_name = "uživatel")
	name = models.CharField(max_length = 256, verbose_name = "název")
	description = models.TextField(verbose_name = "popis")
	tags = models.ManyToManyField(Tag, related_name = "videos", related_query_name = "video", verbose_name = "tagy")
	state = models.CharField(max_length = 1, choices = STATE_CHOICES, default = UPLOADED, verbose_name = "stav")
	duration = models.IntegerField(null = True, verbose_name = "trvání")
	datetime = models.DateTimeField(auto_now_add = True, verbose_name = "datum nahrání")
	
	def get_video_url(self):
		return settings.MEDIA_URL + "%d.webm" % self.id
	
	def get_thumbnail_urls(self):
		return [settings.MEDIA_URL + "{0}.{1}.jpg".format(self.id, i) for i in range(3)]
	
	def is_processed(self):
		return self.state == Video.PROCESSED
	
	def has_thumbnails(self):
		return self.state == Video.PREPROCESSED or self.state == Video.PROCESSED
	
	def __str__(self):
		return self.name
	
	def __unicode__(self):
		return self.name
	
	class Meta:
		verbose_name = "Video"
		verbose_name_plural = "Videa"
		ordering = ["-datetime"]


class Comment(models.Model):
	user = models.ForeignKey(User, related_name = "comments", related_query_name = "comment", verbose_name = "uživatel")
	video = models.ForeignKey(Video, related_name = "comments", related_query_name = "comment", verbose_name = "video")
	text = models.TextField(verbose_name = "komentář")
	datetime = models.DateTimeField(auto_now_add = True, verbose_name = "datum")
	
	class Meta:
		verbose_name = "Komentář"
		verbose_name_plural = "Komentáře"
		ordering = ["-datetime"]
