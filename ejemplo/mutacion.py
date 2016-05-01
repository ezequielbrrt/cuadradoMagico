import random
import ejercicio1 as punto1

def mutacionUniforme(nuevaPoblacion, PROBABILIDAD_MUTACION, tamanioGenotipo):
	Individuos=nuevaPoblacion
	t = tamanioGenotipo
	nuevaPoblacion = []
	for i in Individuos:
		lista = list(i)
		r = random.random()
		if PROBABILIDAD_MUTACION < r :
			i = int(random.randint(0, t-1))
			j = int(random.randint(0, t-1))
			while i == j:
				i = int(random.randint(0, t-1))
				j = int(random.randint(0, t-1))
			#print i, j
			aux = lista[i]
			lista[i] = lista[j]
			lista[j] = aux
		nuevaPoblacion.append(lista)
		
	return nuevaPoblacion
