from django import forms
from django.contrib import auth

class SearchForm(forms.Form):
	term = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Zadejte hledaný výraz', 'size': '30'}))

class UploadForm(forms.Form):
	name = forms.CharField(max_length = 256)
	description = forms.CharField()
	tags = forms.CharField()
	file = forms.FileField()

class CommentForm(forms.Form):
	comment = forms.CharField(min_length = 10)

class RegisterForm(forms.Form):
	username = forms.CharField(max_length = 30, min_length = 1)
	email = forms.EmailField()
	password = forms.CharField()
