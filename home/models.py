from django.db import models
from django.contrib.auth.models import User

class Tag(models.Model):
	name = models.CharField(max_length = 256)
	description = models.TextField()

class Video(models.Model):
	user = models.ForeignKey(User, related_name = "videos", related_query_name = "video")
	name = models.CharField(max_length = 256)
	description = models.TextField()
	file = models.FileField()
	thumbnail = models.FileField()
	tags = models.ManyToManyField(Tag, related_name = "videos", related_query_name = "video")
	upvotes = models.IntegerField(default = 0)

class Comment(models.Model):
	user = models.ForeignKey(User, related_name = "comments", related_query_name = "comment")
	video = models.ForeignKey(Video, related_name = "comments", related_query_name = "comment")
	text = models.TextField()
	upvotes = models.IntegerField(default = 0)
