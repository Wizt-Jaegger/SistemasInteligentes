def seleccionBasadaRangos():
    print("seleccion basada en rangos")
    #usamos bubble sort para ordenar 
    
def bubble_sort(poblacion, fitness):
    # Crear un diccionario con la relación genética - fitness
    individuos = [{"genetico": poblacion[i], "fitness": fitness[i]} for i in range(len(poblacion))]
    
    # Implementación del Bubble Sort en base al fitness
    n = len(individuos)
    for i in range(n):
        for j in range(0, n - i - 1):
            if individuos[j]["fitness"] > individuos[j + 1]["fitness"]:  # Orden ascendente
                individuos[j], individuos[j + 1] = individuos[j + 1], individuos[j]

    # Vaciar listas originales y llenarlas con los valores ordenados
    poblacion.clear()
    fitness.clear()
    
    for individuo in individuos:
        poblacion.append(individuo["genetico"])
        fitness.append(individuo["fitness"])

# datos hardcodeados
poblacion = ["01010", "00101", "01111", "00111"]
fitness = [10, 5, 15, 7]

print("Antes de ordenar:")
print("Población:", poblacion)
print("Fitness:", fitness)

bubble_sort(poblacion, fitness)

print("\nDespués de ordenar:")
print("Población:", poblacion)
print("Fitness:", fitness)
