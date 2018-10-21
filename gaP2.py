import numpy
from random import randint

'''
Questão 3 - Prova 2

Implementar algoritmo genético responsável por achar melhor caminho
'''
#cria população inicial
pop = numpy.zeros(shape=(5,5))
#matriz para armazenar os fits de cada cromossomo
fits= numpy.zeros(shape=(5,1))

#preenchendo os pesos iniciais dos caminhos	
pop[0][0] = 0
pop[0][1] = 2
pop[0][2] = 9
pop[0][3] = 3
pop[0][4] = 6

pop[1][0] = 2
pop[1][1] = 0
pop[1][2] = 4
pop[1][3] = 3
pop[1][4] = 8

pop[2][0] = 9
pop[2][1] = 4
pop[2][2] = 0
pop[2][3] = 7
pop[2][4] = 3

pop[3][0] = 3
pop[3][1] = 3
pop[3][2] = 7
pop[3][3] = 0
pop[3][4] = 3
	
pop[4][0] = 6
pop[4][1] = 8
pop[4][2] = 3
pop[4][3] = 3
pop[4][4] = 0
	
for i in pop:
	print(i)

def fit():

fit()

for i in fits:
	print(i)

