import random
from math import exp

class simulatedAnnealing:
    '''
    variaveis de entrada
    s0 = entrada, configuração inicial
    s = conf final
    to = temp inicial
    ti = temp na iteração
    m = num max de iterações
    p = num max de pertubações
    l = num maximo de sucessoes
    alfa = fator de redução da temp
    nSucesso = contador de sucesso em iteração
    '''
    def __init__(self,s0,m,p,l,alfa):
        self.s0 = s0
        self.m = m
        self.p = p
        self.l = l
        self.alfa = alfa
       
    #função que gera a temperatura inicial
    def tempInicial():

    #realiza uma perturbação na solução s
    def perturba():
    
    #necessário definir
    def funcaoObjetivo():

    def gerarAleatorio():
        random.uniform(0,1) #gera um float entre os dois nums

    def main():
        t0= tempInicial()
        t = t0
        j=1
        S=s0
        while(nSucesso = 0 || j >m):
            i = 1
            nSucesso = 0
            while(nSucesso >= l || i>p):
                s[i] = perturba(S)
                deltaF[i] = funcaoObjetivo(S[i]) - funcaoObjetivo(S)
                if(deltaF[i] <= 0 || (exp(-delta[i]/T) > gerarAleatorio())
                        S= s[i]
                        nSucesso++
                i++
    print(S)

