from django.shortcuts import render, HttpResponse
from .models import restaurantes

# Create your views here.

def index(request):
	context = {}
	return render(request, 'index.html', context)

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
	# session['acceso-con-get']=True
	# client = MongoClient('localhost', 27017)
	# db = client['test']
	# restaurants = db.restaurants
	# if(request.method=='POST'):
	# 	session['acceso-con-get']=False
	# 	query = restaurants.find({ 'borough' : request.form['buscar']}).limit(10)
	# 	return render_template('busqueda.html', value=query, param=request.form['buscar'])
    #
    # # return render_template('restaurants.html', value=query)
	# else:
	# 	return render_template('busqueda.html', value="null")
	return render(request, 'busqueda.html')
