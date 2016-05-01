#! /usr/bin/python
# -*- coding: utf-8 -*-


import random as rand
import numpy as np

def crearPoblacion(tamanioPoblacion,tamanioGenotipo):
	poblacion = []
	z = np.array([])
	aux = []
	for j in range(tamanioPoblacion):
		while True :
			x = rand.randint(1,tamanioGenotipo)
			if x not in aux:
				aux.append(x)
			if len(aux) == tamanioGenotipo:
				break
		poblacion.append(aux)
		aux = []	
	return poblacion

def magic_square(matrix):
    iSize = len(matrix[0])
    sum_list = []
    #Horizontal
    sum_list.extend([sum (lines) for lines in matrix])
    #Vertical:
    for col in range(iSize):
        sum_list.append(sum(row[col] for row in matrix))
    #Diagonals
    dlResult = 0
    for i in range(0,iSize):
        dlResult +=matrix[i][i]
    sum_list.append(dlResult)  
    drResult = 0
    for i in range(iSize-1,-1,-1):
        drResult +=matrix[i][i]
    sum_list.append(drResult)
    return sum_list


def matriz(individuo,n):
	mat = []
	m = []
	z = n
	for i in individuo:
		z -= 1
		mat.append(i)
		if z == 0:
			m.append(mat)
			mat=[]
			z = n
	return m

def calcularAptitud(poblacion,tipoProblema,n):
	aptitud = []
	sn = (n*(n**2 + 1))/2 	
	for each in range(len(poblacion)):
		suma = 0
		x = matriz(poblacion[each],n)
		aux = magic_square(x)
		for i in range(0,len(aux)-1):
			suma = suma + (sn - aux[i])**2
		aptitud.append(suma * tipoProblema)
	return aptitud 


#poblacion = [[5, 9, 1, 7, 2, 6, 3, 4, 8]]	
#print calcularAptitud(poblacion,-1,3)



"""
import random

def aleatorios(tamanioGenotipo):
	numeros = []
	while len(numeros) < tamanioGenotipo:
		numero = random.randint(1, tamanioGenotipo)     
		if not numero in numeros:
			numeros.append(numero)     
	return numeros

def crearPoblacion(tamanioPoblacion,tamanioGenotipo):
	arr = []
	for i in range(tamanioPoblacion):
		x = aleatorios(tamanioGenotipo)
		arr.append(x)
	return arr

###########Calcular Aptitud########
def evaluar_funcion(x1,tipoProblema, TAMANIO_CUADRO, tamanioGenotipo):
	suma = 0
	aptitud = 0
	Mi = []
	Sn = (TAMANIO_CUADRO*((TAMANIO_CUADRO**2)+1))/2
	resultado = 0
	for i in range(TAMANIO_CUADRO):
		suma = 0
		for j in range(0,len(x1),TAMANIO_CUADRO):
			new = x1[i + j] 
			suma = new + suma
		Mi.append(suma)
	
	for i in range(0,len(x1),TAMANIO_CUADRO):
		suma = 0
		for j in range(TAMANIO_CUADRO):
			new = x1[i + j] 
			suma = new + suma
		Mi.append(suma)
	i = 0
	j = 0
	suma = 0
	while i < len(x1):
		new = x1[i + j]
		suma = new + suma
		i += TAMANIO_CUADRO
		j +=1
	Mi.append(suma)
	#print suma
	i = len(x1)-1
	j = TAMANIO_CUADRO - 1
	suma = 0
	while i > 0:
		new = x1[i - j]
		#print i, j
		suma = new + suma
		i -= TAMANIO_CUADRO
		j -=1
	Mi.append(suma)
	#print suma
	#print "sumas", Mi
	#print "sn", Sn
	for i  in range (0, ((TAMANIO_CUADRO * 2) + 2)):
		sumatoria = (Sn - Mi[i])**2
		aptitud = aptitud + sumatoria
	#print aptitud
	return aptitud * tipoProblema
	#return sumah * tipoProblema
def calcular_Aptitud(poblacion,tipoProblema, TAMANIO_CUADRO, tamanioGenotipo):
	aptitudes = []
	for i in range(0,len(poblacion)):
		x1 = poblacion[i]
		aptitudes.append(evaluar_funcion(x1, tipoProblema, TAMANIO_CUADRO, tamanioGenotipo))
	#print len(aptitud)
	#print aptitud
	return aptitudes
##############################
"""