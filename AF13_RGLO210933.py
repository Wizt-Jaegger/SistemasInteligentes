# Entrenar el perceptrón simple para clasificación de frutas: Manzana-1 y Naranja-0.
# El
# perceptrón aprenderá a clasificar frutas basándose en las siguientes cuatro características de entrada:
# •Peso: Ligero (0) o Pesado (1)
# •Textura: Lisa (0) o Rugosa (1)
# •Color: Rojo (0) o Naranja (1)
# •Diámetro: Pequeño (0) o Grande (1)
# Salida
# esperada:
# •1 (Manzana) si la fruta es pesada, lisa, roja y grande.
# •0 (Naranja) si la fruta es ligera, rugosa, naranja y pequeña. 
# Los datos de entrenamiento son los que se presentan en la imagen compartida.
# Evaluar el entrenamiento validando los resultados del modelo en la inferencia de entradas previamente aprendidas. 

import random

def generarPrimerosPesos():
    peso1 = random.randint(0,5)
    return peso1

def funcionActivacion(patron,W, umbral):
    # Escalon: y = sign(x) 
    sumatoria = patron[0]*W[0] + patron[1]*W[1] + patron[2]*W[2] + patron[3]*W[3] + umbral
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
            if y != patrones[i][4]:
                bandera=1
                #ajustamos peso y umbral
                W[0] = W[0] + ((patrones[i][4]-y)*patrones[i][0])
                W[1] = W[1] + ((patrones[i][4]-y)*patrones[i][1])
                W[2] = W[2] + ((patrones[i][4]-y)*patrones[i][2])
                W[3] = W[3] + ((patrones[i][4]-y)*patrones[i][3])
                umbral = umbral + (patrones[i][4]-y)
                print(W,umbral)
            iteraciones += 1
    return iteraciones, umbral

def inferencia(entrada, W,umbral):
    y = (entrada[0]*W[0]+entrada[1]*W[1]+entrada[2]*W[2]+entrada[3]*W[3]+umbral)
    if y>0:
        return 1
    else:
        return 0
patrones = [[1,0,0,1,1],[0,1,1,0,0],[1,0,0,0,1],[0,1,1,1,0],[1,0,0,1,1],[0,1,1,0,0],[1,0,0,1,1],[0,1,1,1,0]]    
# patrones = [[2,0,0,0,0],[3,1,1,1,1],[4,1,1,1,1],[1,0,0,0,0],[5,1,1,1,1],[6,1,1,1,1],[3,0,0,0,0],[4,0,0,0,0]]
W=[]
W.append(generarPrimerosPesos())
W.append(generarPrimerosPesos())
W.append(generarPrimerosPesos())
W.append(generarPrimerosPesos())
umbral = generarPrimerosPesos()
iteraciones, umbral = perceptron(patrones, W, umbral)
entrada=[1,1,1,1]
salida = inferencia(entrada,W,umbral)
print("Iteraciones: ",iteraciones)
print(W,umbral) 
print("Salida: ",salida)
