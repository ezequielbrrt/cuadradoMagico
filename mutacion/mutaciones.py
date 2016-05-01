#! /usr/bin/python
# -*- coding: utf-8 -*-

import random as ran

def mutacion(poblacion,porcentajeMutacion):
	pm = float(porcentajeMutacion)/100
	nuevaPoblacion = []
	for individuo in poblacion:
		for i in individuo:
			r = ran.random()
			if r > pm:	
				p1 = ran.randint(0, len(individuo)-1)
				p2 = ran.randint(0, len(individuo)-1)
				individuo[p1],individuo[p2] = individuo[p2], individuo[p1]
		nuevaPoblacion.append(individuo)
	return nuevaPoblacion
