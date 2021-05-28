from django.shortcuts import render

# Create your views here.
def sreejithPage(request):
	"""Rendering Sreejith's page"""
	return render(request, 'sreejith.html')
