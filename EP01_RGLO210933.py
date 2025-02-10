import os
import platform
import random
import time
import math
print("bienvenido usuario de ",platform.system())
#---------------------------------------------------------funciones de formato
import os
import platform

def limpiar():
    if platform.system() == "Windows":
        os.system("cls")
    else:
        print("\033c", end="")  # Código ANSI para limpiar la pantalla


def enter():
    input("\npresiona ENTER para continuar\n")
    limpiar()
#------------------------------------------------------------nodos
class nodo:
    def __init__(self, valor,np):
        self.np=np 
        self.valor = valor
        self.hijos=[]

    def agregarHijo(self, hijo):
        self.hijos.append(hijo)
#------------------------------------------------------------construccion de arbol
raiz = nodo('A5',0)
nodo2 = nodo('A7',1)
nodo3 = nodo('B1',1)
nodo4 = nodo('G1',1)
nodo5 = nodo('C1',1)
nodo6 = nodo('H3',1)
nodo7 = nodo('D1',1)
nodo8 = nodo('C5',1)
nodo9 = nodo('H2',1)
nodo10 = nodo('C7',1)
nodo11 = nodo('B5',1)
nodo12 = nodo('C10',1)
nodo13 = nodo('D6',1)
nodo14 = nodo('H5',1)
nodo15 = nodo('B8',1)
nodo16 = nodo('H8',1)
nodo17 = nodo('I4',1)
nodo18 = nodo('B9',1)
nodo19 = nodo('B6',1)
nodo20 = nodo('I9',1)
nodo21 = nodo('I6',1)

raiz.agregarHijo(nodo2)
raiz.agregarHijo(nodo3)
nodo3.agregarHijo(nodo4)
nodo3.agregarHijo(nodo5)
nodo4.agregarHijo(nodo6)
nodo4.agregarHijo(nodo7)
nodo6.agregarHijo(nodo8)
nodo6.agregarHijo(nodo9)
nodo8.agregarHijo(nodo10)
nodo8.agregarHijo(nodo11)
nodo10.agregarHijo(nodo12)
nodo10.agregarHijo(nodo13)
nodo12.agregarHijo(nodo14)
nodo12.agregarHijo(nodo15)
nodo14.agregarHijo(nodo16)
nodo14.agregarHijo(nodo17)
nodo15.agregarHijo(nodo18)
nodo15.agregarHijo(nodo19)
nodo16.agregarHijo(nodo20)
nodo16.agregarHijo(nodo21)

#------------------------------------------------------------calcular niveles de profundidad 
def calcularNivelesProfundidad(raiz):
    if raiz is None:
        return 0
    else:
        
        for hijo in raiz.hijos:
            hijo.np = raiz.np + 1 
            calcularNivelesProfundidad(hijo)
        return 1 + max(calcularNivelesProfundidad(hijo) for hijo in raiz.hijos) if raiz.hijos else 0
#------------------------------------------------------------busquedas ciegas

def busquedaProfundidadIzquierda(raiz, nodoMeta):
    print("Busqueda en profundidad izquierda")
    agenda = []
    agenda.append(raiz)
    while (len(agenda) > 0):
        nodoVisitado = agenda.pop()
        print("Nodo visitado: ", nodoVisitado.valor)
        if nodoVisitado.valor == nodoMeta:
            
            break
        else :
            for hijo in reversed(nodoVisitado.hijos):
                agenda.append(hijo)

def busquedaProfundidadDerecha(raiz, nodoMeta):
    print("Busqueda en profundidad derecha")
    agenda = []
    agenda.append(raiz)
    while (len(agenda) > 0):
        nodoVisitado = agenda.pop()
        print("Nodo visitado: ", nodoVisitado.valor)
        if nodoVisitado.valor == nodoMeta:
            
            break
        else :
            for hijo in (nodoVisitado.hijos):
                agenda.append(hijo)

def busquedaAnchuraIzquierda(raiz,nodoMeta):
    print("Busqueda en anchura izquierda")
    #es con cola
    agenda = []
    agenda.append(raiz)
    while (len(agenda) > 0):
        nodoVisitado = agenda.pop(0)    
        print("Nodo visitado: ", nodoVisitado.valor)
        if nodoVisitado.valor == nodoMeta:
            
            break
        else :
            for hijo in nodoVisitado.hijos:
                agenda.append(hijo)

def busquedaAnchuraDerecha(raiz, nodoMeta):
    print("\nBusqueda en anchura derecha\n")
    #es con cola
    agenda = []
    agenda.append(raiz)
    while (len(agenda) > 0):
        nodoVisitado = agenda.pop(0)    
        print("\tNodo visitado: ", nodoVisitado.valor)
        if nodoVisitado.valor == nodoMeta:
            
            break
        else :
            for hijo in reversed(nodoVisitado.hijos):
                agenda.append(hijo)

