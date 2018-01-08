from django.shortcuts import render, HttpResponse, redirect, HttpResponseRedirect
from .models import restaurantes
from .form import *
from bson.json_util import dumps
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse

# Create your views here.

def index(request):
	return render(request, 'index.html')

def contacto(request):
	return render(request, 'contacto.html')

# def registro(request):
# 	if(request.method == 'POST'):
# 		return render(request, 'index.html')
#
# 	return HttpResponseRedirect('/accounts/register')

# @login_required
# def iniciarsesion(request):
# 	if(request.method == 'POST'):
# 		context = {'logged': True}
# 		return render(request, 'index.html', context)
#
# 	return HttpResponseRedirect('/accounts/login')

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
		'otroform': formAnadir(request),
		'otroform2': formModificar(request),
		'mapaform': formMapa(request),
	}
	return render(request, 'busqueda.html', context)

def busqueda_ajax(request):
	barrio = request.GET.get('param', None)
	pagina_py = int(request.GET.get('pagina_py', 1))-1
	query = restaurantes.find({ 'borough' : barrio}).skip(pagina_py*10).limit(10)
	data = dumps(query)
	return HttpResponse(data, content_type='json')

# def logout(request):
# 	return render(request, 'logout.html')

def anadir(request):
	if(request.method=='POST'):
		form = formAnadir(request)
		print(form)
		nombre = form.cleaned_data['nombre']
		barrio = form.cleaned_data['barrio']
		query = restaurantes.insert_one({ 'name' : nombre, 'borough' : barrio, 'cuisine' : "Casera"}).inserted_id

	return render(request, 'anadir.html')

def modificar(request):
	if(request.method=='POST'):
		form = formModificar(request)
		print(form)
		iden = form.cleaned_data['iden']
		nombre = form.cleaned_data['nombre']
		cocina = form.cleaned_data['cocina']
		restaurantes.update_one({ 'restaurant_id' : iden},
			{"$set" : {"name" : nombre,
					  "cuisine" : cocina}
			})

	return render(request, 'modificar.html')

def mapa(request):
	if(request.method=='POST'):
		form = formMapa(request)
		print(form)
		ident = form.cleaned_data['ident']
		query = restaurantes.find({ 'restaurant_id' : ident})
		rest = restaurantes.find_one({ 'restaurant_id' : ident})
		context = {
			'value' : query,
			'latitud' : rest['address']['coord'][1],
			'longitud' : rest['address']['coord'][0],
		}

	return render(request, 'mapa.html', context)

def grafica(request):
	return render(request, 'grafica.html')

def estadistica(request):
	barrios = {}

	for r in restaurantes.find({},{"borough":1, "_id":0}).sort("borough"):
		if barrios.get(r["borough"]) == None:
			barrios[r["borough"]] = 1
		else:
			barrios[r["borough"]] = barrios[r["borough"]] +1
	datosProcesados = []
	datos = []
	for r in barrios:
		datos = []
		datos.append(r)
		datos.append(barrios[r])
		datosProcesados.append(datos)

	return JsonResponse({'datosChart' : datosProcesados})

def formRest(request):
	if request.method == 'POST':
		form = RestauranteForms(request.POST)
	else:
		form = RestauranteForms()
	return form
	# return RestauranteForms()

def formAnadir(request):
	if request.method == 'POST':
		form = AnadirRestForms(request.POST)
	else:
		form = AnadirRestForms()
	return form
	# return AñadirRestForms()

def formModificar(request):
	if request.method == 'POST':
		form = ModificarForms(request.POST)
	else:
		form = ModificarForms()
	return form

def formMapa(request):
	if request.method == 'POST':
		form = MapaForms(request.POST)
	else:
		form = MapaForms()
	return form
