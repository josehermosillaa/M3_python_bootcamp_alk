"""1.Uso de for para recorrer una lista
Queremos imprimir los nombres de una lista de estudiantes."""

# personajes = [
#     "Arnold", "Helga", "Gerald",
#     "Phoebe", "Harold", "Sid",
#     "Stinky", "Rhonda", "Eugene",
#     "Curly", "Brainy", "Lila",
#     "Sheena", "Olga", "Abuelo Phil",
#     "Abuela Gertie", "Señor Hyunh",
#     "Ernie", "Oscar", "Suzy"
# ]

# for nombre in personajes:
#     print("el nombre del personaje es: ", nombre)




"""2.Uso de while con una condición de parada
Pedimos un número al usuario y seguimos sumando hasta llegar o superar 50."""

# numero =  int(input("ingrese un numero:"))
# #no olvidar transformar el texto a numero

# while numero <= 50:
#     print(numero)
#     numero+=1

# print("ejecucion terminada")


"""3.Uso de break para detener un bucle
Se detiene la búsqueda de un número en una lista cuando se encuentra el número 7."""

numeros = [ 1, 2, 3, 5, 7, 8, 9, 12]
# #           0  1  2  3  4  5  6   7          indices para una lista de python 
# #numeros[0] = 1
# #numeros[1] = 2
# #numeros[2] = 3
# #numeros[3] = 5
# #numeros[4] = 7
# #numeros[5] = 8
# #numeros[6] = 9
# #numeros[7] = 12
# #tiene una posicion en python
# contador = 0 
# while True:
#     if  numeros[contador] == 7:
#         print("encontramos el 7")
#         break
#     print(numeros[contador])
#     contador +=1

# for numero in numeros:
#     if  numero == 7:
#         print("encontramos el 7")
#         break
#     print(numero)
    




"""4.Uso de continue para saltar iteraciones
Imprimir los números del 1 al 10, pero saltar los múltiplos de 3.
"""

for numero in range(1,11):
#recordar el range se mueve desde numero inicial inclusive y el final sin considerarlo o final -1
    if numero % 3 == 0:
        continue
    print(numero)