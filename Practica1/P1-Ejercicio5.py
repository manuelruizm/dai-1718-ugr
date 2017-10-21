#------------------------------------------------------------------------------
#
#	Manuel Ruiz Maldonado
#	
#	DAI - Desarrollo de Aplicaciones para Internet
#	Curso 2017-2018
#
#	Práctica 1: Ejercicio 5 - Soluciones
#
#------------------------------------------------------------------------------

#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from random import randint

def generarCorchetes():
	'''
	Función que genera una cadena de corchetes.

	Argumentos:

		No tiene.

	Salida:

		Una cadena de corchetes.

	'''

	n = randint(1,10)
	cadena = ""

	for i in range(0, n):
		valor = randint(0,1)
		if valor==0:
			cadena += "["
		else:
			cadena += "]"

	return cadena

def estaBalanceada():
	'''
	Función que comprueba si una cadena generada con la función 
	generarCorchetes está balanceada o no.

	Argumentos:

		No tiene.

	Salida:

		True o False dependiendo si está o no balanceada.
	'''

	cadena = generarCorchetes()
	abren = 0
	cierran = 0
	i = 0
	balanceada = True

	while((i < len(cadena)) and (balanceada)):
		if(cadena[i] == "["):
			abren += 1
		elif(cadena[i] == "]"):
			cierran += 1

		if((abren - cierran) < 0):
			balanceada = False
		i += 1

	if(abren - cierran != 0):
		balanceada = False

	print(cadena)
	if(balanceada):
		print("Está balanceada")
	else:
		print("No está balanceada - Posición: ", i)

#------------------------------------------------------------------------------

estaBalanceada()