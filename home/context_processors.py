from . import forms

def searchform(request):
	form = forms.SearchForm(request.GET)
	return {'searchform': form}
