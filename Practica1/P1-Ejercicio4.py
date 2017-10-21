#------------------------------------------------------------------------------
#
#	Manuel Ruiz Maldonado
#	
#	DAI - Desarrollo de Aplicaciones para Internet
#	Curso 2017-2018
#
#	Práctica 1: Ejercicio 4 - Soluciones
#
#------------------------------------------------------------------------------

#!/usr/bin/env python
# -*- coding: UTF-8 -*-

def fibonacci(n):
	'''
	Función que calcula el n-ésimo número de la sucesión de Fibonacci.

	Argumentos:

		n: Número de la sucesión que se quiere calcular.

	Salida:

		El valor de la sucesión de Fibonacci en la posición n-ésima.

	'''

	a, b = 1, 1
	for i in range(n):
		a, b = b, a+b
	return a


def leerEscribirFibonacci():
	'''
	Función encargada de leer desde un fichero, llamar a la función de 
	Fibonacci y guardar el resultado en otro fichero.

	Argumentos:

		No tiene.

	Salida:

		Un fichero llamado E4-out.txt.

	'''

	f = open("IOFiles/E4-in.txt")
	n = int(f.read())
	f.close()

	fib = fibonacci(n)

	f = open("IOFiles/E4-out.txt", "w")
	f.write(str(fib))
	f.close()

	print("El número de Fibonacci en la posición ", n, " es ", fib)


#------------------------------------------------------------------------------

leerEscribirFibonacci()