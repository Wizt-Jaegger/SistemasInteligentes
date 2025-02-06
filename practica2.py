import os
import platform
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

def practicandoESD():
    Lista=[1,2,3]
    tupla=(4,5,6)
    Lista.append(5)
    #print(Lista)
    Lista2=["nombre",3.4,5,'a']
    Lista=[["lista 1",20,30,[3,4,5,[6,7,8, Lista2]]]]
    #print(Lista)
    #print(Lista[0][3][3][3])
    for i in range(len(Lista)):
        print(Lista[i])
def funcion(var):
    var = 20
    print("variable", var)
def practicado2ESD():
    var = 30
    funcion(var)
    print(var)
class Perro: 

    def __init__(self, nombre, raza):
        self.nombre = nombre
        self.raza = raza

    def printPerro(self):
        print("\n\tTu perro ",self.nombre, " es de la raza:")
        print("\t",self.raza)

def practicado3ESD():  

    nombrePerro = input("Dame el nombre de tu perro: ")
    razaPerro = input("Dime la raza de tu perro: ")
    mi_perro = Perro(nombrePerro, razaPerro)
    Perro.printPerro(mi_perro)

def practicado4ESD():
    print()
    
def menu():
    while True:
        enter()
        print("\nSeleccione una opcion:")
        print("\n\t1. Practica1")
        print("\t2. Practica2")
        print("\t3. ClasePerro")
        print("\t0. Salir")

        opcion = int(input("\n\tIngrese el numero de la opcion: "))
        enter()
        if opcion == 1:
            practicandoESD()
        elif opcion == 2:
            practicado2ESD()
        elif opcion == 3:
            practicado3ESD()
        elif opcion == 0:
            print("Saliendo del programa...")
            break
        else:
            print("Opcion no valida, por favor intente de nuevo.")

menu()