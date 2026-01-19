"""
Las lista son ordenadas y mutables (que el contenido puede cambiar su posicion)

para definir la posicion en la lista se usan los indices, se cuentan desde el 0 de izquierda a derecha

"""

lista =  []  #lista vacia
nombres =           [ "Ana", "Diego", "Yerko", "Iris", "Jesus", "Cristian", "Mauro" ]
#orden en la lista     0        1         2        3       4         5         6
# estos son los indices para la lista nombres 

mezcla = [ 1, "Texto", True, 3.14, [ 1, 2, 3], {"nombre":"Juan","edad":18}, (1,"juan"), {1,2,3} ]
#el ultimo elemento es un conjunto (set) se vera al final de la clase.

#Tarea imprimir los nombres con indice 1, 3,5 sin usar ciclo for
print(nombres[0])

#modificamos el nombre de la lista nombres con el indice 1
nombres[1] = "Dieguito" # nombre = "Dieguito"

print(nombres)
"""
el caso de la lista de tareas
#modificar la tarea, buscamos el indice y la sobreescribimos

"""

nombres =           [ "Ana", "Diego", "Yerko", "Iris", "Jesus", "Cristian", "Mauro" ]
#orden en la lista     -7      -6        -5      -4      -3         -2        -1
#pero existe una notacion para los indices inversa es decir de derecha a izqquierda

print(nombres[-1]) #ultimo termino de la lista
print(mezcla[-1]) #ultimo termino de la lista


""" Metodos utiles de las listas"""

tareas = [ "Enviar WhatsApp", "Terminar Informe" ]

#agregar un elemento al final de la fila

tareas.append("Revisar codigo")
print(tareas) #['Enviar WhatsApp', 'Terminar Informe', 'Revisar codigo']

#agregar un elemento en una posicion especifica
#metodo insert
tareas.insert( 1, "Llamar cliente" ) 
print(tareas)#['Enviar WhatsApp', 'Llamar cliente', 'Terminar Informe', 'Revisar codigo']

#eliminar un elemento por indice
tareas.pop(0)
print(tareas)#['Llamar cliente', 'Terminar Informe', 'Revisar codigo']
#si no le damos el indice, se elimina el ultimo elemento de la lista
tareas.pop()
print(tareas)#['Llamar cliente', 'Terminar Informe']


#buscar el indice de un elemento 
test = ["hola", "mundo", "mundo"]
indice = test.index("mundo") # me dara el indice del primer elemento que encuentre
print(indice)

# ordanmiento de la lista
letras = ["a","z", "n","j","e"]
letras.sort()
print(letras)

#invertir el orden
letras.reverse()
print(letras)

#count cuenta la cantidad de apariciones de un elemento en una estructura de dato

#contar la cantidad de elementos de una lista
print(len(letras))#5 