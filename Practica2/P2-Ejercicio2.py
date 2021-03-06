#------------------------------------------------------------------------------
#
#	Manuel Ruiz Maldonado
#	
#	DAI - Desarrollo de Aplicaciones para Internet
#	Curso 2017-2018
#
#	Práctica 2: Ejercicio 2 - Soluciones
#
#------------------------------------------------------------------------------

#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('P2-E2.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)