#busqueda en profundidad izquierda
class nodo:
    def __init__(self, valor,np):
        self.np=np 
        self.valor = valor
        self.hijos=[]

    def agregarHijo(self, hijo):
        self.hijos.append(hijo)

#Representacion del espacio de estados (Construir el arbol)

# Crear nodos
raiz = nodo(1,0)
nodo2 = nodo(2,1)
nodo3 = nodo(3,1)
nodo4 = nodo(4,1)
nodo5 = nodo(5,1)
nodo6 = nodo(6,1)
nodo7 = nodo(7,1)
nodo8 = nodo(8,1)
nodo9 = nodo(9,1)
nodo10 = nodo(10,1)
nodo11 = nodo(11,1)
nodo12 = nodo(12,1)
nodo13 = nodo(13,1)
nodo14 = nodo(14,1)
nodo15 = nodo(15,1)
nodo16 = nodo(16,1)
nodo17 = nodo(17,1)
nodo18 = nodo(18,1)

# Asignar hijos
raiz.agregarHijo(nodo2)
raiz.agregarHijo(nodo7)
raiz.agregarHijo(nodo14)

nodo2.agregarHijo(nodo3)
nodo2.agregarHijo(nodo6)

nodo3.agregarHijo(nodo4)
nodo3.agregarHijo(nodo5)

nodo7.agregarHijo(nodo8)
nodo7.agregarHijo(nodo13)

nodo8.agregarHijo(nodo9)
nodo8.agregarHijo(nodo10)

nodo9.agregarHijo(nodo11)

nodo10.agregarHijo(nodo12)

nodo14.agregarHijo(nodo15)
nodo14.agregarHijo(nodo17)
nodo14.agregarHijo(nodo18)

nodo15.agregarHijo(nodo16)

#raiz.hijos.append(nodo(2))
#raiz.hijos.append(nodo(3))
#raiz.hijos.append(nodo(4))
#raiz.hijos(0).hijos.append(nodo(5))
#raiz.hijos(0).hijos.append(nodo(6))

def calcularNivelesProfundidad(raiz):
    if raiz is None:
        return 0
    else:
        
        for hijo in raiz.hijos:
            hijo.np = raiz.np + 1 
            calcularNivelesProfundidad(hijo)
        return 1 + max(calcularNivelesProfundidad(hijo) for hijo in raiz.hijos) if raiz.hijos else 0

#busqueda en profundidad izquierda
def busquedaProfundidadIzquierda(raiz):
    print("Busqueda en profundidad izquierda")
    agenda = []
    agenda.append(raiz)
    nodoMeta = 6
    while (len(agenda) > 0):
        nodoVisitado = agenda.pop()
        print("Nodo visitado: ", nodoVisitado.valor)
        if nodoVisitado.valor == nodoMeta:
            
            break
        else :
            for hijo in reversed(nodoVisitado.hijos):
                agenda.append(hijo)


busquedaProfundidadIzquierda(raiz)
#busqueda en profundidad derecha
def busquedaProfundidadDerecha(raiz):
    print("Busqueda en profundidad derecha")
    agenda = []
    agenda.append(raiz)
    nodoMeta = 6
    while (len(agenda) > 0):
        nodoVisitado = agenda.pop()
        print("Nodo visitado: ", nodoVisitado.valor)
        if nodoVisitado.valor == nodoMeta:
            
            break
        else :
            for hijo in nodoVisitado.hijos:
                agenda.append(hijo)


busquedaProfundidadDerecha(raiz)
#busqueda en anchura izquierda
def busquedaAnchuraIzquierda(raiz):
    print("Busqueda en anchura izquierda")
    #es con cola
    agenda = []
    agenda.append(raiz)
    nodoMeta = 6
    while (len(agenda) > 0):
        nodoVisitado = agenda.pop(0)    
        print("Nodo visitado: ", nodoVisitado.valor)
        if nodoVisitado.valor == nodoMeta:
            
            break
        else :
            for hijo in nodoVisitado.hijos:
                agenda.append(hijo)

busquedaAnchuraIzquierda(raiz)
#busqueda en anchura derecha
def busquedaAnchuraDerecha(raiz):
    print("\nBusqueda en anchura derecha\n")
    #es con cola
    agenda = []
    agenda.append(raiz)
    nodoMeta = 6
    while (len(agenda) > 0):
        nodoVisitado = agenda.pop(0)    
        print("\tNodo visitado: ", nodoVisitado.valor)
        if nodoVisitado.valor == nodoMeta:
            
            break
        else :
            for hijo in reversed(nodoVisitado.hijos):
                agenda.append(hijo)
busquedaAnchuraDerecha(raiz)

#busqueda en profundidad limitada izquierda
def busquedaProfundidadLimitadaIzquierda(raiz, lim):
    
    agenda = []
    agenda.append(raiz)
    nodoMeta = 10
    
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

print("\nBusqueda en profundidad limitada izquierda\n")
busquedaProfundidadLimitadaIzquierda(raiz, 3)

def busquedaProfundidadIteradaIzquierda(raiz):
    print("\nBusqueda en profundidad iterada izquierda\n")
    agenda = []
    agenda.append(raiz)
    nodoMeta = 10
    lim = 0
    flag = False
    while not (flag) :
        
        flag = busquedaProfundidadLimitadaIzquierda(raiz, lim)
        lim = lim + 1


busquedaProfundidadIteradaIzquierda(raiz)
