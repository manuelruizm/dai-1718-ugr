from django.shortcuts import render, HttpResponse
from .models import restaurantes

# Create your views here.

def index(request):
	return render(request, 'index.html')

def contacto(request):
	return render(request, 'contacto.html')

def registro(request):
	if(request.method == 'POST'):
		db = shelve.open('datos.dat')
		user = request.form['nombre']
		password = request.form['contraseña']

		db[user] = {'Username': user, 'Password': password}
		db.close()
		return render(request, 'index.html')

	return render(request, 'registrarse.html')
