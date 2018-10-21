import numpy
from random import uniform

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

fits=fit()

def selecao():
	totalFits = fits.sum()
	#Armazena os indices dos cromossomos escolhidos
	popAux = numpy.zeros(3)
	novaPop = numpy.zeros((5,5))

	aux = numpy.zeros(5)
	#Armazena os limites para gerar roleta
	valAux = 0
	for i in range(5):
		valAux += fits[i]
		aux[i] = valAux
	#Intervalos de possíveis valores
	intInferior = 0
	intSuperior = totalFits
	#limites usados para encontrar cromossomo
	limInferior = 0
	limSuperior = aux[0]
	#variavel para controlar o preenchimeto da população
	ind=0
	while(ind < 3):
		#Gera-se um valor para procurar na roleta
		probab =uniform(intInferior,intSuperior)
		#Procura-se o elemento entre os intervalos
		#Tendo-se sido somado os fits do elemento atual com os anteriores para assim obter-se as faixas correspondentes
		for i in range(4):
		#Caso o elemento esteja na faixa, armazena-se o indice
		# correspondente ao cromossomo
			if probab>=limInferior and probab<limInferior:
				popAux[ind]=i
				ind+=1
			else:
				limInferior=limSuperior
				limSuperior=aux[i+1]
	#Armazena-se os genes escolhidos
	for i in range(3):
		novaPop[i]=pop[popAux[i]]			 
	#Substitui a população atual pela nova
	for i in range(5):
		pop[i]=novaPop[i]

selecao()	

def crossingOver():
	#Matriz para armazenar os filhos
	filhos = numpy.zeros((2,5))
	for i in range(3):
		for i in range(5):				
			filhos
#def mutacao():
'''
Modifica o gene com maior peso, tornando-o um
caminho não acessavel,por defini-lo como peso 0.
Escolhe os cromossomos com maior fit.
'''
