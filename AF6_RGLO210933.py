import os
import platform
print("bienvenido usuario de ",platform.system())
#---------------------------------------------------------funciones de formato COOL
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

#busqueda en profundidad derecha
def busquedaProfundidadDerecha(raiz):
    print("Busqueda en profundidad derecha")
    agenda = []
    agenda.append(raiz)
    nodoMeta = (1, 2, 3, 8, 0, 4, 7, 6, 5)
    
    while len(agenda) > 0:
        nodoVisitado = agenda.pop()
        
        
        valor = nodoVisitado.valor
        print("Nodo visitado:")
        #Darle forma de matriz asi bonita
        for i in range(0, len(valor), 3): 
            print(" ", valor[i:i + 3])
        
        if nodoVisitado.valor == nodoMeta:
            break
        else:
            for hijo in (nodoVisitado.hijos):
                agenda.append(hijo)

#busqueda en profundidad izquierda
def busquedaProfundidadIzquierda(raiz):
    print("Busqueda en profundidad izquierda")
    agenda = []
    agenda.append(raiz)
    nodoMeta = (1, 2, 3, 8, 0, 4, 7, 6, 5)
    
    while len(agenda) > 0:
        nodoVisitado = agenda.pop()
        valor = nodoVisitado.valor
        print("Nodo visitado:")
        #Darle forma de matriz asi bonita
        for i in range(0, len(valor), 3): 
            print(" ", valor[i:i + 3])
        
        if nodoVisitado.valor == nodoMeta:
            break
        else:
            for hijo in reversed(nodoVisitado.hijos):
                agenda.append(hijo)

#busqueda en profundidad limitada izquierda
def busquedaProfundidadLimitadaIzquierda(raiz, lim):
    
    agenda = []
    agenda.append(raiz)
    nodoMeta = (1, 2, 3, 8, 0, 4, 7, 6, 5)
    
    var = False
    while (len(agenda) > 0):
        nodoVisitado = agenda.pop()
        valor = nodoVisitado.valor
        print("\tNodo visitado: ")
        for i in range(0, len(valor), 3): 
            print(" ", valor[i:i + 3])
        print("nivel de profundidad: ",nodoVisitado.np)
        
        if nodoVisitado.valor == nodoMeta:
            var = True
            break
        else :
            for hijo in reversed(nodoVisitado.hijos):
                
                if hijo.np <= lim:
                    agenda.append(hijo)
    return var
#busqueda en profundidad limitada derecha
def busquedaProfundidadLimitadaDerecha(raiz, lim):
    
    agenda = []
    agenda.append(raiz)
    nodoMeta = (1, 2, 3, 8, 0, 4, 7, 6, 5)
    
    var = False
    while (len(agenda) > 0):
        nodoVisitado = agenda.pop()
        valor = nodoVisitado.valor
        print("\tNodo visitado: ")
        for i in range(0, len(valor), 3): 
            print(" ", valor[i:i + 3])
        print("nivel de profundidad: ",nodoVisitado.np)
        
        if nodoVisitado.valor == nodoMeta:
            var = True
            break
        else :
            for hijo in (nodoVisitado.hijos):
                
                if hijo.np <= lim:
                    agenda.append(hijo)
    return var
def busquedaProfundidadIterada(raiz,opt):
    print("\nBusqueda en profundidad iterada izquierda\n")
    agenda = []
    agenda.append(raiz)
    nodoMeta = (1, 2, 3, 8, 0, 4, 7, 6, 5)
    lim = 0
    flag = False
    while not (flag) :
        if opt == 1:
            flag = busquedaProfundidadLimitadaIzquierda(raiz, lim)
        else:
            flag = busquedaProfundidadLimitadaDerecha(raiz, lim)
        lim = lim + 1
def busquedaAnchuraIzquierda(raiz):
    print("Busqueda en anchura izquierda")
    #es con cola
    agenda = []
    agenda.append(raiz)
    nodoMeta = (1, 2, 3, 8, 0, 4, 7, 6, 5)
    while (len(agenda) > 0):
        nodoVisitado = agenda.pop(0)
        valor = nodoVisitado.valor    
        print("Nodo visitado: ")
        #Darle forma de matriz asi bonita
        for i in range(0, len(valor), 3): 
            print(" ", valor[i:i + 3])
        
        if nodoVisitado.valor == nodoMeta:
            
            break
        else :
            for hijo in nodoVisitado.hijos:
                agenda.append(hijo)

