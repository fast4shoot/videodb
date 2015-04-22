from django.shortcuts import render
from django.http import HttpResponse
from . import models

def index(request):
	video_list = models.Video.objects.order_by("-upvotes")[:10]
	context = {
		"video_list" : video_list,
	}
	return render(request, "home/index.html", context)
