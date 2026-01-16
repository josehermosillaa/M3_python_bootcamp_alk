#####
# ciclo for y el ciclo while

# una lista

avengers_endgame = [
    "Iron Man",
    "Captain America",
    "Thor",
    "Hulk",
    "Black Widow",
    "Hawkeye",
    "Spider-Man",
    "Doctor Strange",
    "Scarlet Witch",
    "Vision",
    "Falcon",
    "Winter Soldier",
    "War Machine",
    "Ant-Man",
    "Wasp",
    "Black Panther",
    "Shuri",
    "Okoye",
    "M'Baku",
    "Star-Lord",
    "Gamora",
    "Drax",
    "Rocket Raccoon",
    "Groot",
    "Nebula",
    "Wong",
    "The Ancient One",
    "Captain Marvel"
]

#metodo enumerate nos sirve para poder trabajar con tuplas que nosentregan (posicion del elemento, elemento)
#metodo len permite saber el largo de una lista

print(len(avengers_endgame)) 

# for avenger in avengers_endgame:
#     print(avenger)

# pero vimos tambien el metodo enumerate

# for posicion , avenger in enumerate(avengers_endgame):

#     print(posicion, avenger)

# for elemento in enumerate(avengers_endgame):

#     print(elemento)

lista_vacia = []
#las listas tienen metodos que permiten agregar elementos o quitar elementos en ellas

#para agregar un elemento
lista_vacia.append("Diego")
lista_vacia.append("Yerko")
lista_vacia.append("Sergio")

lista_vacia.append((10,"pizza"))
#metodo append agrega un elemento al final de la lista
lista_vacia.insert(0,("Hola", "Mundo"))
print(lista_vacia)
#con el metodo pop eliminamos el ultimo elemento de la lista (izquierda a derecha)
lista_vacia.pop()
#si le indico un indice como argumento me elimina ese elemento especifico
print(lista_vacia)
lista_vacia.pop(1)
print(lista_vacia)
