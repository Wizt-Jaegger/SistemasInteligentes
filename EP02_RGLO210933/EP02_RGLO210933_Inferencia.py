
import numpy as np 

def funcion_activacion(suma):
    return 1 if suma > 0 else 0

def cargar_pesos_umbral(archivo='pesos_umbral.txt'):
    with open(archivo, 'r') as f:
        valores = [float(linea.strip()) for linea in f.readlines()]
    return np.array(valores[:-1]), valores[-1]

def inferir(entrada, pesos, umbral):
    suma = np.dot(np.array(entrada), pesos) - umbral
    return funcion_activacion(suma)

if __name__ == '__main__':
    pesos, umbral = cargar_pesos_umbral()

    print('Modelo de inferencia para aprobación de crédito')
    ingreso = float(input('Ingresos mensuales en miles de pesos: '))
    historial = int(input('Historial crediticio (0 = Malo, 1 = Regular, 2 = Bueno): '))
    credito_solicitado = float(input('Monto del crédito solicitado en miles de dólares: '))
    deuda_ingreso = float(input('Relación deuda-ingresos (%): '))
    edad = int(input('Edad del solicitante: '))

    entrada = [ingreso, historial, credito_solicitado, deuda_ingreso, edad]
    resultado = inferir(entrada, pesos, umbral)

    if resultado == 1:
        print('Crédito aprobado.')
    else:
        print('Crédito rechazado.')
