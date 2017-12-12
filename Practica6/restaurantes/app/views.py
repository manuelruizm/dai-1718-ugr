from django.shortcuts import render, HttpResponse
from .models import restaurantes

# Create your views here.

def index(request):
	return render(request, 'index.html')

def contacto(request):
	return render(request, 'contacto.html')

def error404(request):
	return render(request, 'error404.html')
