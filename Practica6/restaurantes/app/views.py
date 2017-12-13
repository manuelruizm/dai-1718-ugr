from django.shortcuts import render, HttpResponse
from .models import restaurantes
from .form import *
from bson.json_util import dumps

# Create your views here.

def index(request):
	return render(request, 'index.html')

def contacto(request):
	return render(request, 'contacto.html')

def registro(request):
	# if(request.method == 'POST'):
	# 	db = shelve.open('datos.dat')
	# 	user = request.form['nombre']
	# 	password = request.form['contraseña']
    #
	# 	db[user] = {'Username': user, 'Password': password}
	# 	db.close()
	# 	return render(request, 'index.html')

	return render(request, 'registrarse.html')

def iniciarsesion(request):
	# Si se pide con un GET se da la página tal cual.
	# if(request.method == 'POST'):
	# 	db = shelve.open('datos.dat')
	# 	user = db.get(request.form['nombreid'], None)
	# 	if(user!=None):
	# 		user = user['Username']
	# 	password = request.form['contraseñaid']
    #
	# 	if(password == db[user]['Password']):
	# 		session['logged'] = True
	# 		session['username'] = user
	# 	else:
	# 		session['logged'] = False
	# 	db.close()
	# 	return redirect(url_for('index'))

	return render(request, 'iniciarsesion.html')

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

def formRest(request):
	if request.method == 'POST':
		form = RestauranteForms(request.POST)
	else:
		form = RestauranteForms()
	return form
	# return RestauranteForms()