def busquedaProfundidadLimitadaIzquierda(raiz, lim, nodoMeta):
    
    agenda = []
    agenda.append(raiz)
    
    var = False
    while (len(agenda) > 0):
        nodoVisitado = agenda.pop()
        print("\tNodo visitado: ", nodoVisitado.valor," nivel de profundidad: ",nodoVisitado.np)
        if nodoVisitado.valor == nodoMeta:
            var = True
            break
        else :
            for hijo in reversed(nodoVisitado.hijos):
                calcularNivelesProfundidad(hijo)
                if hijo.np <= lim:
                    agenda.append(hijo)
    return var
def busquedaProfundidadLimitadaDerecha(raiz, lim, nodoMeta):
    
    agenda = []
    agenda.append(raiz)
    
    var = False
    while (len(agenda) > 0):
        nodoVisitado = agenda.pop()
        print("\tNodo visitado: ", nodoVisitado.valor," nivel de profundidad: ",nodoVisitado.np)
        if nodoVisitado.valor == nodoMeta:
            var = True
            break
        else :
            for hijo in (nodoVisitado.hijos):
                calcularNivelesProfundidad(hijo)
                if hijo.np <= lim:
                    agenda.append(hijo)
    return var

def busquedaProfundidadIterada(raiz, num, nodoMeta):
    if num == 1:
        print("\nBusqueda en profundidad iterada izquierda\n")
    else:
        print("\nBusqueda en profundidad iterada derecha\n")
    agenda = []
    agenda.append(raiz)
    lim = 0
    flag = False
    while not (flag) :
        if num == 1:
            flag = busquedaProfundidadLimitadaIzquierda(raiz, lim, nodoMeta)
        if num == 2:
            flag = busquedaProfundidadLimitadaDerecha(raiz, lim, nodoMeta)
        lim = lim + 1
#------------------------------------------------------------menus
def menuCiega():
    while True:
        enter()

        print("\nSeleccione el tipo de busqueda ciega:")
        print("\n\t1. Búsqueda en profundidad")
        print("\n\t2. Búsqueda en anchura")
        print("\n\t3. Búsqueda en profundidad limitada")
        print("\n\t4. Búsqueda en profundidad iterada")
        print("\n\t0. Salir")

        try:
            opt_ciega = int(input("\n\tIngrese el número de la opción: "))

            if opt_ciega == 0:
                print("Saliendo...")
                break

            enter() 
            print("\nIzquierda o derecha:")
            print("\n\t1. Izquierda")
            print("\n\t2. Derecha")

            orientacion = int(input("\n\tIngrese 1 o 2: "))

            enter() 
            objetivo = 'A5'
            objetivo = input("\nIngrese el nodo objetivo: ")

            if opt_ciega == 1:
                if orientacion == 1:
                    busquedaProfundidadIzquierda(raiz, objetivo)
                elif orientacion == 2:
                    busquedaProfundidadDerecha(raiz, objetivo)
                else:
                    print("\nOpción de orientación no válida.")

            elif opt_ciega == 2:
                if orientacion == 1:
                    busquedaAnchuraIzquierda(raiz, objetivo)
                elif orientacion == 2:
                    busquedaAnchuraDerecha(raiz, objetivo)
                else:
                    print("\nOpción de orientación no válida.")

            elif opt_ciega == 3:
                limite = int(input("\nIngrese el limite de profundidad: "))
                if orientacion == 1:
                    print("\nBusqueda en profundidad limitada izquierda\n")
                    busquedaProfundidadLimitadaIzquierda(raiz, limite, objetivo)
                elif orientacion == 2:
                    print("\nBusqueda en profundidad limitada derecha\n")
                    busquedaProfundidadDerecha(raiz,limite, objetivo)
                else:
                    print("\nOpción de orientación no válida.")

            elif opt_ciega == 4:
                if orientacion == 1:
                    busquedaProfundidadIterada(raiz,1, objetivo)
                elif orientacion == 2:
                    busquedaProfundidadIterada(raiz,2, objetivo)
                else:
                    print("\nOpción de orientación no válida.")

            else:
                print("\nOpción de búsqueda no válida, intente de nuevo.")

        except ValueError:
            print("\nError: Ingrese un número válido.")

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

#---------------------------------------------------------------------------------------------------------------------Reinas
class NodoReinas:
    def __init__(self, estado, nivelProfundidad, costoAcumulado, heuristica):
        self.estado = estado  # Estado actual del tablero
        self.nivelProfundidad = nivelProfundidad  # Nivel de profundidad
        self.costoAcumulado = costoAcumulado  # Costo acumulado (g(n))
        self.heuristica = heuristica  # Heurística (h(n))
        self.f = costoAcumulado + heuristica  # Función de evaluación (f(n) = g(n) + h(n))

