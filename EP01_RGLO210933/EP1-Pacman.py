
~ 0 1 2 3 4 5 6 7
A X X . . . . . .
B X . . . . X Ϯ .
C X . . . . X . .
D . . . X X X . .
E . Ỽ . . . . . .
F . . . . . . . .
G X X X . . . . .
ideas de resolucion...
nodoInicial = [Ỽ(1,E),Ϯ(6,B)]
objetivo = Ỽ == Ϯ
ideas contruir 2 arboles diferentes con los movimientos posibles de cada uno eliminando los obstaculos de la ruta, ir haciendo un recorrido buscando que choquen, para determinar el choque Ỽ tiene que estar en la misma posicion que Ϯ,para mostra
al usuario el movimiento en el mapa se puede definir una matris con los obstaculos estaticos 'X' y que va mostrando la posicion de los personajes Ỽ Ϯ con cada movimiento, un movimiento seria cada que se cambia a un nodo hijo por parte del Ϯ y del Ỽ
siendo esta una simulacion de pacman, para los recorridos toca utilizar el algoritmo hill climbing para