#busqueda en anchura derecha
def busquedaAnchuraDerecha(raiz):
    print("\nBusqueda en anchura derecha\n")
    #es con cola
    agenda = []
    agenda.append(raiz)
    nodoMeta = (1, 2, 3, 8, 0, 4, 7, 6, 5)
    while (len(agenda) > 0):
        nodoVisitado = agenda.pop(0)    
        valor = nodoVisitado.valor    
        print("Nodo visitado: ")
        #Darle forma de matriz asi bonita
        for i in range(0, len(valor), 3): 
            print(" ", valor[i:i + 3])
        if nodoVisitado.valor == nodoMeta:
            
            break
        else :
            for hijo in reversed(nodoVisitado.hijos):
                agenda.append(hijo)


#Representacion del espacio de estados (Construir el arbol) 

# Crear nodos en forma de matriz para el juego de numeros
# Estado meta (1,2,3,8,0,4,7,6,5)
raiz  =  nodo((2,8,3,1,0,4,7,6,5),0)#posicion inicial

nodo2  = nodo((2,0,3,1,8,4,7,6,5),1)#nivel 1 = 1 intercambio
nodo3  = nodo((2,8,3,0,1,4,7,6,5),1)
nodo4  = nodo((2,8,3,1,6,4,7,0,5),1)
nodo5  = nodo((2,8,3,1,4,0,7,6,5),1)

#------------------------------------------nivel 2 = 2 intercambios

nodo6  = nodo((0,2,3,1,8,4,7,6,5),2)#hijo Nodo2 
nodo7  = nodo((2,3,0,1,8,4,7,6,5),2)#hijo Nodo2

nodo8  = nodo((0,8,3,2,1,4,7,6,5),2)#Hijo Nodo3
nodo9 = nodo((2,8,3,7,1,4,0,6,5),2)#Hijo Nodo3


nodo10 = nodo((2,8,3,1,6,4,0,7,),2)#Hijo Nodo4
nodo11 = nodo((2,8,3,1,6,4,7,5,0),2)#Hijo Nodo4

nodo12 = nodo((2,8,0,1,4,3,7,6,5),2)#Hijo Nodo5
nodo13 = nodo((2,8,3,1,4,5,7,6,0),2)#Hijo Nodo5

#------------------------------------------nivel 3 = 3 intercambios

nodo14 = nodo((1,2,3,0,8,4,7,6,5),3)#Hijo Nodo6
nodo15 = nodo((2,3,4,1,8,0,7,6,5),3)#Hijo Nodo7

nodo16 = nodo((8,0,3,2,1,4,7,6,5),3)#Hijo Nodo8
nodo17 = nodo((2,8,3,7,1,4,6,0,5),3)#Hijo Nodo9

nodo18 = nodo((2,8,3,0,6,4,1,7,5),3)#Hijo Nodo10
nodo19 = nodo((2,8,3,1,6,0,7,5,4),3)#Hijo Nodo11

nodo20 = nodo((2,0,8,1,4,3,7,6,5),3)#Hijo Nodo12
nodo21 = nodo((2,8,3,1,4,5,7,0,6),3)#Hijo Nodo13

#------------------------------------------nivel 4 = 4 intercambios

nodo22 = nodo((1,2,3,8,0,4,7,6,5),4)#Hijo Nodo14
nodo23 = nodo((1,2,3,7,8,4,0,6,5),4)#Hijo Nodo14

nodo24 = nodo((2,3,4,1,0,8,7,6,5),4)#Hijo Nodo15
nodo25 = nodo((2,3,4,1,8,5,7,6,0),4)#Hijo Nodo15

nodo26 = nodo((8,3,0,2,1,4,7,6,5),4)#Hijo Nodo16
nodo27 = nodo((8,1,3,2,0,4,7,6,5),4)#Hijo Nodo16

nodo28 = nodo((2,8,3,7,0,4,6,1,5),4)#Hijo Nodo17
nodo29 = nodo((2,8,3,7,1,4,6,5,0),4)#Hijo Nodo17

nodo30 = nodo((0,8,3,2,6,4,1,7,5),4)#Hijo Nodo18
nodo31 = nodo((2,8,3,6,0,4,1,7,5),4)#Hijo Nodo18

