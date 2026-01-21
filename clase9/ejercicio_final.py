from collections import Counter
"""
1. Crear un diccionario llamado libros donde la clave sea un ID ("B001", "B002", etc.)
2. Cada valor será un diccionario con:

"titulo": cadena
"autor": tupla con (nombre, año de nacimiento)
"genero": cadena
"stock": entero

3. Mostrar todos los libros disponibles
4. Permitir buscar libros por género ingresado por el usuario
5. Calcular cuántos libros hay por género usando Counter
6. Mostrar solo los libros con stock menor a 3 unidades
7. Agregar un nuevo libro y actualizar el stock de uno existente
8. Bonus: Eliminar un libro del diccionario por su código"""


#1 #2
libros = {
    "B001": {
        "titulo": "1984",
        "autor": ("George Orwell", 1903),
        "genero": "Distopía",
        "stock": 5
    },
    "B002": {
        "titulo": "El Hobbit",
        "autor": ("J. R. R. Tolkien", 1892),
        "genero": "Fantasía",
        "stock": 2
    },
    "B003": {
        "titulo": "Dune",
        "autor": ("Frank Herbert", 1920),
        "genero": "Ciencia ficción",
        "stock": 1
    },
    "B004": {
        "titulo": "Fahrenheit 451",
        "autor": ("Ray Bradbury", 1920),
        "genero": "Distopía",
        "stock": 4
    },
    "B005": {
        "titulo": "El nombre de la rosa",
        "autor": ("Umberto Eco", 1932),
        "genero": "Misterio",
        "stock": 3
    },
    "B006": {
        "titulo": "Crónica de una muerte anunciada",
        "autor": ("Gabriel García Márquez", 1927),
        "genero": "Novela",
        "stock": 6
    },
    "B007": {
        "titulo": "Neuromante",
        "autor": ("William Gibson", 1948),
        "genero": "Ciencia ficción",
        "stock": 2
    },
    "B008": {
        "titulo": "La sombra del viento",
        "autor": ("Carlos Ruiz Zafón", 1964),
        "genero": "Novela",
        "stock": 1
    }
}
#quiero obtener el autor del liubro B008
#nombre del autor
libros["B008"]["autor"][0]
#año de nacimiento del autor
libros["B008"]["autor"][1]

#3
#libros.values() -> [{..},{...},...] lista de los diccionarios que se encuentran dentro de la llave B001, B002 etc
# como autor se encuentra en una tupla debemos acceder a el con su indice
generos = []

for libro in libros.values():
    print(f"Titulo: {libro["titulo"]}| Autor: {libro["autor"][0]}| Genero: {libro["genero"]} | Stock: {libro["stock"]}")
    #mientras imprimo los datos voy almacenando el genero del libro en la lista generos
    
    #esto es para agregar 1 genero por libro, tomando en cuenta el stock
    for stock in range(libro["stock"]): #range(1) -> [0]  range(3) -> [0,1,2], range(5)-> [0,1,2,3,4], range(2) -> [0,1]
        generos.append(libro["genero"])

#4. Permitir buscar libros por género ingresado por el usuario

#ahora debemos  mostrar al usuario los generos disponibles, para que sepa que generos buscar

#debemos dejar la lista con elementos unicos
""" funciones para transformacion de estructuras de datos
set()  transforma un iterable en uyn conjunto
list() transforma un iterable en una lista
tuple() transforma un iterable en una tupla
dict() transforma una lista de  tuplas en diccionario llave valor
 dict([('clave1', 'valor1'), ('clave2', 'valor2')])
"""
conjunto_generos = set(generos) #el conjunto elimina los datos duplicados

lista_generos_unicos = list(conjunto_generos)  
# generos = list(set(generos))
print("")
print("Generos disponibles")
for genero in lista_generos_unicos:
    print("-",genero)

while True:
    opcion = input("Ingrese el genero a buscar (debe respetar tildes y espacios) :")

    if opcion in lista_generos_unicos: #si encuentra el genero en la lista de los generos entonces imprime los libros para ese genero
        for libro in libros.values():
            
            if opcion == libro["genero"]:
                print(f"Titulo: {libro["titulo"]}| Autor: {libro["autor"][0]}| Genero: {libro["genero"]} | Stock: {libro["stock"]}")

        break#el break detiene un ciclo
    else:
        print("Genero no disponible, ingrese una opcion de la lista")
        continue

#5. Calcular cuántos libros hay por género usando Counter

#necesitamos una lista de los generos?

libro_por_genero = Counter(generos)  #lista de generos creada anteriormente 
# print(libro_por_genero)
print("Cantidad de libros por genero: ")

for llave, valor in libro_por_genero.items():
    print(f"{llave}: {valor}")

# 6. Mostrar solo los libros con stock menor a 3 unidades
print()
print("Libros con stock menor a 3 unidades")
for libro in libros.values():
    if libro["stock"]<3:
        print(f"Titulo: {libro["titulo"]}| Autor: {libro["autor"][0]}| Genero: {libro["genero"]} | Stock: {libro["stock"]}")

# 7. Agregar un nuevo libro y actualizar el stock de uno existente
print()
print("*********Actualizacion*********")
libros["B009"] =  {
        "titulo": "La psicologia del dinero",
        "autor": ("Morgan Housel",1990 ),
        "genero": "Autoayuda",
        "stock": 2
    }

#editamos stcok a B007

libros["B007"]["stock"] = 1

#8. Bonus: Eliminar un libro del diccionario por su código"""

libros.pop("B003")

for libro in libros.values():
    print(f"Titulo: {libro["titulo"]}| Autor: {libro["autor"][0]}| Genero: {libro["genero"]} | Stock: {libro["stock"]}")