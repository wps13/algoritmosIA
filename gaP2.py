import numpy
from random import randint

'''
Questão 3 - Prova 2

Implementar algoritmo genético responsável por achar melhor caminho
'''
#cria população inicial
pop = [
	[0,2,9,3,6],
	[2,0,4,3,8],
	[9,4,0,7,3],
	[3,3,7,0,3],
	[6,8,3,3,0]]

#array para armazenar os fits de cada cromossomo
fits=numpy.zeros(5)

def fit():
	'''
	Função que calcula os fits dos cromossomos
	Quanto maior o valor, melhor é o cromossomo
	soma-se os pesos dos genes e calcula o inverso
	Visto que procura-se o menor caminho possível
	'''
	sumFits=numpy.sum(pop,axis=1)
	sumFits = 1/sumFits
	return sumFits

def selecao():
	totalFits = fits.sum()
	print(totalFits)
	limInferior = 0
	limSuperior = totalFits
	while(ind <= 3):
		indAtual = 

	
#def crossingOver():
		

#def mutacao():
'''
Modifica o gene com maior peso, tornando-o um
caminho não acessavel,por defini-lo como peso 0.
Escolhe os cromossomos com maior fit.
'''			
	
def main():
	fits=fit()
	selecao()
	#crossingOver()
