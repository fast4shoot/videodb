from django.shortcuts import render
from django.http import HttpResponse
from . import models
from . import forms

def index(request):
	video_list = models.Video.objects.order_by("-upvotes")[:10]
	context = {"video_list": video_list,}
	return render(request, "home/index.html", context)

def search(request):
	# najít výsledky a zobrazit
	return render(request, "home/search.html", {})

def upload(request):
	if request.method == "POST":
		# provést upload zde
		pass
	else:
		uploadform = forms.UploadForm(request.POST)
		context = {"uploadform": uploadform}
		return render(request, "home/upload.html", context)

def video(request, video_id):
	commentform = forms.CommentForm()
	# vytáhnout video
	context = {
		"commentform": commentform,
	}
	return render(request, "home/video.html", commentform)
