from django.db import models
from django.contrib.auth.models import User

class Tag(models.Model):
	name = models.CharField(max_length = 256)
	description = models.TextField()

class Video(models.Model):
	name = models.CharField(max_length = 256)
	description = models.TextField()
	file = models.FileField()
	thumbnail = models.FileField()
	tags = models.ManyToManyField(Tag, related_name = "videos", related_query_name = "video")
	upvotes = models.IntegerField(default = 0)

class Comment(models.Model):
	user = models.ForeignKey(User)
	text = models.TextField()
	upvotes = models.IntegerField(default = 0)
