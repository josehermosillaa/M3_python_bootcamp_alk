"""
1. Crear dos listas de usuarios con posibles repetidos
2. Convertir las listas en conjuntos para eliminar duplicados
3. Mostrar los usuarios únicos de cada plataforma
4. Calcular la intersección (usuarios en ambas plataformas)
5. Calcular la unión (todos los usuarios sin duplicados)
6. Calcular diferencia (usuarios solo en una plataforma)
7. Usar add() y remove() para modificar un set
8. Recorrer un set con for e imprimir los resultados
"""

#1
usuarios1 = ["Juan", "Pedro","Juan","Yerko", "Peter", "Diego", "Ana", "Peter"]
usuarios2 = ["Isidora", "Ana", "Yerko", "Fabian", "Ana", "Yerko"]
#2
conjunto_usuario1 = set(usuarios1)
conjunto_usuario2 = set(usuarios2)
#3
print(conjunto_usuario1)
print(conjunto_usuario2)
print("operaciones")
#4 Interseccion

interseccion_u1u2 = conjunto_usuario1.intersection(conjunto_usuario2)
print("interseccion:",interseccion_u1u2)

#5 union
union_u1u2 = conjunto_usuario1.union(conjunto_usuario2)
print("union",union_u1u2)

#6 diferencia
differencia_u1u2 = conjunto_usuario1.difference(conjunto_usuario2)
print("Diferencia u1-u2:", differencia_u1u2)
#no es lo mismo u1-u2 que u2-u1
differencia_u2u1 = conjunto_usuario2.difference(conjunto_usuario1)
print("Diferencia u2-u1:", differencia_u2u1)

#7 agrear y eliminar un elemento
interseccion_u1u2.remove("Yerko")
print("Interseccion se le remueve Yerko con remove",interseccion_u1u2)

interseccion_u1u2.add("Mauro")
interseccion_u1u2.add("Sergio")
print("Se agrega Mauro y sergio a la interseccion",interseccion_u1u2)

#aplicar un for
for elemento in interseccion_u1u2:
    print("elemento: ",elemento)


####ejemplo de uso

usuarios1 = ["Juan", "Pedro","Juan","Yerko", "Peter", "Diego", "Ana", "Peter"]
#obtener una lista de usuarios unicos
usuarios1_unicos = set(usuarios1) #el conjunto nunca tiene datos repetidos
lista_usuarios_unicos = list(usuarios1_unicos) #metodo para transformar un iterable (set{} o tupla )
print(lista_usuarios_unicos)