#------------------------------------------------------------------------------
#
#	Manuel Ruiz Maldonado
#	
#	DAI - Desarrollo de Aplicaciones para Internet
#	Curso 2017-2018
#
#	Práctica 1: Ejercicio 2 - Soluciones
#
#------------------------------------------------------------------------------

#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from random import randint
from time import time

def burbujaSort(matrix):
	'''
	Función de ordenación de matrices unidimensionales (vectores) utilizando
	el método de Selección.

	Argumentos:

		matrix: una matriz unidimensional

	Salida:

		Esa matriz (vector) ordenado ascendentemente

	'''

	vector = matrix[:]
	n = len(vector)
	for i in range(1, n):
		for j in range(0, n-i):
			if(vector[j] > vector[j+1]):
				vector[j], vector[j+1] = vector[j+1], vector[j]


def seleccionSort(matrix):
	'''
	Función de ordenación de matrices unidimensionales (vectores) utilizando
	el método de la Burbuja.

	Argumentos:

		matrix: una matriz unidimensional

	Salida:

		Esa matriz (vector) ordenado ascendentemente

	'''

	vector = matrix[:]
	n = len(vector)
	for i in range(0, n-1):
		minimo = i
		for j in range(i+1, n):
			if(vector[j] < vector[minimo]):
				minimo = j
		vector[minimo], vector[i] = vector[i], vector[minimo]


def generarVectoresAleatorios():
	'''
	Función encargada de generar matrices unidimensionales con valores 
	aleatorios según el tamaño especificado.

	Argumentos:

		No hay.

	Salida:

		Un vector con valores aleatorios de tamaño tam

	'''

	tam = int(input("Introduzca el tamaño del vector: "))

	if(tam < 2):
		print("El tamaño debe ser mayor que 2.")

	else:

		vector = []
		for i in range(0,tam):
			vector.insert(len(vector), randint(1,tam*2))

		return vector


def compararTiempos():
	'''
	Función encargada de llevar el flujo del programa. Además debe comparar
	los tiempos de ejecución de los dos algoritmos de ordenación implementados.

	Argumentos:

		No hay.

	Salida:

		Comparación de los tiempos de ejecución.

	'''

	vector = generarVectoresAleatorios()

	tiempo_ini_burbuja = time()
	burbujaSort(vector)
	tiempo_fin_burbuja = time()

	tiempo_ini_seleccion = time()
	seleccionSort(vector)
	tiempo_fin_seleccion = time()

	print("Tiempo de ejecución de la Burbuja: ", tiempo_fin_burbuja - tiempo_ini_burbuja)
	print("Tiempo de ejecución de Selección: ", tiempo_fin_seleccion - tiempo_ini_seleccion)

#------------------------------------------------------------------------------

compararTiempos()