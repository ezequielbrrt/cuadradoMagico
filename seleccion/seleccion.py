#! /usr/bin/python
# -*- coding: utf-8 -*-
import random as ran
import numpy as np


def  sobrante_Estocastico_CR(poblacion,aptitud):
	f = float(sum(aptitud))/float(len(aptitud))
	listaPadres = []	
	e = []
	for i in aptitud:
		e.append(float(i)/f)
	for i in range(len(poblacion)):
		pass
	

def seleccion_ruleta(poblacion,aptitud):
	f = float(sum(aptitud))/float(len(aptitud))
  	e = []
  	suma = 0
  	for i in aptitud:
  		e.append(float(i)/f)
  	r = ran.randint(0,len(poblacion))
  	i = 0   		
  	while i < len(poblacion):
	  	suma = suma + e[i]
	  	if suma > r:
	  		return i
	  	i += 1
	return i-1

def sobrante_Estocastico_SR(poblacion,aptitud):
	listaPadres = []
	aux = []
	#print aptitud
	f = float(sum(aptitud))/float(len(aptitud))
	e = []
	for i,y in zip(aptitud,range(len(aptitud))):
  		aux.append(float(i)/f)
  		aux.append(y)
  		e.append(aux)
  		aux = []
  	#print e
  	for i in range(len(e)):
  		#print e[i][0]
  		#print e[i][1]
  		if e[i][0] >= 1:
  			listaPadres.append(e[i][1])
  	i = 0
  	#print listaPadres	
  	while len(listaPadres) -1 < len(poblacion)-1:
  		if int(e[i % len(poblacion)][0]) == ran.randint(0,1):
  			listaPadres.append(i % len(poblacion))
  		i += 1	
  	return listaPadres

def estocastico_universal(poblacion,aptitud):
 	pass
  
def obtener_lista(poblacion,aptitud):
	listaPadres = sobrante_Estocastico_SR(poblacion,aptitud)
	#for i in range(len(poblacion)):
	#	listaPadres.append(seleccion_ruleta(poblacion,aptitud))
	return listaPadres

