# -*- coding: utf-8 -*-

from django.db.models import Count
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.contrib import messages, auth
from django.conf import settings
from django.contrib.auth.decorators import login_required
from . import models
from . import forms
from . import utils
import subprocess
import os
import threading
import json

def index(request):
	videos = models.Video.objects.filter(state = models.Video.PROCESSED).order_by("-datetime")
	context = {"videos": videos,}
	return render(request, "home/index.html", context)

def search(request):
	searchform = forms.SearchForm(request.GET)
	if searchform.is_valid():
		term = searchform.cleaned_data['term']
		videos = models.Video.objects.filter(name__icontains = term)
		context = {"videos": videos}
	else:
		context = {}
	
	return render(request, "home/search.html", context)

@login_required
def upload(request):
	if request.method == "POST":
		uploadform = forms.UploadForm(request.POST, request.FILES)
		if uploadform.is_valid():
			# provést upload zde
			name = uploadform.cleaned_data['name']
			description = uploadform.cleaned_data['description']
			tags = uploadform.cleaned_data['tags']
			file = uploadform.cleaned_data['file']
			
			video = models.Video (
				user = request.user,
				name = name,
				description = description
			)
			
			video.save()
			
			for tagname in tags.split():
				tags = models.Tag.objects.filter(name = tagname)
				if tags:
					video.tags.add(tags[0])
				else:
					tag = models.Tag.objects.create (name = tagname)
					video.tags.add(tag)
			
			video.save()
			
			uploadedpath = file.temporary_file_path()
			temporarycopy = utils.create_temporary_copy(uploadedpath)
			
			messages.info(request, "Video nahráno, zpracovávám.")
			process_thread = threading.Thread(target = process_video, args = (temporarycopy, video.id))
			process_thread.start()
		else:
			context = {"uploadform": uploadform}
			return render(request, "home/upload.html", context)
	
	uploadform = forms.UploadForm()
	context = {"uploadform": uploadform}
	return render(request, "home/upload.html", context)

def video(request, video_id):
	video = get_object_or_404(models.Video, id = video_id)
	commentform = None
	if request.method == "POST": # kontrolovat prihlasenost uzivatele
		commentform = forms.CommentForm(request.POST)
		if commentform.is_valid():
			text = commentform.cleaned_data['comment']
			comment = models.Comment(text = text, user = request.user)
			video.comments.add(comment)
			comment.save()
			return redirect('video', video_id = video_id)
	else:
		commentform = forms.CommentForm()
		
	context = {
		"video": video,
		"comments": video.comments.order_by("-datetime"),
		"tags": video.tags.all(),
		"commentform": commentform,
	}
	return render(request, "home/video.html", context)

def tags(request):
	top_tags = models.Tag.objects.annotate(num_videos = Count("video")).order_by("-num_videos")[:50]
	context = {
		"top_tags": top_tags,
	}
	return render(request, "home/tags.html", context)

def tag(request, tag_name):
	tag = get_object_or_404(models.Tag, name = tag_name)
	context = {
		"tag": tag,
		"videos": tag.videos.filter(state = models.Video.PROCESSED).order_by("-datetime"),
	}
	return render(request, "home/tag.html", context)

def profile(request, user_id):
	user = get_object_or_404(auth.models.User, pk = user_id)
	context = {
		"profile": user,
		"videos": user.videos.order_by("-datetime"),
		"comments": user.comments.order_by("-datetime")[:50]
	}
	return render(request, "home/profile.html", context)

def register(request):
	registerform = None
	if request.method == "POST":
		registerform = forms.RegisterForm(request.POST)
		if registerform.is_valid():
			username = registerform.cleaned_data["username"]
			password = registerform.cleaned_data["password"]
			email = registerform.cleaned_data["email"]
			
			auth.models.User.objects.create_user(username, email, password)
			user = auth.authenticate(username = username, password = password)
			auth.login(request, user)
			messages.info(request, "Uživatelský účet byl vytvořen.")
			return redirect('index')
	else:
		registerform = forms.RegisterForm()
	
	return render(request, "registration/register.html", {"form": registerform})

def process_video(path, video_id):
	try:
		print("Startujeme: ", path)
		
		probe_out = subprocess.check_output(["ffprobe", path, "-show_format", "-print_format", "json"]).decode("utf-8")
		probe_json = json.loads(probe_out)
		duration = int(float(probe_json["format"]["duration"]))
		
		finalpath = os.path.join(settings.MEDIA_ROOT, "%d.webm" % video_id)
		
		for i in range(3):
			tpath = os.path.join(settings.MEDIA_ROOT, "{0}.{1}.jpg".format(video_id, i))
			subprocess.check_call(["ffmpeg", "-i", path, "-ss", str((i + 1) * duration / 4), "-vf", "scale=-1:150", "-vframes", "1", tpath])
		
		set_video_state(video_id, models.Video.PREPROCESSED, duration)
		
		finalpath = os.path.join(settings.MEDIA_ROOT, "%d.webm" % video_id)
		subprocess.check_call(["ffmpeg", "-i", path, "-acodec", "vorbis", "-aq", "10", "-ac", "2", "-qmax", "10", finalpath])
		os.remove(path)
		
		set_video_state(video_id, models.Video.PROCESSED)
		
		print("Končíme: ", path)
		
	except subprocess.CalledProcessError:
		set_video_state(video_id, models.Video.PROCESSING_ERROR)
		print ("Skončili jsme s chybou: ", path)

def set_video_state(video_id, state, duration = None):
	video = models.Video.objects.get(id = video_id)
	video.state = state
	if duration != None:
		video.duration = duration
	video.save()
