import os
import platform
print("bienvenido usuario de ",platform.system())
#---------------------------------------------------------funciones de formato
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

        

def menu():
    while True:
        enter()
        print("\nSeleccione una opcion:")
        print("\n\t1. Busqueda ciega")
        print("\t2. juego pacman")
        print("\t0. Salir")

        opcion = int(input("\n\tIngrese el numero de la opcion: "))
        enter()
        if opcion == 1:
            menuCiega()
        elif opcion == 2:
            print("Buscando en heuristica...")
            #3.- Desarrollar un programa en Python que permita aplicar los algoritmos de búsqueda heurística a
            #un juego similar al Pac-Man, tomando en cuenta las siguientes restricciones para el problema:
            #* El laberinto es fijo, es decir, el tamaño y los obstáculos serán definidos por ustedes y no
            #cambiarán.
            #* La posición inicial tanto del fantasma como del pac-man debe ser aleatoria, evitando colocarlos
            #en casillas que se consideran obstáculos.
            #* El único que puede moverse es el pac-man (estado inicial) para poder acercarse al fantasma
            #(estado objetivo), este último se queda en su posición siempre.

            
            #menuHeuristica()
        elif opcion == 0:
            print("Saliendo del programa...")
            limpiar()
            break
        else:
            print("Opcion no valida, por favor intente de nuevo.")
menu()