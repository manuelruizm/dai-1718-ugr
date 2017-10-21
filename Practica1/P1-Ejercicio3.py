#------------------------------------------------------------------------------
#
#	Manuel Ruiz Maldonado
#	
#	DAI - Desarrollo de Aplicaciones para Internet
#	Curso 2017-2018
#
#	Práctica 1: Ejercicio 3 - Soluciones
#
#------------------------------------------------------------------------------

#!/usr/bin/env python
# -*- coding: UTF-8 -*-

def cribaErastotenes():
	'''
	Función que realiza la Criba de Erastótenes para encontrar los números
	primos menores o iguales que n.

	Argumentos:

		No hay.

	Salida:

		Una lista con todos los números primos menores que n

	'''

	n = int(input("Introduzca un número para realizar la Criba de Erastótenes: "))

	multiplos = set()
	primos = []
	for i in range(2, n+1):
		if i not in multiplos:
			primos.insert(len(primos), i)
			multiplos.update(range(i*i, n+1, i))

	print(primos)

#------------------------------------------------------------------------------

cribaErastotenes()