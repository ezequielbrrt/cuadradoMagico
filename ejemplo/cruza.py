import random


def volado(PROBABILIDAD_CRUZA):
	r=random.randint(0,1)
	if(r<=PROBABILIDAD_CRUZA):
		volado=0
	else:	
		volado=1
	return volado
	
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



def cruzarPadres(Individuos, listaPadres, PROBABILIDAD_CRUZA):
	nuevaPoblacion = []
	for i in range(0, len(Individuos), 2):
		if volado(PROBABILIDAD_CRUZA)==1:
			hijo1,hijo2 = OrdererCrossover(Individuos[listaPadres[i]],Individuos[listaPadres[i+1]])
		else:
			hijo1=Individuos[listaPadres[i]]
			hijo2=Individuos[listaPadres[i+1]]
		nuevaPoblacion.append(hijo1)
		nuevaPoblacion.append(hijo2)
	return nuevaPoblacion
