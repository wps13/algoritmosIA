import numpy
from random import randint

'''
Grupo: Ana Luisa, Estela, Kallil, Willane

O problema proposto foi movimentar animais, mais especificamente formigas, dentro de um espaço
delimitado. No qual o movimento seria gerado aleatoriamente, tendo como intervalo inicial um 
valor menor, de forma a limitar o espaço e aumentando gradativamente. O algoritmo considera que cada cromossomo tem como genes a posição, onde cada coordenada é um gene, e o fit, assim esses valores são calculados e armazenados na matriz pop. A seleção será feita usando o método da roleta, considerando como intervalo o menor valor de e a soma total dos fits, gerando valores aleatorios e associando cada cromossomo com um subintervalo correspondente. 
'''

class movAnimal():
    '''
     manipultaMat
        Função responsável por inicializar e preencher as matrizes da população(pop)
        Calcula-se a distância e fit de cada elemento.
        A matriz da população tem como parametros as posições x,y e fit de cada elemento(linha)
    '''
    def main(elems,valorMax):
        #cromossomos iniciais - matriz 5xelems
        pop = numpy.zeros(shape=(elems,3))
        aux = numpy.zeros(shape=(elems),2)
        novaPop = numpy.zeros(shape=(2,1))
        somaFit = 0
        qntdNovaPop=0

        for i in range(elems):
            posX = randint(0,valorMax)
            posY = randint(0,valorMax)
            distElem = dist(posX,posY)
            fitElem = fit(distElem)
            pop[i] = [posX,posY,fitElem]
            aux= mutacao(posX,posY) #mutação do gene
            pop[i] = [aux[0],aux[1],fitElem]
            somaFit+= fitElem
            ind=0

            #seleção dos elementos pelo método da roleta
            if(i == 0):
                aux[i] = pop[i][2]
            else:
                aux[i] = pop[i-1][2] +  fitElem

            
            limInferior = aux[0]
            limSuperior = somaFit
            probabilidade = randint(limInferior,limSuperior)
                while(qntdNovaPop <= 2):
                    for i in range(elems)
                        if(probabilidade>aux[i-1] && probabilidade<=aux[i])
                        novaPop[ind] = aux[i]
                    ind++

    #modificação do gene
    def mutacao(posX,posY):
        #Gera-se uma nova posição, que será no máx. 49, já somando com a antiga posição
        novoX = posX + randint(0,(49-posX))
        novoY = posY + randint(0,(49-posY))
        return [novoX,novoY]

    #dist: Calcula a distância euclidiana de cada elemento com relação ao tamanho do espaço
    def dist(a,b):
        distTotal = ((49-a)**2 + (49-b)**2)**0.5
        return distTotal
    
    # A função fit responsável por  calcular a proximidade do elemento, considerando 1 como tendo chegado a posição final 
    # e iniciando em (1+sqrt(2)50)
    def fit(distElem):
        fitElem = 1+distElem
        return fitElem

   #reprodução dos cromossomos     
    def crossingOver():
    
    
class main:

    #gerações totais a serem geradas
    geracoes = 20

