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

from flask import Flask, render_template, session, request

app = Flask(__name__)

@app.route('/', methods=['GET','POST'])
def index():
	return render_template('index.html')


@app.route('/clasificacion')
def clasificacion():
    return render_template('clasificacion.html')

@app.route('/contacto')
def contacto():
    return render_template('contacto.html')

@app.errorhandler(404)
def page_not_found(error):
    return render_template('error404.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)