def generarEstadoInicialReinas():
    """Genera un estado inicial con todas las reinas en la misma fila aleatoria."""
    filaInicial = random.randint(0, 3)
    return tuple((filaInicial, i) for i in range(4))

def calcularHeuristicaReinas(estado):
    """Calcula la heurística como el número de reinas mal colocadas."""
    contador = 0
    for i in range(4):
        fila1, col1 = estado[i]
        esValido = True
        for j in range(4):
            if i != j:
                fila2, col2 = estado[j]
                if fila1 == fila2 or abs(fila1 - fila2) == abs(col1 - col2):
                    esValido = False
                    break
        if not esValido:
            contador += 1
    return contador  # Queremos minimizar el número de reinas mal colocadas

def generarSucesoresReinas(nodoActual):
    """Genera sucesores válidos moviendo una reina a la vez."""
    sucesores = []
    estadoActual = nodoActual.estado
    for i in range(4):
        fila, columna = estadoActual[i]
        for nuevaFila in [fila - 1, fila + 1]:
            if 0 <= nuevaFila < 4:
                nuevoEstado = list(estadoActual)
                nuevoEstado[i] = (nuevaFila, columna)
                sucesores.append(tuple(nuevoEstado))
    return sucesores

def aEstrellaReinas():
    """Algoritmo A* para resolver el problema de las 4 reinas."""
    estadoInicial = generarEstadoInicialReinas()
    heuristicaInicial = calcularHeuristicaReinas(estadoInicial)
    nodoInicial = NodoReinas(estadoInicial, 0, 0, heuristicaInicial)
    agenda = [nodoInicial]  # Usamos una lista como agenda
    visitados = set()
    solucionesExploradas = []  # Para almacenar las soluciones exploradas

    while agenda:
        # Ordenar la agenda por f(n) (costo + heurística)
        agenda.sort(key=lambda x: x.f)
        nodoActual = agenda.pop(0)  # Seleccionar el nodo con menor f(n)
        solucionesExploradas.append((nodoActual.estado, nodoActual.f))  # Registrar solución explorada

        if nodoActual.heuristica == 0:  # Si todas las reinas están bien colocadas
            print("Soluciones exploradas con su costo asociado (f(n)):")
            for idx, (estado, costo) in enumerate(solucionesExploradas):
                print(f"Solución {idx + 1}:")
                imprimirTableroReinas(estado)
                print(f"Costo (f(n)): {costo}\n")
            print("Mejor solución encontrada:")
            return nodoActual.estado, nodoActual.f

        if nodoActual.estado in visitados:
            continue
        visitados.add(nodoActual.estado)

        for sucesor in generarSucesoresReinas(nodoActual):
            if sucesor not in visitados:
                nuevaProfundidad = nodoActual.nivelProfundidad + 1
                heuristicaSucesor = calcularHeuristicaReinas(sucesor)
                costoSucesor = nuevaProfundidad
                nodoSucesor = NodoReinas(sucesor, nuevaProfundidad, costoSucesor, heuristicaSucesor)
                agenda.append(nodoSucesor)

    return None, None

def imprimirTableroReinas(estado):
    """Imprime el tablero de manera visual."""
    tablero = [['.' for _ in range(4)] for _ in range(4)]
    for fila, col in estado:
        tablero[fila][col] = 'Q'
    for fila in tablero:
        print(' '.join(fila))
    print()
#--------------------------------------------------------------------------Sub menus
def menuReinas():
    """Menú para ejecutar el algoritmo A* en el problema de las 4 reinas."""
    solucion, costo = aEstrellaReinas()
    if solucion:
        print("Mejor solución encontrada:")
        imprimirTableroReinas(solucion)
        print(f"Costo asociado (f(n)): {costo}")
    else:
        print("No se encontró solución.")
    enter()

def menuPacman():
    while True:
        time.sleep(2)
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
        

def menu():
    while True:
        enter()
        print("\nSeleccione una opcion:")
        print("\n\t1. Busqueda ciega")
        print("\t2. Juego Pac-Man")
        print("\t3. Problema de las 4 reinas")
        print("\t0. Salir")
        opcion = int(input("\n\tIngrese el numero de la opcion: "))
        enter()
        if opcion == 1:
            menuCiega()
        elif opcion == 2:
            print("Buscando en heuristica...")
            menuPacman()
        elif opcion == 3:
            print("Resolviendo el problema de las 4 reinas...")
            menuReinas()
        elif opcion == 0:
            print("Saliendo del programa...")
            limpiar()
            break
        else:
            print("Opcion no valida, por favor intente de nuevo.")

menu()