import os
import platform
import random
import time
import math

# Función para limpiar la pantalla
def limpiar():
    varClear = "clear"
    if platform.system() == "Windows":
        varClear = "cls"
    os.system(varClear)
    
def enter():
    input("\npresiona ENTER para continuar\n")
    limpiar()

# Clase para definir un nodo
class NodoPacman:
    def __init__(self, valor, np):
        self.np = np  # Nivel de profundidad
        self.valor = valor  # Coordenadas (fila, columna)
        self.hijosPacman = []  # Lista de nodos hijos
        self.g = 0  # Costo acumulado (para A*)
        self.f = 0  # Función de evaluación (para A*)

    def agregarHijoPacman(self, hijoPacman):
        self.hijosPacman.append(hijoPacman)

# Declarar todos los nodos válidos (no paredes)
nodosPacman = {
    'A1': NodoPacman(('A', 1), 1),
    'A2': NodoPacman(('A', 2), 1),
    'A3': NodoPacman(('A', 3), 1),
    'A4': NodoPacman(('A', 4), 1),
    'A6': NodoPacman(('A', 6), 1),
    'A7': NodoPacman(('A', 7), 1),
    'A8': NodoPacman(('A', 8), 1),
    'B1': NodoPacman(('B', 1), 1),
    'B4': NodoPacman(('B', 4), 1),
    'B6': NodoPacman(('B', 6), 1),
    'B8': NodoPacman(('B', 8), 1),
    'C1': NodoPacman(('C', 1), 1),
    'C3': NodoPacman(('C', 3), 1),
    'C4': NodoPacman(('C', 4), 1),
    'C6': NodoPacman(('C', 6), 1),
    'C8': NodoPacman(('C', 8), 1),
    'D1': NodoPacman(('D', 1), 1),
    'D6': NodoPacman(('D', 6), 1),
    'D8': NodoPacman(('D', 8), 1),
    'E1': NodoPacman(('E', 1), 1),
    'E2': NodoPacman(('E', 2), 1),
    'E3': NodoPacman(('E', 3), 1),
    'E4': NodoPacman(('E', 4), 1),
    'E5': NodoPacman(('E', 5), 1),
    'E6': NodoPacman(('E', 6), 1),
    'F1': NodoPacman(('F', 1), 1),
    'F4': NodoPacman(('F', 4), 1),
    'F8': NodoPacman(('F', 8), 1),
    'G1': NodoPacman(('G', 1), 1),
    'G2': NodoPacman(('G', 2), 1),
    'G4': NodoPacman(('G', 4), 1),
    'G5': NodoPacman(('G', 5), 1),
    'G6': NodoPacman(('G', 6), 1),
    'G8': NodoPacman(('G', 8), 1),
    'H5': NodoPacman(('H', 5), 1),
    'H6': NodoPacman(('H', 6), 1),
    'H7': NodoPacman(('H', 7), 1),
    'H8': NodoPacman(('H', 8), 1),
}

# Función para obtener un nodo por su valor (coordenadas)
def obtenerNodoPacman(valor):
    clave = f"{valor[0]}{valor[1]}"
    return nodosPacman.get(clave, None)

# Función para construir el arbol/grafo pacman
def construirArbol(raizPacman, metaPacman):
    movimientos = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # Arriba, abajo, izquierda, derecha
    filaLetra, columna = raizPacman.valor
    filaNum = ord(filaLetra) - ord('A') + 1  # Convertir fila (letra) a numero
    for movimiento in movimientos:
        nuevaFilaNum = filaNum + movimiento[0]
        nuevaColumna = columna + movimiento[1]
        if 1 <= nuevaFilaNum <= 8 and 1 <= nuevaColumna <= 8:
            nuevaFilaLetra = chr(ord('A') + nuevaFilaNum - 1)  # Convertir numero a letra
            nuevoNodoPacman = obtenerNodoPacman((nuevaFilaLetra, nuevaColumna))
            if nuevoNodoPacman and nuevoNodoPacman not in raizPacman.hijosPacman:
                raizPacman.agregarHijoPacman(nuevoNodoPacman)
                construirArbol(nuevoNodoPacman, metaPacman)

# Funcion heuristica (distancia Manhattan, distancia euclidiana)
def heuristicaManhattan(nodoPacman, metaPacman):
    filaNodoPacman = ord(nodoPacman.valor[0]) - ord('A') + 1
    columnaNodoPacman = nodoPacman.valor[1]
    filaMetaPacman = ord(metaPacman.valor[0]) - ord('A') + 1
    columnaMetaPacman = metaPacman.valor[1]
    return abs(filaNodoPacman - filaMetaPacman) + abs(columnaNodoPacman - columnaMetaPacman)

