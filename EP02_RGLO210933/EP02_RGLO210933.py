import random


POBLACION_TAM = 10
RANGO_MIN = -5
RANGO_MAX = 5
PROB_MUTA = 0.025
GENERACIONES_MAX = 300


def calcular_errores(x, y, z, u):
    ecuacion1 = abs(2 * x + 3 * y - z + 4 * u - 2)
    ecuacion2 = abs(-x + y + 2 * z - 2 * u - 2)
    ecuacion3 = abs(3 * x - y + z + 2 * u - 11)
    ecuacion4 = abs(4 * x + 2 * y - 3 * z - u + 4)
    return ecuacion1 + ecuacion2 + ecuacion3 + ecuacion4


def generar_poblacion():
    return [
        [random.randint(RANGO_MIN, RANGO_MAX) for _ in range(4)] for _ in range(POBLACION_TAM)
    ]


def evaluar_poblacion(poblacion):
    return [calcular_errores(*individuo) for individuo in poblacion]

# Seleccion por ruleta y basada en rangos
def seleccionar(poblacion, fitness):
    # Seleccion por ruleta para los primeros 5
    total_fitness = sum(fitness)
    probabilidades = [1 / (f + 1) for f in fitness]
    seleccionados = random.choices(poblacion, weights=probabilidades, k=5)

    # Seleccion porrangos para el resto
    rangos = sorted(zip(poblacion, fitness), key=lambda x: x[1])
    for i in range(5):
        if random.random() < 0.5:
            seleccionados.append(rangos[i][0])

    return seleccionados


def cruza(poblacion):
    nueva_generacion = []
    for _ in range(5): 
        padre1, padre2 = random.sample(poblacion, 2)
        punto_cruce = random.randint(1, 3)
        hijo1 = padre1[:punto_cruce] + padre2[punto_cruce:]
        hijo2 = padre2[:punto_cruce] + padre1[punto_cruce:]
        nueva_generacion.extend([hijo1, hijo2])
    return nueva_generacion


def muta(poblacion):
    for individuo in poblacion:
        if random.random() < PROB_MUTA:
            gen_a_mutar = random.randint(0, 3)
            individuo[gen_a_mutar] = random.randint(RANGO_MIN, RANGO_MAX)
    return poblacion


def algoritmo_genetico():
    poblacion = generar_poblacion()
    for generacion in range(GENERACIONES_MAX):
        print(poblacion)
        fitness = evaluar_poblacion(poblacion)
        mejor_fitness = min(fitness)
        print(f"Generación {generacion + 1} - Mejor Fitness: {mejor_fitness}")

        if mejor_fitness == 0:
            print("Solución encontrada:", poblacion[fitness.index(mejor_fitness)])
            return

        poblacion = seleccionar(poblacion, fitness)
        poblacion = cruza(poblacion)
        poblacion = muta(poblacion)

    print("No se encontró una solución exacta en el límite de generaciones.")

algoritmo_genetico()
