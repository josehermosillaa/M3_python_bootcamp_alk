
###### como nosotros hariamos una lista de los numeros pares que se encuentran en los primeros 50 numeros naturales

numeros = []
#recordar que podemos agregar los numero con numeros.append(EL NUMERO A AGREGAR)

for numero in range(1,51):
    #recorro todos los numeros entre 1 y 50
    if numero % 2 == 0: #resto es cero
        #aqui ya es par
        # print(numero)
        numeros.append(numero)

print(numeros)

#como hariamos esto con compresion de listas
#ESTO ES MAS COMPLEJO DE ESCRIBIR EN UN COMIENZO, PERO ES MAS OPTIMO PARA EL PROGRAMA.
pares = [ numero for numero in range(1,51) if numero %2 == 0]

lista_primeros_5_numeros = [numero for numero in range(1,6)] #-> [1,2,3,4,5]
print(pares)