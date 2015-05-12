# -*- coding: utf-8 -*-

from django import forms
from django.contrib import auth

class SearchForm(forms.Form):
	term = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Zadejte hledaný výraz', 'size': '30'}))

class UploadForm(forms.Form):
	name = forms.CharField(max_length = 256, label='Název videa')
	description = forms.CharField(widget=forms.Textarea(attrs={'rows': '6', 'cols': '60'}), label='Popis videa')
	tags = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'jednotlivé tagy oddělujte mezerou', 'size': '30'}), label='Tagy')
	file = forms.FileField(label='Video')

class CommentForm(forms.Form):
	comment = forms.CharField(label='',widget=forms.Textarea(attrs={'rows': '4', 'style': 'width: 100%'}), min_length = 2)

class RegisterForm(forms.Form):
	username = forms.CharField(max_length = 30, min_length = 1)
	email = forms.EmailField()
	password = forms.CharField()
