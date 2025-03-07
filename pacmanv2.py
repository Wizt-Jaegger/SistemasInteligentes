import os
import platform
import random
import time

# Función para limpiar la pantalla
def limpiar():
    varClear = "clear"
    if platform.system() == "Windows":
        varClear = "cls"
    os.system(varClear)

# Clase para definir un nodo
class Nodo:
    def __init__(self, valor, np):
        self.np = np  # Nivel de profundidad
        self.valor = valor  # Coordenadas (fila, columna)
        self.hijos = []  # Lista de nodos hijos

    def agregarHijo(self, hijo):
        self.hijos.append(hijo)

# Declarar todos los nodos válidos (no paredes)
nodos = {
    'A1': Nodo(('A', 1), 1),
    'A2': Nodo(('A', 2), 1),
    'A3': Nodo(('A', 3), 1),
    'A4': Nodo(('A', 4), 1),
    'A6': Nodo(('A', 6), 1),
    'A7': Nodo(('A', 7), 1),
    'A8': Nodo(('A', 8), 1),
    'B1': Nodo(('B', 1), 1),
    'B4': Nodo(('B', 4), 1),
    'B6': Nodo(('B', 6), 1),
    'B8': Nodo(('B', 8), 1),
    'C1': Nodo(('C', 1), 1),
    'C3': Nodo(('C', 3), 1),
    'C4': Nodo(('C', 4), 1),
    'C6': Nodo(('C', 6), 1),
    'C8': Nodo(('C', 8), 1),
    'D1': Nodo(('D', 1), 1),
    'D6': Nodo(('D', 6), 1),
    'D8': Nodo(('D', 8), 1),
    'E1': Nodo(('E', 1), 1),
    'E2': Nodo(('E', 2), 1),
    'E3': Nodo(('E', 3), 1),
    'E4': Nodo(('E', 4), 1),
    'E5': Nodo(('E', 5), 1),
    'E6': Nodo(('E', 6), 1),
    'F1': Nodo(('F', 1), 1),
    'F4': Nodo(('F', 4), 1),
    'F8': Nodo(('F', 8), 1),
    'G1': Nodo(('G', 1), 1),
    'G2': Nodo(('G', 2), 1),
    'G4': Nodo(('G', 4), 1),
    'G5': Nodo(('G', 5), 1),
    'G6': Nodo(('G', 6), 1),
    'G8': Nodo(('G', 8), 1),
    'H5': Nodo(('H', 5), 1),
    'H6': Nodo(('H', 6), 1),
    'H7': Nodo(('H', 7), 1),
    'H8': Nodo(('H', 8), 1),
}

# Función para obtener un nodo por su valor (coordenadas)
def obtenerNodo(valor):
    clave = f"{valor[0]}{valor[1]}"
    return nodos.get(clave, None)

# Función para construir el árbol/grafo
def construirArbol(raiz, meta):
    movimientos = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # Arriba, abajo, izquierda, derecha
    fila_letra, columna = raiz.valor
    fila_num = ord(fila_letra) - ord('A') + 1  # Convertir fila (letra) a número
    for movimiento in movimientos:
        nueva_fila_num = fila_num + movimiento[0]
        nueva_columna = columna + movimiento[1]
        if 1 <= nueva_fila_num <= 8 and 1 <= nueva_columna <= 8:
            nueva_fila_letra = chr(ord('A') + nueva_fila_num - 1)  # Convertir número a letra
            nuevo_nodo = obtenerNodo((nueva_fila_letra, nueva_columna))
            if nuevo_nodo and nuevo_nodo not in raiz.hijos:
                raiz.agregarHijo(nuevo_nodo)
                construirArbol(nuevo_nodo, meta)

# Función para imprimir el laberinto
def imprimirLaberinto(raiz, meta):
    laberinto = [['.' for _ in range(8)] for _ in range(8)]
    for i in range(8):
        for j in range(8):
            if not obtenerNodo((chr(ord('A') + i), j + 1)):
                laberinto[i][j] = 'X'  # Paredes
    x, y = raiz.valor
    laberinto[ord(x) - ord('A')][y - 1] = 'Ϯ'  # Fantasma
    x, y = meta.valor
    laberinto[ord(x) - ord('A')][y - 1] = 'Ỽ'  # Pac-Man
    for fila in laberinto:
        print(' '.join(fila))
    print()

# Función de búsqueda en profundidad (DFS)
def hillclimbing(raiz, meta):
    print("Búsqueda en profundidad izquierda simulando Hill Climbing")
    agenda = []
    agenda.append(raiz)
    visitados = set()

    while agenda:
        nodoVisitado = agenda.pop()
        if nodoVisitado.valor in visitados:
            continue
        visitados.add(nodoVisitado.valor)
        print("Nodo visitado:", nodoVisitado.valor)
        limpiar()
        imprimirLaberinto(nodoVisitado, meta)
        time.sleep(1)
        if nodoVisitado.valor == meta.valor:
            print("¡Pac-Man encontrado!")
            break
        for hijo in reversed(nodoVisitado.hijos):
            if hijo.valor not in visitados:
                agenda.append(hijo)

# Menú principal
def menu():
    while True:
        opt = input("\n¿Deseas jugar Pac-Man?\n\t1 = Sí\n\t0 = No\n")
        if opt == '1':
            raiz = random.choice(list(nodos.values()))
            meta = random.choice(list(nodos.values()))
            while meta.valor == raiz.valor:
                meta = random.choice(list(nodos.values()))
            construirArbol(raiz, meta)
            hillclimbing(raiz, meta)
        else:
            print("¡Gracias por jugar!")
            break

menu()