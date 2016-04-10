#! /usr/bin/python
# -*- coding: utf-8 -*-

import random as rand
import numpy as np

def crearPoblacion(tamanioPoblacion,tamanioGenotipo):
	poblacion = []
	aux = ""
	for j in range(tamanioPoblacion):
		for i in range(tamanioGenotipo):
			x = str(rand.randint(1,9))
			aux = aux + x
		poblacion.append(aux)
		aux = ""	
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
def mc(A,n):
	matriz = []
	A = map(int,A)
	for i in range(0,len(A),n):
		aux = list(A[i:i+n])
		matriz.append(aux)
		aux = []
	return  matriz
def calcular_Aptitud(poblacion,tipoProblema):
	aptitud = []
	suma = 0
	n = len(poblacion[0]) / 3
	print n
	sn = (n*(n**2 + 1))/2 	
	for each in poblacion:
		aux = mc(each,n)
		aux = magic_square(aux)
		print aux
		for i in range(len(each)-1):
			suma = suma + (sn - aux[i])**2
		aptitud.append(suma)
	return aptitud  * tipoProblema

poblacion =  crearPoblacion(1,9)	
print calcular_Aptitud(['123456789'],1)
#f = lambda A, n = 4: [A[i:i+n] for  i in range(0,len(A),n)]
#print z