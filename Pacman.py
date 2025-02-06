import os
import platform
import random
import time
print("bienvenido usuario de ",platform.system())
#---------------------------------------------------------funciones de formato
def limpiar():
    varClear = "Clear"
    if platform.system() == "Windows":
        varClear = "cls"
    else:
        varClear = "clear"
    os.system(varClear)
#------------------------------------------------------------------------------------- definiendo que lleva mi nodo
class nodo:
    def __init__(self, valor,np):
        self.np=np 
        self.valor = valor
        self.hijos=[]

    def agregarHijo(self, hijo):
        self.hijos.append(hijo)
#------------------------------------------------------------------------------------- Declarar nodos que no sean una pared de pacman
#nota todos tienen nivel de profundidad 1 porque la profundidad dependera de cual es nodo raiz, entonces se debe asignar despues de definir el nodo raiz y meta

nodoA1 = nodo(('A',1),1)
nodoA2 = nodo(('A',2),1)
nodoA3 = nodo(('A',3),1)
nodoA4 = nodo(('A',4),1)
nodoA6 = nodo(('A',6),1)
nodoA7 = nodo(('A',7),1)
nodoA8 = nodo(('A',8),1)
nodoB1 = nodo(('B',1),1)
nodoB4 = nodo(('B',4),1)
nodoB6 = nodo(('B',6),1)
nodoB8 = nodo(('B',8),1)
nodoC1 = nodo(('C',1),1)
nodoC3 = nodo(('C',3),1)
nodoC4 = nodo(('C',4),1)
nodoC6 = nodo(('C',6),1)
nodoC8 = nodo(('C',8),1)
nodoD1 = nodo(('D',1),1)
nodoD6 = nodo(('D',6),1)
nodoD8 = nodo(('D',8),1)
nodoE1 = nodo(('E',1),1)
nodoE2 = nodo(('E',2),1)
nodoE3 = nodo(('E',3),1)
nodoE4 = nodo(('E',4),1)
nodoE5 = nodo(('E',5),1)
nodoE6 = nodo(('E',6),1)
nodoF1 = nodo(('F',1),1)
nodoF4 = nodo(('F',4),1)
nodoF8 = nodo(('F',8),1)
nodoG1 = nodo(('G',1),1)
nodoG2 = nodo(('G',2),1)
nodoG4 = nodo(('G',4),1)
nodoG5 = nodo(('G',5),1)
nodoG6 = nodo(('G',6),1)
nodoG8 = nodo(('G',8),1)
nodoH5 = nodo(('H',5),1)
nodoH6 = nodo(('H',6),1)
nodoH7 = nodo(('H',7),1)
nodoH8 = nodo(('H',8),1)


#Ejemplo de calculo de nivel de profundidad
def calcularNivelesProfundidad(raiz):
    if raiz is None:
        return 0
    else:
        for hijo in raiz.hijos:
            hijo.np = raiz.np + 1
            calcularNivelesProfundidad(hijo)
        return 1 + max(calcularNivelesProfundidad(hijo) for hijo in raiz.hijos) if raiz.hijos else 0

#------------------------------------------------------------------------------------- Validar si son nodos pared

def validarPared(numero, letra):
    paredes = [(2, 'B'), (3, 'B'), (2, 'C'), (2, 'D'), (3, 'D'), (4, 'D'), (5, 'D'), (5, 'C'), (5, 'B'), (5, 'A'), (2, 'F'), (3, 'F'), (3, 'G'), (1, 'H'), (2, 'H'), (3, 'H'), (4, 'H'), (7, 'B'), (7, 'C'), (7, 'D'), (7, 'E'), (8, 'E'), (5, 'F'), (6, 'F'), (7, 'F'), (7, 'G')]
    return (numero, letra) not in paredes    
#------------------------------------------------------------------------------------- Generacion dinamica de pacman y fantasma
#--------- Generar fantasma
def generarNodoRaiz():
    while True:
        numRaiz = random.randint(1, 8)
        letraRaiz = random.choice(['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H'])
        if validarPared(numRaiz, letraRaiz):
            nodoMeta = generarNodoMeta()
            if (numRaiz, letraRaiz) != nodoMeta.valor:
                raiz = nodo((numRaiz, letraRaiz), 1)
                construirArbol(raiz, nodoMeta)
                calcularNivelesProfundidad(raiz)
                return raiz, nodoMeta
#-----------Generar el pacman
def generarNodoMeta():
    while True:
        numMeta = random.randint(1, 8)
        letraMeta = random.choice(['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H'])
        if validarPared(numMeta, letraMeta):
            return nodo((numMeta, letraMeta), 1)
        

def construirArbol(raiz, meta):
    # Aquí se debe implementar la lógica para construir el árbol
    #no estoy seguro porque depende de la generacion de raiz y meta
    pass
#-----------------------------------------------------------------------Impresion
def imprimirLaberinto(raiz, meta):
    laberinto = [['.' for _ in range(8)] for _ in range(8)]
    for i in range(8):
        for j in range(8):
            if not validarPared(i+1, chr(ord('A')+j)):
                laberinto[i][j] = 'X'
    x, y = raiz.valor
    laberinto[x-1][ord(y)-ord('A')] = 'Ϯ'
    x, y = meta.valor
    laberinto[x-1][ord(y)-ord('A')] = 'Ỽ'
    for fila in laberinto:
        print(' '.join(fila))
    print()
    #para testing, hill climbing sera reemplazado por profundidad

def hillclimbing(raiz, meta):
    print("Busqueda en profundidad izquierda simulando hill")
    agenda = []
    agenda.append(raiz)
    nodoMeta = meta
    
    while len(agenda) > 0:
        nodoVisitado = agenda.pop()
        valor = nodoVisitado.valor
        print("Nodo visitado:")
        #limpiar()
        imprimirLaberinto(raiz, meta)
        time.sleep(1)
        if nodoVisitado.valor == nodoMeta:
            break
        else:
            for hijo in reversed(nodoVisitado.hijos):
                agenda.append(hijo)

def menu():
    raiz, meta = generarNodoRaiz()
    while True:
        opt= input("\nDeseas jugar pacman?\n\t1= Si\n\t0=No")
        if opt == 1:
            hillclimbing()
        else:
            break