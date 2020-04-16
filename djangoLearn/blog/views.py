from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home(request):
	return HttpResponse("""
		<h1>c'est mon project djengoLearn</h1><br />
		<p>je c'est pas encore quoi dire exactement</p>	
	""")
