from random import random
from random import randint
def generarPoblacion(cantInd):
    poblacion=[]
    for i in range(4):
       poblacion.append(format(randint(0,31), f'0{5}b'))
    return poblacion

def evaluarPoblacion(poblacion):
    fitness=[]
    #recorro mi poblacion
    for ind in poblacion:
         #decodificar y aplicamos la funcion objetivo fx=x^2
        fitness.append(int(ind,2)**2)
    return fitness

def Seleccion(poblacion, fitness):
    nuevaPob=[]
    #se elige al mejor por elitismo
    indice=fitness.index(max(fitness))
    nuevaPob.append(poblacion[indice])
    for i in range(3):
      ind1=randint(0,3)
      ind2=randint(0,3)
      while(ind1==ind2):
        ind2=randint(0,3)
      #aplicamos torneo determinista
      if fitness[ind1]>fitness[ind2]:
           nuevaPob.append(poblacion[ind1])
      else:
           nuevaPob.append(poblacion[ind2])
    return nuevaPob
def Cruza(poblacion):
    nuevaPob=[]
    for i in range(2):
         padre1=randint(0,3)
         padre2=randint(0,3)
         while(padre1==padre2):
            padre2=randint(0,3)
         puntoCruce=randint(1,4)
         hijo1=poblacion[padre1][:puntoCruce]+poblacion[padre2][puntoCruce:]
         hijo2=poblacion[padre2][:puntoCruce]+poblacion[padre1][puntoCruce:]
         nuevaPob.append(hijo1)
         nuevaPob.append(hijo2)
    return nuevaPob
def Muta(poblacion):
    nuevaPob=[]
    for i in range(len(poblacion)):
        individuo=list(poblacion[i])
        #Se evalúa si muta o no el individuo
        if random()<=0.1:
           alelo=randint(0,4)

           if individuo[alelo]=='0':
              individuo[alelo]='1'
           else:
              individuo[alelo]='0'

        individuo=''.join(individuo)
        nuevaPob.append(individuo)
    return nuevaPob
def evaluacion(fitness):
    for fit in fitness:
      if fit==961:
         return True
    return False
#1.- Generar una población aleatoria de 4 individuos
poblacion=[]
poblacion=generarPoblacion(4)
#2.-Evaluar fitness
fitness=evaluarPoblacion(poblacion)
print(poblacion)
paro=False
generacion=0
while((paro!=True)and (generacion<=30)):
    #Seleccionar a los mejores individuos según su fitness, aplicar elitismo para el primer individuo, y torneo determinasta
    poblacion=Seleccion(poblacion,fitness)
    #Cruza de un solo punto, generación de dos hijos por pareja
    poblacion=Cruza(poblacion)
    #Muta de un solo gen con prob. 0.1 -10%
    poblacion=Muta(poblacion)
    fitness=evaluarPoblacion(poblacion)
    print(poblacion)
    paro=evaluacion(fitness)
    generacion=generacion+1