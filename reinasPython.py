class nodo:
    def __init__(self, valor,np):
        self.np=np 
        self.valor = valor
        self.hijos=[]

    def agregarHijo(self, hijo):
        self.hijos.append(hijo)