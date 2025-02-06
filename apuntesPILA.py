class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.izquierda = None
        self.derecha = None

#diccionario con el arbol

relaciones = {
    1: [2, 7, 8],
    2: [3, 6],
    3: [4, 5],
    4: [],
    5: [],
    6: [],
    7: [],
    8: [9, 10],
    9: [11],
    10: [12],
    11: [],
    12: []
}

def construir_arbol(relaciones):
    nodos = {} #diccionario de objetos tipo Nodo
    for clave in relaciones:
        if clave not in nodos: #si la clave no esta en el diccionario, agrega un nuevo nodo al diccionario
            nodos[clave] = Nodo(clave)
        nodo_actual = nodos[clave]#independientemente de si se agrego un nuevo nodo o no, se obtiene el nodo actual
        if relaciones[clave]:#si la lista de relaciones no esta vacia
            nodo_actual.izquierda = nodos[relaciones[clave][0]] = Nodo(relaciones[clave][0])#se crea un nuevo nodo y se asigna a la izquierda del nodo actual
            if len(relaciones[clave]) > 1:#si la lista de relaciones tiene mas de un elemento
                nodo_actual.derecha = nodos[relaciones[clave][1]] = Nodo(relaciones[clave][1])#se crea un nuevo nodo y se asigna a la derecha del nodo actual
    return nodos[1]#regresamos el nodo raiz

raiz = construir_arbol(relaciones) #se llama a la funcion construir arbol para armar el arbol y recibir la raiz

def recorrido_profundidad_izquierda(raiz):
    if not raiz:#si la raiz es nula, no hay nada que hacer
        return

    pila = [raiz] #se crea una pila con la raiz
    while pila:#mientras la pila no este vacia
        nodo = pila.pop()#se saca el ultimo elemento de la pila
        print(nodo.valor, end=' ') #se imprime el valor del nodo
        if nodo.derecha:#si el nodo tiene un hijo derecho, se agrega a la pila
            pila.append(nodo.derecha) #se agrega a la pila
        if nodo.izquierda:#si el nodo tiene un hijo izquierdo, se agrega a la pila
            pila.append(nodo.izquierda) #se agrega a la pila

recorrido_profundidad_izquierda(raiz)#se llama a la funcion de recorrido en profundidad izquierda

