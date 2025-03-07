from random import random
from random import randint
#


   # 2.2 CRUZA : Se cruzan los cromosomas

  #  2.3 MUTACIÓN : Se mutan los cromosomas

 #   2.4 EVALUACIÓN : Evaluar la calidad de la solución

#    3 END WHILE

#0 INICIO : Crear población aleatoria de n cromosomas
def crearPoblacion(cantidadCromosomas):
    poblacion = []
    for i in range (cantidadCromosomas):
        poblacion.append(format(randint(0,31), f'0{5}b'))#aqui ya me queda todo en binario
    return poblacion
#1 FITNESS : Evaluar fitness f(x) para cada cromosoma en la población
def evaluarFitness(poblacion):
    fitness = []
    for ind in poblacion:
         #decodificar y aplicamos la funcion objetivo fx=x^2
        fitness.append(int(ind,2)**2)#basicamente es convertir en enteros otra vez y elevar al cuadrado
    return fitness

def seleccion(poblacion, fitness):
    nuevaPob=[]
    nuevaPob=seleccionRuleta(poblacion,fitness,len(poblacion))
    return nuevaPob
#def seleccionRango(poblacion, fitness):   
def seleccionRuleta(poblacion, fitness, tamPob):
    rangos = []
    nuevaPob=[]
    sumatoria = sum(fitness)
    rango = 0    
    for cromosoma, apt in zip(poblacion, fitness):#zip es como un indice
        rango = rango + (apt / sumatoria)
        rangos.append(rango)

    conteo = 0
    while (conteo < tamPob):
         # Generar número aleatorio entre 0 y 1
        conteo = conteo + 1
        posibleSeleccionado = randint(0, 1000) / 1000 
        rangoAnterior = False
        # Encontrar el índice del cromosoma más cercano
        for i, r in enumerate(rangos):#Nos da el índice i de cada elemento r en rangos
            
            if posibleSeleccionado <= r:
                if rangoAnterior == False:
                    nuevaPob.append(poblacion[i])
                rangoAnterior = True
               
                

    return nuevaPob
    
#def seleccionTorneo(poblacion, fitness):


def inicio():
    noResuelto = True
    poblacion = []
    poblacion = crearPoblacion(4)
    fitness = []
    fitness = evaluarFitness(poblacion)
    nuevaPob = []
    while (noResuelto):
        #2.1 SELECCIÓN : Basada en f(x)
        print("si entro al while")
        print(poblacion)
        nuevaPob = seleccion(poblacion, fitness)
        print(nuevaPob)
        noResuelto = False
        #2.2 CRUZA : Se cruzan los cromosomas
        #2.3 MUTACIÓN : Se mutan los cromosomas

inicio()