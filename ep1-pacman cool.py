import random
import heapq

def generarLaberinto(rows, cols, obstacles_ratio=0.2):
    laberinto = [['.' for _ in range(cols)] for _ in range(rows)]
    num_obstacles = int(rows * cols * obstacles_ratio)
    
    for _ in range(num_obstacles):
        x, y = random.randint(0, rows - 1), random.randint(0, cols - 1)
        laberinto[x][y] = 'X'
    
    return laberinto

def posicionRandom(laberinto):
    rows, cols = len(laberinto), len(laberinto[0])
    while True:
        x, y = random.randint(0, rows - 1), random.randint(0, cols - 1)
        if laberinto[x][y] == '.':
            return (x, y)
#---------------------------------------------------------------------Calculo de las distancias
def distanciaManhattan(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def distanciaEuclidiana(a, b):
    return ((a[0] - b[0])**2 + (a[1] - b[1])**2) ** 0.5

def hillClimbing(laberinto, pacman, ghost):
    actual = pacman
    path = [actual]
    while actual != ghost:
        vecinos = [(actual[0] + dx, actual[1] + dy) 
                     for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]
                     if 0 <= actual[0] + dx < len(laberinto) and 0 <= actual[1] + dy < len(laberinto[0])
                     and laberinto[actual[0] + dx][actual[1] + dy] != 'X']
        
        sigMovimiento = min(vecinos, key=lambda n: distanciaManhattan(n, ghost), default=None)
        
        if not sigMovimiento or distanciaManhattan(sigMovimiento, ghost) >= distanciaManhattan(actual, ghost):
            break
        
        actual = sigMovimiento
        path.append(actual)
    return path

def aEstrella(laberinto, pacman, ghost):
    open_set = [(0, pacman)]  #costo, posicion
    origen = {}
    g_score = {pacman: 0}
    f_score = {pacman: distanciaEuclidiana(pacman, ghost)}
    #---------------------------
    while open_set:
        _, actual = heapq.heappop(open_set)
        if actual == ghost:
            path = []
            while actual in origen:
                path.append(actual)
                actual = origen[actual]
            path.append(pacman)
            return path[::-1]
        
        vecinos = [(actual[0] + dx, actual[1] + dy) 
                     for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]
                     if 0 <= actual[0] + dx < len(laberinto) and 0 <= actual[1] + dy < len(laberinto[0])
                     and laberinto[actual[0] + dx][actual[1] + dy] != 'X']
        
        for vecino in vecinos:
            tentative_g_score = g_score[actual] + (2 if vecino[0] != actual[0] else 1)
            
            if vecino not in g_score or tentative_g_score < g_score[vecino]:
                origen[vecino] = actual
                g_score[vecino] = tentative_g_score
                f_score[vecino] = tentative_g_score + distanciaEuclidiana(vecino, ghost)
                heapq.heappush(open_set, (f_score[vecino], vecino))
    return []

def mostrarLaberinto(laberinto, pacman, ghost, path=[]):
    display = [row[:] for row in laberinto]
    display[ghost[0]][ghost[1]] = 'Ϯ'
    for step in path:
        display[step[0]][step[1]] = '*'
    display[pacman[0]][pacman[1]] = 'Ỽ'
    
    for row in display:
        
        print('\t',' '.join(row))
    print()

def menuProblema3():
    rows, cols = 8, 8
    laberinto = generarLaberinto(rows, cols)
    pacman = posicionRandom(laberinto)
    ghost = posicionRandom(laberinto)
    
    print("\n\tLaberinto:")
    mostrarLaberinto(laberinto, pacman, ghost)
    
    opc = input("\tEscoge un algoritmo:\n\n\t\t1.- Hill Climbing\n\t\t2.- A*\n\n\t------> ")
    if opc == '1':
        path = hillClimbing(laberinto, pacman, ghost)
    else:
        path = aEstrella(laberinto, pacman, ghost)
    
    print("\n\tSolucion:")
    mostrarLaberinto(laberinto, pacman, ghost, path)

menuProblema3()
