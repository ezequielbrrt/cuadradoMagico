#! /usr/bin/python
# -*- coding: utf-8 -*-

import cruza.cruzas as cruza
import mutacion.mutaciones as mutacion
import seleccion.seleccion as seleccion
import practicas.cuadradoMagico.cuadradoMagico as cuadradoMagico
import random  as ran
import numpy as np
import sys

metodoAptitud = {
	1 : cuadradoMagico.calcularAptitud, 
}
MAX = 1
MIN = - 1
metodoPoblacion = {
	1 : cuadradoMagico.crearPoblacion, 
}

###############CONFIGURACION INICIAL ##################
NUMERO_PRACTICA = 1
TIPO_PROBLEMA = MIN
N = int(sys.argv[1])


TAMANIO_POBLACION =   1000
NUMERO_GENERACIONES = 200000
PORCENTAJE_CRUZA = 85
PORCENTAJE_MUTACION = 90	
NUMERO_MEJORES_INDIVIDUOS = 4
TAMANIO_GENOTIPO = N * N
######################################################

####################Elitismo######################
def getKey(item):
	return item[1]
def ordenar(poblacion, aptitud):
	lista = []
	aux = []
	ordenados = [] 
	for i,(pob,apt) in enumerate(zip(poblacion,aptitud)):
		aux.append(i)
		aux.append(apt)
		aux.append(pob)
		lista.append(aux)
		aux = []
	lista = sorted(lista,key=getKey,reverse=True)
	for x  in range(len(poblacion)):
		ordenados.append(lista[x][2])
	return ordenados
def elitismo(poblacion, mejoresIndividuos,aptitud,numeroMejoresIndividuos):
	if mejoresIndividuos == None:
		ordenados = ordenar(poblacion,aptitud)
		mejoresIndividuos = []
		for i in range(0,numeroMejoresIndividuos):
			mejoresIndividuos.append(ordenados[i])
	else:
		ordenados = ordenar(poblacion,aptitud)
		for x in range(numeroMejoresIndividuos):
			mejoresIndividuos.append(ordenados[x])
		aptitud = metodoAptitud[NUMERO_PRACTICA](mejoresIndividuos,TIPO_PROBLEMA,N)
		ordenados2 = ordenar(mejoresIndividuos,aptitud)
		mejoresIndividuos = ordenados2[:numeroMejoresIndividuos]
	return mejoresIndividuos
##############################################

############Algoritmo Genetico######################
def algoritmoGeneticoSimple(tamanioPoblacion,numeroGeneraciones,porcentajeCruza,
	porcentajeMutacion, numeroMejoresIndividuos, tamanioGenotipo,mejoresIndividuos):
	generacionActual = 0
	poblacion = metodoPoblacion[NUMERO_PRACTICA](tamanioPoblacion,tamanioGenotipo)
	aptitud = metodoAptitud[NUMERO_PRACTICA](poblacion,TIPO_PROBLEMA,N)
	mejoresIndividuos = elitismo(poblacion,mejoresIndividuos,aptitud,numeroMejoresIndividuos)
	listaPadres = seleccion.obtener_lista(poblacion,aptitud)
	nuevaPoblacion = poblacion
	while generacionActual < numeroGeneraciones:
		nuevaPoblacion = cruza.cruzaPadres(nuevaPoblacion,listaPadres,porcentajeCruza)
		#aptitud = metodoAptitud[NUMERO_PRACTICA](nuevaPoblacion,TIPO_PROBLEMA,N)
		#mejoresIndividuos = elitismo(nuevaPoblacion,mejoresIndividuos,aptitud,numeroMejoresIndividuos)
		nuevaPoblacion = mutacion.mutacion(nuevaPoblacion, porcentajeMutacion)
		aptitud = metodoAptitud[NUMERO_PRACTICA](nuevaPoblacion,TIPO_PROBLEMA,N)
		#print aptitud
		mejoresIndividuos = elitismo(nuevaPoblacion,mejoresIndividuos,aptitud,numeroMejoresIndividuos)
		print "\n mejores individuos, generación: ", generacionActual
		for i,y in zip(mejoresIndividuos,metodoAptitud[NUMERO_PRACTICA](mejoresIndividuos,TIPO_PROBLEMA,N)) :
			print i, y * TIPO_PROBLEMA
		listaPadres = seleccion.obtener_lista(nuevaPoblacion,aptitud)
		generacionActual += 1
	
#####################################################


def main():
	mejoresIndividuos = None
	listaPadres = []
	algoritmoGeneticoSimple(TAMANIO_POBLACION,NUMERO_GENERACIONES,PORCENTAJE_CRUZA,
		PORCENTAJE_MUTACION, NUMERO_MEJORES_INDIVIDUOS,TAMANIO_GENOTIPO,mejoresIndividuos)
 	
main()


