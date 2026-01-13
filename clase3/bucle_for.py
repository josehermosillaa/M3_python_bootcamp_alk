#ejemplos bucle for

#lista

numeros = [ 1, 2, 3, 4, 7, 8, 12] #conjunto de 7 elementos

for elemento in numeros: #for in recorre elemento a elemento
    #puedo escribir logica (funciones) para cada elemento del arreglo
    print(elemento+1)


#range(3)
#[0,1,2]
#range(6)
#[0,1,2,3,4,5]


for numero in range(5):
    print("numero",numero)

for letra in "Python es la luz":
    print(letra)

#ejemplo con range 
#imprimir por consola los numeros pares que se encuentran en los primeros 50 numeros naturales.

# conjunto = [0,1,2,3,4,5......50]

#ejemplo de uso del range
for numero in range(1,51):
    if numero % 2 == 0 and numero %3 ==0:
        print(numero)




# for numero in range(100):
#     if numero == 10:
#         print("pasamos por el 10")
#         break
#     print(numero)

# ejemplo del continue
for numero in range(20):
    if numero % 2 == 0:
        continue
    print(numero)