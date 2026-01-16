#########    0        1         2
#las listas se ordenan de izquierda a derecha empezando por el indice 0    
"""
matriz[1] = [ 4, 5, 6]
             0   1  2

matriz[1][2] = 6   
por que matriz[1] es una lista
lista1 = matriz[1]
lista1[2] = 6


como obtengo el numero 3
matriz[0][2]
el valor 9?
matriz[2][2]

"""
matriz = [[1,2,3], [4,5,6], [7,8,9]]
for fila in matriz:

    for elemento in fila:
        print(elemento, end=' ')
        
    print() #crea un salto de linea

