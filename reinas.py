import random

class Nodo:
    def __init__(self, estado, nivelProfundidad, costoAcumulado, heuristica):
        self.estado = estado  # Estado actual del tablero
        self.nivelProfundidad = nivelProfundidad  # Nivel de profundidad
        self.costoAcumulado = costoAcumulado  # Costo acumulado (g(n))
        self.heuristica = heuristica  # Heurística (h(n))
        self.f = costoAcumulado + heuristica  # Función de evaluación (f(n) = g(n) + h(n))

def generarEstadoInicial():
    """Genera un estado inicial con todas las reinas en la misma fila aleatoria."""
    filaInicial = random.randint(0, 3)
    return tuple((filaInicial, i) for i in range(4))

def calcularHeuristica(estado):
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

def generarSucesores(nodoActual):
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

def aEstrella():
    """Algoritmo A* para resolver el problema de las 4 reinas."""
    estadoInicial = generarEstadoInicial()
    heuristicaInicial = calcularHeuristica(estadoInicial)
    nodoInicial = Nodo(estadoInicial, 0, 0, heuristicaInicial)
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
                imprimirTablero(estado)
                print(f"Costo (f(n)): {costo}\n")
            print("Mejor solución encontrada:")
            return nodoActual.estado, nodoActual.f

        if nodoActual.estado in visitados:
            continue
        visitados.add(nodoActual.estado)

        for sucesor in generarSucesores(nodoActual):
            if sucesor not in visitados:
                nuevaProfundidad = nodoActual.nivelProfundidad + 1
                heuristicaSucesor = calcularHeuristica(sucesor)
                costoSucesor = nuevaProfundidad
                nodoSucesor = Nodo(sucesor, nuevaProfundidad, costoSucesor, heuristicaSucesor)
                agenda.append(nodoSucesor)

    return None, None

def imprimirTablero(estado):
    """Imprime el tablero de manera visual."""
    tablero = [['.' for _ in range(4)] for _ in range(4)]
    
    for fila, col in estado:
        tablero[fila][col] = 'Q'
    for fila in tablero:
        print(' '.join(fila))
    print()

# Ejecutar el algoritmo A*
solucion, costo = aEstrella()
if solucion:
    print("Mejor solución encontrada:")
    imprimirTablero(solucion)
    print(f"Costo asociado (f(n)): {costo}")
else:
    print("No se encontró solución.")