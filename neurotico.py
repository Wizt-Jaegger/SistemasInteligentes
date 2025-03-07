#Modelo de red neuronal simple de McCulloch-Pitts
#Compuerta OR
from random import randint

def generarPrimerosPesos():
    peso1 = randint(0,5)
    return peso1

def funcionActivacion(patrones,W, umbral):
    # Escalon: y = sign(x) 
    sumatoria = patrones[0]*W[0] + patrones[1]*W[1] + umbral
    if (sumatoria>0):
        return 1
    else:
        return 0
    
def perceptron (patrones, W, umbral):
    bandera=1
    while (bandera==1):
        bandera=0
        iteraciones=0
        for i in range(len(patrones)):
            y = funcionActivacion(patrones[i],W,umbral)
            if y != patrones[i][2]:
                bandera=1
                #ajustamos peso y umbral
                W[0] = W[0] + ((patrones[i][2]-y)*patrones[i][0])
                W[1] =W[1] + ((patrones[i][2]-y)*patrones[i][1])
                umbral = umbral + (patrones[i][2]-y)
                print(W,umbral)
            iteraciones += 1
    return iteraciones, umbral

def inferencia(entrada, W,umbral):
    y = (entrada[0]*W[0]+entrada[1]*W[1]+umbral)
    if y>0:
        return 1
    else:
        return 0
    
patrones = [[2,0,0],[3,1,1],[4,1,1],[1,0,0],[5,1,1],[6,1,1],[3,0,0],[4,0,0]]
W=[]
W.append(generarPrimerosPesos())
W.append(generarPrimerosPesos())
umbral = generarPrimerosPesos()
iteraciones, umbral = perceptron(patrones, W, umbral)
entrada=[1,1]
salida = inferencia(entrada,W,umbral)
print("Iteraciones: ",iteraciones)
print(W,umbral)
print("Salida: ",salida)
