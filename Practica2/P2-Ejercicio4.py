#------------------------------------------------------------------------------
#
#   Manuel Ruiz Maldonado
#   
#   DAI - Desarrollo de Aplicaciones para Internet
#   Curso 2017-2018
#
#   Práctica 2: Ejercicio 4 - Soluciones
#
#------------------------------------------------------------------------------

#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from flask import Flask, render_template, request, redirect, url_for
from mandelbrot import *

app = Flask(__name__)

@app.route('/', methods=['GET','POST'])
def index():
    return render_template('P2-E4-1.html')

@app.route('/mandelbrot', methods=['GET','POST'])
def generaFractal():
    x1 = float(request.args.get('x1'))
    x2 = float(request.args.get('x2'))
    y1 = float(request.args.get('y1'))
    y2 = float(request.args.get('y2'))
    anchura = int(request.args.get('anchura'))
    iteraciones = int(request.args.get('iteraciones'))

    renderizaMandelbrot(x1,y1,x2,y2,anchura, iteraciones, "fractal.png")

    return render_template('P2-E4-2.html')

@app.errorhandler(404)
def page_not_found(error):
    return render_template('P2-error.html', err = error)

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
