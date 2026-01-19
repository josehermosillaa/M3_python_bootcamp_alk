"""
Las tuplas funciona de forma similar a las listas con la diferencia que no permiten la modificacion de la posicion de la tupla
inmutable
"""

tupla = (1, 2, 3)
otra_tupla = 1, 2, 3    # tupla == otra_tupla
print(tupla)
print(otra_tupla)

tupla_mixta = True, 1, 3.14, "perrito", [1,2,3, True] # tupla
tupla_mixta2 = (True, 1, 3.14, "perrito", [1,2,3, True]) # tupla
 
# print(tupla_mixta)

ejemplo = (1, 2, 3, 2, 3)
#indices   0  1  2  3  4

print(ejemplo.count(2)) # cuenta la cantidad de veces que aparece un elemento en la tupla(tambien funciona para listas)

print(len(ejemplo)) #me da el largo de la tupla 

print(ejemplo.index(3)) #me devuelve el indice del primer elemento que coincida en la tupla


#una tupla no permite 
# ejemplo.append(10)
#permite acceso por indice
print(ejemplo[-1])

#pero no permite modificar los elementos

# ejemplo[-1] = 10


""" cosa importante en python de las tuplas es la asignacion multiple en una linea"""
#("Juan", 14, True) caracteristica de una persona
tupla_ejemplo = ("Juan", 14, True)
"""
nombre = tupla_ejemplo[0]
edad = tupla_ejemplo[1]
tiene_licencia = tupla_ejemplo[2]
"""

nombre, edad, tiene_licencia = ("Juan", 14, True)
# nombre, edad, tiene_licencia = "Juan", 14, True

