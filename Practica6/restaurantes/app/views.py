from django.shortcuts import render, HttpResponse, redirect, HttpResponseRedirect
from .models import restaurantes
from .form import *
from bson.json_util import dumps

# Create your views here.

def index(request):
	return render(request, 'index.html')

def contacto(request):
	return render(request, 'contacto.html')

def registro(request):
	if(request.method == 'POST'):
		return render(request, 'index.html')

	return HttpResponseRedirect('/accounts/register')

def iniciarsesion(request):
	if(request.method == 'POST'):
		context = {'logged': True}
		return render(request, 'index.html', context)

	return HttpResponseRedirect('/accounts/login')

def busqueda(request):
	accesoconget = True
	query = []
	barrio = []
	if(request.method=='POST'):
		accesoconget = False
		# return render_template('busqueda.html', value=query, param=request.form['buscar'])
		form = formRest(request)
		if(form.is_valid()):
			barrio = form.cleaned_data['barrio']
		query = restaurantes.find({ 'borough' : barrio}).limit(10)
	else:
		print("Con el Get")

	context = {
		'form': formRest(request),
		'accesoconget': accesoconget,
		'value': query,
		'param': barrio,
	}
	return render(request, 'busqueda.html', context)

def busqueda_ajax(request):
	barrio = request.GET.get('param', None)
	pagina_py = int(request.GET.get('pagina_py', 1))-1
	query = restaurantes.find({ 'borough' : barrio}).skip(pagina_py*10).limit(10)
	data = dumps(query)
	return HttpResponse(data, content_type='json')

def logout(request):
	context = {'logged': False}
	return render(request, 'index.html', context)

def formRest(request):
	if request.method == 'POST':
		form = RestauranteForms(request.POST)
	else:
		form = RestauranteForms()
	return form
	# return RestauranteForms()
