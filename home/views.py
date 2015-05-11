from django.shortcuts import render
from django.http import HttpResponse
from . import models
from . import forms

def index(request):
	video_list = models.Video.objects.order_by("-upvotes")[:10]
	context = {"video_list": video_list,}
	return render(request, "home/index.html", context)

def search(request):
	searchform = forms.SearchForm(request.GET)
	if searchform.is_valid():
		term = searchform.cleaned_data['term']
		video_list = models.Video.objects.get(name__icontains = term)
		context = {"video_list": video_list}
	else:
		context = {}
	
	return render(request, "home/search.html", context)

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
