#algoritmo hill climbing
class nodo:
    def __init__(self, valor,np):
        self.np=np 
        self.valor = valor
        self.hijos=[]
        
    def agregarHijo(self, hijo):
        self.hijos.append(hijo)
def calcularDistancia (nodoInicio,nodoMeta):
    for i in range(len(nodoInicio)):
        for j in range(len(nodoInicio[i])):
            valor = nodoInicio[i][j]
            x,y=buscar(valor, nodoMeta)
            dist = dist+(abs(i-x)+abs(j-y))
    return dist
def buscar(valor, nodoMeta):
    for i in range(len(nodoMeta)):
        for j in range(len(nodoMeta[i])):
            if valor == nodoMeta[i][j]:
                return i,j
fn = calcularDistancia([[2,8,3],[1,0,4],[7,6,5]], [[1,2,3],[8,0,4],[7,6,5]])
raiz  =  nodo([[2,8,3],[1,0,4],[7,6,5]],0)