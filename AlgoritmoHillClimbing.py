#algoritmo hill climbing
class nodo:
    def __init__(self, valor,np):
        self.np=np 
        self.valor = valor
        self.hijos=[]
        
    def agregarHijo(self, hijo):
        self.hijos.append(hijo)
valor = input("Ingrese el valor del primer nodo: ")
hn = input("Ingresa ek valor de la heuristica: ")
np = input("Ingresa el nivel de profundidad: ")
raiz = nodo(valor,hn, np)
agenda=[]
nodoMeta = "H"
agenda.append(raiz)
while (agenda):
    elemento = agenda.pop()
    print("Nodo visitado: ", elemento.valor)
    if elemento.valor == nodoMeta:
        print("Encontrado")
        break
    else:
        nodosVecinos = input("cuantos nodos vecinos tiene el nodo: ",elemento.valor)
        for i in range(nodosVecinos):
            valor = input("Ingrese el valor del nodo vecino: ")
            hn = input("Ingrese el valor de la heuristica: ")
            np = input("Ingrese el nivel de profundidad: ")
            agenda.append(nodo(valor,hn,np))
        #ordenar a los sucesores
        agenda.sort(key=lambda obj: obj.hn)
        for i in range(1,len(agenda)):
            agenda.pop(i)