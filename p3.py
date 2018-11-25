#Implementação de RNA - MLP

x = [0.2, 0.3]        #Entradas, x1 e x2
bias = 0.7            #bias dos neuronios
wx1 = [0.2,0.1]       #Pesos associados a entrada x1, w1 e w3
wx2 = [0.5,0.3]       #Pesos associados a x2, w2 e w4
alpha = 0.1           #Taxa de aprendizado
d =[0,1]              #Saida desejada, y1 e y2

def degrau(num):
    return 1 if num >= 0 else 0

def neuronio(ent1, ent2, peso1, peso2, bias):
    u = ent1*peso1+ ent2*peso2 - bias

    saida = degrau(u)

    return saida

def main():
    y=[0,0]
    erro = 0

    for i in range(0,2):
        y[i]=neuronio(x[i],wx1[i],wx2[i],bias)
        erro +=((d[i] - y[i])**2)  
        wx1[i]+= erro*alpha*x[0]
        wx2[i] += erro*alpha*x[1]
        bias += erro*alpha        
