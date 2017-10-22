#------------------------------------------------------------------------------
#
#	Manuel Ruiz Maldonado
#	
#	DAI - Desarrollo de Aplicaciones para Internet
#	Curso 2017-2018
#
#	Práctica 2: Ejercicio 3 - Soluciones
#
#------------------------------------------------------------------------------

#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('P2-E3-1.html')

@app.route('/user')
def user():
    return render_template('P2-E3-2.html')

@app.route('/user/<user>')
def username(user):
    return render_template('P2-E3-2.html', usuario=user)

@app.errorhandler(404)
def page_not_found(error):
    return "Página no encontrada", 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)