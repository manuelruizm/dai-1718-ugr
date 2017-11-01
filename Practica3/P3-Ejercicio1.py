#------------------------------------------------------------------------------
#
#	Manuel Ruiz Maldonado
#	
#	DAI - Desarrollo de Aplicaciones para Internet
#	Curso 2017-2018
#
#	Práctica 3: Ejercicio 1 - Soluciones
#
#------------------------------------------------------------------------------

#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from flask import Flask, render_template, session, request, redirect, url_for
import shelve

app = Flask(__name__)
app.secret_key = 'random key'

@app.route('/', methods=['GET','POST'])
def index():

	get_access = True
	global logged
	logged = True

	# Si se pide con un GET se da la página tal cual.
	if(request.method == 'POST'):
		get_access = False

	if(not 'username' in session):
		logged = False

	if(not get_access):
		db = shelve.open('datos.dat')
		user = db.get(request.form['nombre'], None)
		if(user!=None):
			user = user['Username']
		password = request.form['contraseña']

		if(password == db[user]['Password']):
			logged = True
			session['username'] = user
		else:
			logged = False
		db.close()

	return render_template('index.html', logueado = logged)

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

@app.route('/clasificacion')
def clasificacion():
	return render_template('clasificacion.html', logueado = logged)

@app.route('/contacto')
def contacto():
	return render_template('contacto.html', logueado = logged)

@app.route('/editar', methods=['GET','POST'])
def editar():

	db = shelve.open('datos.dat')
	datos = db.get(session['username'],None)
	db.close()	
	return render_template('editar.html', logueado = logged, misDatos = datos)

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

	return render_template('editar.html', logueado = logged, misDatos = datos)

	

@app.route('/logout')
def logout():
	session.pop('username', None)
	return redirect(url_for('index'))

@app.errorhandler(404)
def page_not_found(error):
	return render_template('error404.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)