import random as ran
import ejercicio1 as punto1


def calculaMedia(aptitudes):
	ap_total=0
	media=0
	for i in range (0,len(aptitudes)):
		ap_total=ap_total+aptitudes[i]
	media = ap_total / len(aptitudes)
	return media
	
def  sobrante_Estocastico_CR(poblacion,aptitud):
	f = float(sum(aptitud))/float(len(aptitud))
	listaPadres = []	
	e = []
	for i in aptitud:
		e.append(float(i)/f)
	for i in range(len(poblacion)):
		pass

def sobrante_Estocastico_SR(poblacion,aptitud):
	listaPadres = []
	aux = []
	f = float(sum(aptitud))/float(len(aptitud))
	e = []
	for i,y in zip(aptitud,range(len(aptitud))):
  		aux.append(float(i)/f)
  		aux.append(y)
  		e.append(aux)
  		aux = []
  	for i in range(len(e)):
  		if e[i][0] >= 1:
  			listaPadres.append(e[i][1])
  	i = 0
  	while len(listaPadres) -1 < len(poblacion)-1:
  		if int(e[i % len(poblacion)][0]) == ran.randint(0,1):
  			listaPadres.append(i % len(poblacion))
  		i += 1	
  	return listaPadres

def seleccionRuleta(Individuos, aptitud):
	x = calculaMedia(aptitud)
	e = []
	var = 0
	for i in range(0, len(Individuos)):
		var=aptitud[i]/x
		e.append(var)
	r=ran.randrange(len(Individuos))
	sum_e=0
	i=0
	while i < len(Individuos):
		sum_e += e[i]
		if sum_e > r:
			return i
		i = i + 1
	return i-1

def seleccionarPadres(Individuos, aptitud):
	#listaPadres=[]
	#for i in range(len(Individuos)):
	#	listaPadres.append(seleccionRuleta(Individuos, aptitud))
	listaPadres = sobrante_Estocastico_SR(Individuos,aptitud)	
	return listaPadres
