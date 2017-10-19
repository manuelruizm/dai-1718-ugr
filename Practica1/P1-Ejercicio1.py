#------------------------------------------------------------------------------
#
#	Manuel Ruiz Maldonado
#	
#	DAI - Desarrollo de Aplicaciones para Internet
#	Curso 2017-2018
#
#	Práctica 1 - Soluciones
#
#------------------------------------------------------------------------------

#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from random import randint

def adivinarNumero():
	'''
	Función que genera un número aleatorio para que lo adivine el usuario.

	Argumentos:

		No tiene.

	Salida:

		No tiene. Interacción mediante print-input.

	'''

	aleatorio = randint(1,100)
	encontrado = False
	i = 0

	while( (i < 10) and (not encontrado)):

		print("--------------------------------------------------")
		print("Número de intentos: ", i)
		valor = int(input("Introduzca un número entre el 1 y el 100: "))

		if valor == aleatorio:
			encontrado = True
			print("\nvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv")
			print("ENHORABUENA!! Valor encontrado.")
			print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")

		elif ((valor < 1) or (valor > 100)):
			print("El número debe estar entre 1 y 100")

		elif valor > aleatorio:
			print("El número buscado es MENOR.")

		elif valor < aleatorio:
			print("El número buscado es MAYOR.")

		i += 1

	if not encontrado:
		print("\nxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
		print("GAME OVER.\nEl número buscado era ", aleatorio)
		print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")

adivinarNumero()