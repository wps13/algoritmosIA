import numpy
from random import randint

'''
Particle Swarm Optimization - Otimização por enxame de Partículas
'''

class pso:
    '''
    tam é o tamanho da enxame
    velMax é a velocidade máxima das partículas
    '''
    def __init__(self,tam, velMax):
        self.tam = tam
        self.velMax = velMax
       #faltam alguns parametros

    def enxame():
        x = numpy.zeros(shape=(tam,1))      #posição
        vel = numpy.zeros(shape=(tam,1))    #velocidade
        lBest = numpy.zeros(shape=(tam,1))  #melhor local
        gBest = numpy.zeros(shape=(tam,1))  #melhor global
        #checar tamanho do vetor para os melhores valores

        #preenche-se os vetores com valores aleatórios
        for i in tam:
            x[i]=randint(0,10)
            v[i]=randint(0,velMax) #o lim superior deve ser dado
            lBest[i]=x[i]
            gBest[i]=lBest[i]

        while condicao :
            for i in tam:
                #falta equacao de atualizacao de v
                x[i]+=v[i]
                if x[i] > gBest[i]:
                    gBest[i]=x[i] 
                if gBest[i] > lBest[i]:
                    lBest[i]=gBest[i]

        return lBest

class main:
    enxame1 = pso(100)
