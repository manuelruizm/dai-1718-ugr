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

def generarTablero():
	'''
	Función que genera un tablero todo a cero.

	Argumentos:

		No tiene.

	Salida:

		Una matriz nxn con todos sus valores a 0.

	'''

	n = 10
	matriz = []

	for i in range(n):
		fila = [0 for j in range(n)]
		matriz.append(fila)

	matriz[4][3] = 1
	matriz[4][4] = 1
	matriz[5][4] = 1
	matriz[5][5] = 1
	matriz[6][4] = 1
	matriz[6][3] = 1

	return matriz


def imprimirTablero(tablero):
	'''
	Función que imprime un tablero.

	Argumentos:

		tablero: Matriz nxn.

	Salida:

	'''

	for i in range(len(tablero)):
		print(tablero[i])


def guardarTablero(tablero, i):

	nombre = "IOFiles/JDLV-Generacion"+str(i)+".txt"
	f = open(nombre, "w")
	for i in range(len(tablero)):
		f.write(str(tablero[i])+"\n")
	f.close()


def calcularVecinos(i,j,tam,tablero):

	vecinos = []
	if(i>=1 and i<tam-1 and j>=1 and j<tam-1):
		vecinos = [tablero[i-1][j-1], tablero[i-1][j], tablero[i-1][j+1], 
				   tablero[i][j-1], 				   tablero[i][j+1], 
				   tablero[i+1][j-1], tablero[i+1][j], tablero[i+1][j+1]]
	elif(i==0 and j>=1 and j<tam-1):
		vecinos = [ 
				   tablero[i][j-1], 				   tablero[i][j+1], 
				   tablero[i+1][j-1], tablero[i+1][j], tablero[i+1][j+1]]
	elif(i==tam-1 and j>=1 and j<tam-1):
		vecinos = [tablero[i-1][j-1], tablero[i-1][j], tablero[i-1][j+1], 
				   tablero[i][j-1], 				   tablero[i][j+1]]
	elif(j==0 and i>=1 and i<tam-1):
		vecinos = [tablero[i-1][j], tablero[i-1][j+1], 
				    				tablero[i][j+1], 
				   tablero[i+1][j], tablero[i+1][j+1]]
	elif(j==tam-1 and i>=1 and i<tam-1):
		vecinos = [tablero[i-1][j-1], tablero[i-1][j], 
				   tablero[i][j-1], 				  
				   tablero[i+1][j-1], tablero[i+1][j]]
	elif(i==0 and j==0):
		vecinos = [tablero[i][j+1], tablero[i+1][j], tablero[i+1][j+1]]
	elif(i==0 and j==tam-1):
		vecinos = [tablero[i][j-1], tablero[i+1][j-1], tablero[i+1][j]]
	elif(i==tam-1 and j==0):
		vecinos = [tablero[i-1][j], tablero[i-1][j+1], tablero[i][j+1]]
	elif(i==tam-1 and j==tam-1):
		vecinos = [tablero[i-1][j-1], tablero[i-1][j], tablero[i][j-1]]

	suma = 0
	for i in range(0,len(vecinos)):
		suma += vecinos[i]

	return suma


def calcularSiguienteGeneracion(tableroAnterior, tablero):

	for i in range(len(tablero)):
		for j in range(len(tablero)):
			numVecinos = calcularVecinos(i,j,len(tablero),tableroAnterior)
			if(tableroAnterior[i][j]==0 and numVecinos==3):
				tablero[i][j] = 1
			elif(tableroAnterior[i][j]==1 and not(numVecinos==2 or numVecinos==3)):
				tablero[i][j] = 0

	return tablero


def juegoDeLaVida(n):
	'''
	Implementación del juego de la vida.

	'''
	
	generacion = 0
	tablero = generarTablero()
	tableroAnterior = [tablero[i][:] for i in range(len(tablero))]

	print("---------------------------")
	print("Generación ", generacion)
	imprimirTablero(tablero)
	guardarTablero(tablero, generacion)

	generacion += 1
	tablero = calcularSiguienteGeneracion(tableroAnterior, tablero)
	tableroAnterior = [tablero[i][:] for i in range(len(tablero))]

	print("---------------------------")
	print("Generación ", generacion)
	imprimirTablero(tablero)
	guardarTablero(tablero, generacion)

	while(generacion < n):

		generacion += 1
		tablero = calcularSiguienteGeneracion(tableroAnterior, tablero)
		tableroAnterior = [tablero[i][:] for i in range(len(tablero))]

		print("---------------------------")
		print("Generación ", generacion)
		imprimirTablero(tablero)
		guardarTablero(tablero, generacion)

#------------------------------------------------------------------------------

juegoDeLaVida(2)