nodo32 = nodo((2,8,3,1,0,6,7,5,4),4)#Hijo Nodo19
nodo33 = nodo((2,8,0,1,6,3,7,5,4),4)#Hijo Nodo19

nodo34 = nodo((0,2,8,1,4,3,7,6,5),4)#Hijo Nodo20
nodo35 = nodo((2,4,8,1,0,3,7,6,5),4)#Hijo Nodo20

nodo36 = nodo((2,8,3,1,0,5,7,4,6),4)#Hijo Nodo21
nodo37 = nodo((2,8,3,1,4,5,0,7,6),4)#Hijo Nodo21

#------------------------------------------nivel 5 = 5 intercambios

# Asignar hijos
raiz.agregarHijo(nodo2)
raiz.agregarHijo(nodo3)
raiz.agregarHijo(nodo4)
raiz.agregarHijo(nodo5)

nodo2.agregarHijo(nodo6)
nodo2.agregarHijo(nodo7)

nodo3.agregarHijo(nodo8)
nodo3.agregarHijo(nodo9)

nodo4.agregarHijo(nodo10)
nodo4.agregarHijo(nodo11)

nodo5.agregarHijo(nodo12)
nodo5.agregarHijo(nodo13)

nodo6.agregarHijo(nodo14)
nodo7.agregarHijo(nodo15)
nodo8.agregarHijo(nodo16)
nodo9.agregarHijo(nodo17)
nodo10.agregarHijo(nodo18)
nodo11.agregarHijo(nodo19)
nodo12.agregarHijo(nodo20)
nodo13.agregarHijo(nodo21)

nodo14.agregarHijo(nodo22)
nodo14.agregarHijo(nodo23)

nodo15.agregarHijo(nodo24)
nodo15.agregarHijo(nodo25)

nodo16.agregarHijo(nodo26)
nodo16.agregarHijo(nodo27)

nodo17.agregarHijo(nodo28)
nodo17.agregarHijo(nodo29)

nodo18.agregarHijo(nodo30)
nodo18.agregarHijo(nodo31)

nodo19.agregarHijo(nodo32)
nodo19.agregarHijo(nodo33)

nodo20.agregarHijo(nodo34)
nodo20.agregarHijo(nodo35)

nodo21.agregarHijo(nodo36)#Esto es ser necio pues, que largo esta esta cosa,aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
nodo21.agregarHijo(nodo37)


def menuCiega():
            opt_ciega = 1
            while opt_ciega != 0:
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
                        limpiar()
                        break

                    enter() 
                    print("\nIzquierda o derecha:")
                    print("\n\t1. Izquierda")
                    print("\n\t2. Derecha")

                    orientacion = int(input("\n\tIngrese 1 o 2: "))

                    if opt_ciega == 1:
                        enter()
                        if orientacion == 1:
                            busquedaProfundidadIzquierda(raiz)
                        elif orientacion == 2:
                            busquedaProfundidadDerecha(raiz)
                        else:
                            print("\nOpción de orientación no válida.")

                    elif opt_ciega == 2:
                        if orientacion == 1:
                            busquedaAnchuraIzquierda(raiz)
                        elif orientacion == 2:
                            busquedaAnchuraDerecha(raiz)
                        else:
                            print("\nOpción de orientación no válida.")

                    elif opt_ciega == 3:
                        limite = int(input("\nIngrese el limite de profundidad: "))
                        enter()
                        if orientacion == 1:
                            print("\nBusqueda en profundidad limitada izquierda\n")
                            busquedaProfundidadLimitadaIzquierda(raiz, limite)
                        elif orientacion == 2:
                            print("\nBusqueda en profundidad limitada derecha\n")
                            busquedaProfundidadDerecha(raiz,limite)
                        else:
                            print("\nOpción de orientación no válida.")

                    elif opt_ciega == 4:
                        enter()
                        if orientacion == 1:
                            busquedaProfundidadIterada(raiz,1)
                        elif orientacion == 2:
                            busquedaProfundidadIterada(raiz,2)
                        else:
                            print("\nOpción de orientación no válida.")

                    else:
                        print("\nOpción de búsqueda no válida, intente de nuevo.")

                except ValueError:
                    print("\nError: Ingrese un número válido.")


menuCiega()

        