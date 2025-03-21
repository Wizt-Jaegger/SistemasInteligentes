
import numpy as np

def funcion_activacion(suma):
    return 1 if suma > 0 else 0

def entrenar_perceptron(patrones, tasa_aprendizaje, epocas):
    num_caracteristicas = len(patrones[0]) - 1
    pesos = np.random.rand(num_caracteristicas)
    umbral = np.random.rand(1)[0]

    for _ in range(epocas):
        for patron in patrones:
            entrada = np.array(patron[:-1])
            salida_esperada = patron[-1]
            suma = np.dot(entrada, pesos) - umbral
            salida = funcion_activacion(suma)
            error = salida_esperada - salida
            pesos += tasa_aprendizaje * error * entrada
            umbral -= tasa_aprendizaje * error

    with open('pesos_umbral.txt', 'w') as f:
        for peso in pesos:
            f.write(f'{peso}\n')
        f.write(f'{umbral}\n')

    return pesos, umbral

if __name__ == '__main__':
    patrones = [
        [5, 2, 20, 25, 30, 1],
        [2, 0, 10, 50, 25, 0],
        [8, 2, 50, 20, 40, 1],
        [3, 1, 15, 40, 28, 0],
        [7, 2, 30, 30, 35, 1],
        [4, 0, 12, 55, 23, 0],
        [9, 2, 60, 15, 45, 1],
        [6, 1, 25, 35, 32, 1],
        [3, 0, 18, 60, 27, 0],
        [10, 2, 70, 10, 50, 1],
        [1, 0, 5, 70, 22, 0],
        [8, 1, 40, 25, 38, 1],
        [2, 0, 8, 65, 24, 0],
        [7, 1, 35, 30, 34, 1],
        [6, 2, 45, 20, 37, 1],
        [4, 0, 20, 50, 29, 0],
        [9, 1, 55, 18, 42, 1],
        [5, 1, 22, 33, 31, 1],
        [3, 0, 12, 58, 26, 0],
        [8, 2, 48, 22, 39, 1],
        [7, 1, 38, 28, 36, 1],
        [4, 0, 16, 52, 27, 0],
        [9, 2, 65, 12, 44, 1],
        [2, 0, 10, 62, 23, 0]
    ]

    tasa_aprendizaje = 0.1
    epocas = 100

    pesos, umbral = entrenar_perceptron(patrones, tasa_aprendizaje, epocas)
    print('Entrenamiento finalizado.')
    print(f'Pesos: {pesos}')
    print(f'Umbral: {umbral}')
