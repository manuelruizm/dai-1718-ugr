#------------------------------------------------------------------------------
#
#	Manuel Ruiz Maldonado
#
#	DAI - Desarrollo de Aplicaciones para Internet
#	Curso 2017-2018
#
#	Práctica 4: Soluciones
#
#------------------------------------------------------------------------------

#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from flask import Flask, render_template, session, request, redirect, url_for
from pymongo import MongoClient
from bson.json_util import dumps
import shelve

app = Flask(__name__)
app.secret_key = 'random key'

@app.route('/', methods=['GET','POST'])
def index():

	# get_access = True
    #
	# # Si se pide con un GET se da la página tal cual.
	# if(request.method == 'POST'):
	# 	get_access = False
	# session['logged'] = 'username' in session
    #
	# if(not get_access):
	# 	db = shelve.open('datos.dat')
	# 	user = db.get(request.form['nombre'], None)
	# 	if(user!=None):
	# 		user = user['Username']
	# 	password = request.form['contraseña']
    #
	# 	if(password == db[user]['Password']):
	# 		session['logged'] = True
	# 		session['username'] = user
	# 	else:
	# 		session['logged'] = False
	# 	db.close()

	return render_template('index.html')

@app.route('/iniciarsesion', methods=['GET','POST'])
def iniciarsesion():

	# get_access = True


	# Si se pide con un GET se da la página tal cual.
	if(request.method == 'POST'):
		# get_access = False



	# if(not get_access):
		db = shelve.open('datos.dat')
		user = db.get(request.form['nombreid'], None)
		if(user!=None):
			user = user['Username']
		password = request.form['contraseñaid']

		if(password == db[user]['Password']):
			session['logged'] = True
			session['username'] = user
		else:
			session['logged'] = False
		db.close()
		return redirect(url_for('index'))

	return render_template('iniciarsesion.html')

@app.route('/registrarse', methods=['GET','POST'])
def registro():

	if(request.method == 'POST'):
		db = shelve.open('datos.dat')
		user = request.form['nombre']
		password = request.form['contraseña']

		db[user] = {'Username': user, 'Password': password}
		db.close()
		return redirect(url_for('index'))

	return render_template('registrarse.html')

@app.route('/busqueda', methods=['GET','POST'])
def busqueda():
	session['acceso-con-get']=True
	client = MongoClient('localhost', 27017)
	db = client['test']
	restaurants = db.restaurants
	if(request.method=='POST'):
		session['acceso-con-get']=False
		query = restaurants.find({ 'borough' : request.form['buscar']}).limit(10)
		return render_template('busqueda.html', value=query, param=request.form['buscar'])

    # return render_template('restaurants.html', value=query)
	else:
		return render_template('busqueda.html', value="null")

@app.route('/busqueda-ajax', methods=['GET'])
def busqueda_ajax():
	client = MongoClient('localhost', 27017)
	db = client['test']
	restaurants = db.restaurants
	barrio = request.args.get('param', '')
	pagina_py = int(request.args.get('pagina_py', 1))-1
	query = restaurants.find({ 'borough' : barrio}).skip(pagina_py*10).limit(10)

	return dumps(query)

@app.route('/contacto')
def contacto():
	return render_template('contacto.html')

@app.route('/editar', methods=['GET','POST'])
def editar():

	db = shelve.open('datos.dat')
	datos = db.get(session['username'],None)
	db.close()
	return render_template('editar.html', misDatos = datos)

@app.route('/modificar', methods=['POST'])
def modificar():
	db = shelve.open('datos.dat')
	del db[session['username']]
	aux_user = request.form['nombre']
	aux_pass = request.form['contraseña']
	db[aux_user] = {'Username': aux_user, 'Password': aux_pass}
	session['username'] = aux_user
	datos = db[aux_user]
	db.close()

	return render_template('editar.html', misDatos = datos)

@app.route('/logout')
def logout():
	session.pop('username', None)
	session['logged'] = False
	return redirect(url_for('index'))

@app.before_request
def before_request():
	nueva = request.url
	if request.url != "http://127.0.0.1:5000/favicon.ico":
		if 'anterior2' in session:
			session['anterior3'] = session['anterior2']
		if 'anterior1' in session:
			session['anterior2'] = session['anterior1']
		session['anterior1'] = nueva

@app.errorhandler(404)
def page_not_found(error):
	return render_template('error404.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
