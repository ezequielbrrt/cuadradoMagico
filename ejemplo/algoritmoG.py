import random
import struct
import ejercicio1 as punto1
import cruza as cruza
import mutacion as mutacion
import seleccion as seleccion

TAMANIO_POBLACION = 4000
NUMERO_GENERACIONES = 100000
TAMANIO_CUADRO = 4
TAMANIO_GENOTIPO = TAMANIO_CUADRO ** 2
PROBABILIDAD_CRUZA = 0.70
NUMERO_MEJORESINDIVIDUOS = 6
PROBABILIDAD_MUTACION = 0.85
MAX = 1
MIN = -1
TIPO_PROBLEMA = MIN
NUMERO_EJERCICIO = 1
metodoAptitud = {
	1 : punto1.calcular_Aptitud
}
metodoPoblacion = {
	1 : punto1.crearPoblacion
}

def getKey(item):
	return item[1]
def ordenar(poblacion, aptitud):
	lista = []
	aux = []
	ordenados = [] 
	for i,(pob,apt) in enumerate(zip(poblacion, aptitud)):
		aux.append(i)
		aux.append(apt)
		aux.append(pob)
		lista.append(aux)
		aux = []
	lista = sorted(lista,key=getKey,reverse=True)
	for x  in range(len(poblacion)):
		ordenados.append(lista[x][2])
	return ordenados   

def elitismo(Individuos, NUMERO_MEJORESINDIVIDUOS, mejoresIndividuos, aptitud):
	if mejoresIndividuos == None:
		ordenados=ordenar(Individuos, aptitud)
		mejoresIndividuos=[]	
		for i in range(0, NUMERO_MEJORESINDIVIDUOS):
			mejoresIndividuos.append(ordenados[i])
	else:
		ordenados=ordenar(Individuos, aptitud)
		for i in range(NUMERO_MEJORESINDIVIDUOS):
			mejoresIndividuos.append(ordenados[i])
		aptitud = metodoAptitud[NUMERO_EJERCICIO](mejoresIndividuos,TIPO_PROBLEMA, TAMANIO_CUADRO, TAMANIO_GENOTIPO)	
		ordenados2=ordenar(mejoresIndividuos, aptitud)
		mejoresIndividuos=ordenados2[0:NUMERO_MEJORESINDIVIDUOS]
	return mejoresIndividuos
	
	
################### ALGORITMO GENETICO ########################	
	
def algoritmoGen(TAMANIO_POBLACION, NUMERO_GENERACIONES, TAMANIO_GENOTIPO, PROBABILIDAD_CRUZA, NUMERO_MEJORESINDIVIDUOS, listaPadres):
	generacionActual=0 #Listo
	mejoresIndividuos=None #Listo
	Individuos = metodoPoblacion[NUMERO_EJERCICIO](TAMANIO_POBLACION,TAMANIO_GENOTIPO)
	aptitud = metodoAptitud[NUMERO_EJERCICIO](Individuos, TIPO_PROBLEMA, TAMANIO_CUADRO, TAMANIO_GENOTIPO)
	mejoresIndividuos=elitismo(Individuos, NUMERO_MEJORESINDIVIDUOS, mejoresIndividuos, aptitud)
	print "Aptitudes ",  metodoAptitud[NUMERO_EJERCICIO](mejoresIndividuos, TIPO_PROBLEMA, TAMANIO_CUADRO, TAMANIO_GENOTIPO)
	for i in mejoresIndividuos :
		print i
	listaPadres = seleccion.seleccionarPadres(Individuos, aptitud)
	nuevaPoblacion = Individuos
	while generacionActual < NUMERO_GENERACIONES :
		nuevaPoblacion = cruza.cruzarPadres(nuevaPoblacion, listaPadres, PROBABILIDAD_CRUZA)
		nuevaPoblacion = mutacion.mutacionUniforme(nuevaPoblacion, PROBABILIDAD_MUTACION, TAMANIO_GENOTIPO)
		aptitud = metodoAptitud[NUMERO_EJERCICIO](nuevaPoblacion, TIPO_PROBLEMA, TAMANIO_CUADRO, TAMANIO_GENOTIPO)
		mejoresIndividuos = elitismo(nuevaPoblacion, NUMERO_MEJORESINDIVIDUOS,mejoresIndividuos, aptitud)
		print "Generacion: ", generacionActual
		print "Aptitudes",  metodoAptitud[NUMERO_EJERCICIO](mejoresIndividuos,TIPO_PROBLEMA, TAMANIO_CUADRO, TAMANIO_GENOTIPO)
		for i in mejoresIndividuos:
			print i
		print("\n")
		listaPadres = seleccion.seleccionarPadres(nuevaPoblacion, aptitud)
		generacionActual+=1
listaPadres = []
algoritmoGen(TAMANIO_POBLACION, NUMERO_GENERACIONES, TAMANIO_GENOTIPO, PROBABILIDAD_CRUZA, NUMERO_MEJORESINDIVIDUOS, listaPadres)
