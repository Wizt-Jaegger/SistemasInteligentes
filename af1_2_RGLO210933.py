# Diseniar un programa que pida los datos de una persona y los imprima
#Codigo de porque emi se sobre complico con algo tan sencillo pa que se viera bonito?
import os
import platform
print("bienvenido usuario de ",platform.system())
def capturaPerros():
    a = int(input("\n\tIngresa el núumero de perros favoritos: "))

    Perros = []
    
    for i in range(a):
        b = input(f"Dame el nombre de tu perro No. {i + 1}: ")
        Perros.append(b) 
    
    print("\nLos nombres de tus perros favoritos son:")
    for perro in Perros:
        print(perro)
def capturaDatosPersonales():
    nombre = input("\nHola, este es un programa de practica Python\n\n\tDame tu nombre: ")
    edad = input("\tDame tu edad: ")
    estatura = input("\tDame tu estatura: ")

    print("\n\tTu nombre es:", nombre)
    print("\tTu edad es:", edad)
    print("\tTu estatura es:", estatura)

def OperacionesMate():
    num1 = float(input("Ingresa el primer numero: "))
    num2 = float(input("Ingresa el segundo numero: "))
    operacion = str(input("Ingresa la operacion (+, -, *, /): "))

    if operacion == "+":
        resultado = num1 + num2
    elif operacion == "-":
        resultado = num1 - num2
    elif operacion == "*":
        resultado = num1 * num2
    elif operacion == "/":
        if num2 != 0:
            resultado = num1 / num2
        else:
            return "Error: No se puede dividir entre cero."
    else:
        return "Operacion invalida"
    
    return f"\nEl resultado de la operacion es:\n\t{num1} {operacion} {num2} = {resultado}"

def ListaNumerica():
    cantidad = int(input("¿Cuantos numeros quieres ingresar? "))
    print("\n")
    lista_numeros = []
    for i in range(cantidad):
        numero = float(input(f"\tIngrese el numero {i + 1}: "))
        lista_numeros.append(numero)

    promedio = sum(lista_numeros) / len(lista_numeros) if lista_numeros else 0
    return f"\nEl promedio de los numeros es: {promedio}"

def limpiar():
    varClear = "Clear"
    if platform.system() == "Windows":
        varClear = "cls"
    else:
        varClear = "clear"
    os.system(varClear)

def enter():
    input("\npresiona ENTER para continuar\n")
    limpiar()
    
def menu():
    while True:
        enter()
        print("\nSeleccione una opcion:")
        print("\n\t1. Captura Perros")
        print("\t2. Captura Datos Personales")
        print("\t3. Operaciones Matematicas")
        print("\t4. Calcular promedio de una lista")
        print("\t5. Salir")

        opcion = int(input("\n\tIngrese el numero de la opcion: "))
        enter()
        if opcion == 1:
            capturaPerros()
        elif opcion == 2:
            capturaDatosPersonales()
        elif opcion == 3:
            print(OperacionesMate())
        elif opcion == 4:
            print(ListaNumerica())
        elif opcion == 5:
            print("Saliendo del programa...")
            break
        else:
            print("Opcion no valida, por favor intente de nuevo.")
        
menu()



