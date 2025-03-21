from random import random
from random import randint

def generarPoblacion(cantInd):
    poblacion = []
    for i in range(cantInd):
        poblacion.append(format(randint(0, 31), f'0{5}b'))
    return poblacion

def evaluarPoblacion(poblacion):
    fitness = []
    for ind in poblacion:
        fitness.append(int(ind, 2) ** 2) 
    return fitness
def SeleccionRango(poblacion, fitness):
    sumaFitness = sum(fitness)
    
def SeleccionRuleta(poblacion, fitness):
    sumaFitness = sum(fitness)
    probabilidadAcumulada = []
    acumulado = 0
    
    for aptitud in fitness:
        acumulado += aptitud / sumaFitness
        probabilidadAcumulada.append(acumulado)

    nuevaPob = []
    for _ in range(2):  
        r = randint(0, 100) / 100
        for i, probabilidad in enumerate(probabilidadAcumulada):
            if r <= probabilidad:
                nuevaPob.append(poblacion[i])
                break
    
    return nuevaPob

def SeleccionTorneoProb(poblacion, fitness):
    nuevaPob = []
    
    # Seleccion mediante torneo para 2 individuos
    for _ in range(2):
        ind1 = randint(0, 3)
        ind2 = randint(0, 3)
        while ind1 == ind2:
            ind2 = randint(0, 3)
        if fitness[ind1] > fitness[ind2]:
            nuevaPob.append(poblacion[ind1])
        else:
            nuevaPob.append(poblacion[ind2])
    
    return nuevaPob


def Cruza(poblacion):
    nuevaPob = []
    for i in range(2):  # Para cada pareja, generamos dos hijos
        padre1 = randint(0, 3)
        padre2 = randint(0, 3)
        while padre1 == padre2:
            padre2 = randint(0, 3)
        puntoCruce = randint(1, 4)
        hijo1 = poblacion[padre1][:puntoCruce] + poblacion[padre2][puntoCruce:]
        hijo2 = poblacion[padre2][:puntoCruce] + poblacion[padre1][puntoCruce:]
        nuevaPob.append(hijo1)
        nuevaPob.append(hijo2)
    
    return nuevaPob

def Muta(poblacion):
    nuevaPob = []
    for i in range(len(poblacion)):
        individuo = list(poblacion[i])
        if random() <= 0.1:  # Probabilidad de mutación del 10%
            alelo = randint(0, 4)
            individuo[alelo] = '1' if individuo[alelo] == '0' else '0'
        nuevaPob.append(''.join(individuo))
    return nuevaPob

def evaluacion(fitness):
    for fit in fitness:
        if fit == 961:  # Condición de paro (si se alcanza el valor 961)
            return True
    return False

# 1.- Generar una población aleatoria de 4 individuos
poblacion = generarPoblacion(4)

# 2.- Evaluar fitness
fitness = evaluarPoblacion(poblacion)
print(f"Poblacion inicial: {poblacion}")
paro = False
generacion = 0

while not paro and generacion <= 30:
    # 2 por ruleta
    poblacion_ruleta = SeleccionRuleta(poblacion, fitness)
    print(f"Seleccion por ruleta: {poblacion_ruleta}")
    # 2 por torneo
    poblacion_torneo = SeleccionTorneoProb(poblacion, fitness)
    print(f"Seleccion por torneo: {poblacion_torneo}")
    
    poblacion = poblacion_ruleta + poblacion_torneo
    
    print(f"Seleccion final: {poblacion}")
    poblacion = Cruza(poblacion)
    print(f"Cruza: {poblacion}")
    poblacion = Muta(poblacion)
    print(f"Mutacion: {poblacion}")
    
    fitness = evaluarPoblacion(poblacion)
    print(f"Generacion {generacion}: {poblacion}")
    
    paro = evaluacion(fitness)
    
    generacion += 1
#recuperar a los individuos para poderlosmeter dentro de la lista y la unica forma de relacionarlos es a travez de sus indices