#! /usr/bin/python
# -*- coding: utf-8 -*-

import random as ran
from itertools import cycle
import random as random

def ordered_crossover(padre,madre):
	hijo1 = [] * 0
	print padre
	print madre
	al = ran.randint(0,len(padre))
	al2 = ran.randint(0,len(padre))
	while al >= al2:
		al = ran.randint(0,len(padre))
		al2 = ran.randint(0,len(padre))
	#hijo1 = list("0"*len(padre))
	print al, al2
	print 
	aux =  padre[al:al2]
	aux2 =  madre[al:al2]
	for i,j in zip(aux,range(al2-al)):
		print i, j
	for i in madre:
		if i not in aux:
			pass 
	

	
def portially_mapped_crossover(padre,madre):	#PMX
	hijo1 = padre
	hijouno = [0] * len(padre)
	p1 = ran.randint(0,len(padre)-1)
	p2 = ran.randint(0,len(padre)-1)
	print p1, p2

def position_based_crossover(padre,madre):
 	al = [ran.randint(0,len(padre)-1) for i in range(ran.randint(1,len(padre)))] 
 	al2 = [ran.randint(0,len(padre)-1) for i in range(ran.randint(1,len(padre)))]
 	pos1 = []
 	pos2 = [] 
	for i in al: 
		if i not in pos1: pos1.append(i)
	for i in al2:
		if i not in pos2: pos2.append(i)
	#print pos1
	#print pos2
	hijo1 = padre
	hijo2 = madre

	for i in pos1:
		if i < len(hijo1):
			del hijo1[i]
	for x in pos1:
		for y in madre:
			if y not in hijo1:
				hijo1.insert(x,y)

	for i in pos2:
		if i < len(hijo2):
			del hijo2[i]
	for x in pos2:
		for y in padre:
			if y not in hijo2:
				hijo2.insert(x,y)
	#print hijo1 
	#print hijo2
	return hijo1,hijo2 

def OrdererCrossover(padre, madre):
	t = len(padre)
	hijo1 = []
	hijo2 = []
	i = int(random.randint(0, t-1))
	j = int(random.randint(0, t-1))
	i2 = int(random.randint(0, t-1))
	j2 = int(random.randint(0, t-1))
	for i in range (0, t):
		hijo1.append(None)
		hijo2.append(None)
	while i >= j:
		i = int(random.randint(0, t-1))
		j = int(random.randint(0, t-1))
	while i2 >= j2:
		i2 = int(random.randint(0, t-1))
		j2 = int(random.randint(0, t-1))
	#print i2, j2
	hijo1[i:j] = padre[i:j]
	hijo2[i2:j2] = padre[i2:j2]
	#print "hijo1", hijo1
	#print "hijo2", hijo2
	madre1 = madre[:]
	madre2 = madre[:]
	#print "madre1", madre1
	#print "madre2", madre2
	for x in range (0, t):
		for y in range (i, j):
			if madre1[x] == hijo1[y]:
				madre1[x] = None
	
	for x2 in range (0, t):
		for y2 in range (i2, j2):
			if madre2[x2] == hijo2[y2]:
				madre2[x2] = None
	#print "madre1", madre1
	#print "madre2", madre2
	x = 0
	y = 0
	while x < t:
		if madre1[x] != None:
			if hijo1[y] == None:
				hijo1[y] = madre1[x]
				x += 1
				y += 1
			else:
				y += 1
		else:
			x += 1
	x2 = 0
	y2 = 0
	while x2 < t:
		if madre2[x2] != None:
			if hijo2[y2] == None:
				hijo2[y2] = madre2[x2]
				x2 += 1
				y2 += 1
			else:
				y2 += 1
		else:
			x2 += 1
	return hijo1, hijo2

def cruzaPadres(poblacion,listaPadres,porcentajeCruza):
	nuevaPoblacion = []
	for i in range(0,len(poblacion),2):
		porcentaje = ran.random()
		if porcentaje < (float(porcentajeCruza)/100):
			hijo1,hijo2 = OrdererCrossover(poblacion[listaPadres[i]],poblacion[listaPadres[i+1]])
		else:
			hijo1 = poblacion[listaPadres[i]]
			hijo2 = poblacion[listaPadres[i+1]]
		nuevaPoblacion.append(hijo1)
		nuevaPoblacion.append(hijo2)
	return nuevaPoblacion

x = [1,2,3,4,5,6,7,8,9]
y = [9,8,7,6,5,4,3,2,1]


#print position_based_crossover(x,y)
#portially_mapped_crossover(x,y)
#print ordered_crossover(x,y)