def heuristicaEuclidiana(nodoPacman, metaPacman):
    filaNodoPacman = ord(nodoPacman.valor[0]) - ord('A') + 1
    columnaNodoPacman = nodoPacman.valor[1]
    filaMetaPacman = ord(metaPacman.valor[0]) - ord('A') + 1
    columnaMetaPacman = metaPacman.valor[1]
    return math.sqrt((filaNodoPacman - filaMetaPacman)**2 + (columnaNodoPacman - columnaMetaPacman)**2)

def imprimirLaberinto(raizPacman, metaPacman, camino=None):
    laberinto = [['.' for _ in range(8)] for _ in range(8)]
    for i in range(8):
        for j in range(8):
            if not obtenerNodoPacman((chr(ord('A') + i), j + 1)):
                laberinto[i][j] = 'X'  # Paredes
    x, y = raizPacman.valor
    laberinto[ord(x) - ord('A')][y - 1] = 'Ỽ'  # Fantasma
    x, y = metaPacman.valor
    laberinto[ord(x) - ord('A')][y - 1] = 'Ϯ'  # Pac-Man

    if camino:
        for paso in camino:
            x, y = paso
            laberinto[ord(x) - ord('A')][y - 1] = '*'  # Marcar el camino

    for fila in laberinto:
        print(' '.join(fila))
    print()

def hillClimbing(raizPacman, metaPacman):
    print("Búsqueda con Hill Climbing mejorada")
    actual = raizPacman
    visitados = set()
    camino = [actual.valor]  # Lista para almacenar el camino recorrido
    
    while True:
        if actual.valor == metaPacman.valor:
            print("¡Fantasma ha sido desvivido!")
            imprimirLaberinto(raizPacman, metaPacman, camino)
            break
            
        visitados.add(actual.valor)
        
        opciones = [(hijoPacman, heuristicaManhattan(hijoPacman, metaPacman)) 
                   for hijoPacman in actual.hijosPacman 
                   if hijoPacman.valor not in visitados]
        
        if not opciones:
            print("No hay más nodos para explorar.")
            imprimirLaberinto(raizPacman, metaPacman, camino)
            break
            
        opciones.sort(key=lambda x: x[1])
        opcion, _ = opciones[0]
        actual = opcion
        camino.append(actual.valor)  # Agregar el nodo actual al camino
        
        print("Nodo actual:", actual.valor)
        limpiar()
        imprimirLaberinto(actual, metaPacman)
        time.sleep(1)

def aEstrella(raizPacman, metaPacman):
    print("Búsqueda con A*")
    abiertos = []
    cerrados = set()
    raizPacman.g = 0
    raizPacman.f = heuristicaEuclidiana(raizPacman, metaPacman)
    abiertos.append(raizPacman)
    camino = []  # Lista para almacenar el camino recorrido

    while abiertos:
        actual = min(abiertos, key=lambda x: x.f)
        abiertos.remove(actual)
        cerrados.add(actual.valor)
        camino.append(actual.valor)  # Agregar el nodo actual al camino

        print("Nodo actual:", actual.valor)
        limpiar()
        imprimirLaberinto(actual, metaPacman)
        time.sleep(1)

        if actual.valor == metaPacman.valor:
            print("¡Fantasma comido!")
            imprimirLaberinto(raizPacman, metaPacman, camino)
            break

        for hijoPacman in actual.hijosPacman:
            if hijoPacman.valor in cerrados:
                continue

            g_tentativo = actual.g + 1
            if hijoPacman not in abiertos or g_tentativo < hijoPacman.g:
                hijoPacman.g = g_tentativo
                hijoPacman.f = hijoPacman.g + heuristicaEuclidiana(hijoPacman, metaPacman)
                if hijoPacman not in abiertos:
                    abiertos.append(hijoPacman)

# Menú principal pacman
def menuPacman():
    while True:
        time.sleep(2)
        limpiar()
        enter()
        opt = input("\n¿Deseas jugar Pac-Man?\n\t1 = Hill Climbing\n\t2 = A*\n\t0 = Salir\n")
        if opt == '1' or opt == '2':
            raizPacman = random.choice(list(nodosPacman.values()))
            metaPacman = random.choice(list(nodosPacman.values()))
            while metaPacman.valor == raizPacman.valor:
                metaPacman = random.choice(list(nodosPacman.values()))
            construirArbol(raizPacman, metaPacman)
            if opt == '1':
                hillClimbing(raizPacman, metaPacman)
            else:
                aEstrella(raizPacman, metaPacman)
        elif opt == '0':
            limpiar()
            print("¡Gracias por jugar!")
            time.sleep(2)
            limpiar()
            break
        else:
            print("Opción no válida. Intenta de nuevo.")

menuPacman()