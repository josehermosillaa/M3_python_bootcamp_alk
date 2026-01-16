#uso del pass

condicion = 2

if condicion == 3:
    pass
#el pass no realiza ninguna accion pero permite que no se levanten errores en python

# while condicion:
#     print(condicion)
#     #todos los valores distinto de False, 0 son considerados True
#     pass

for numero in range(3):
    pass

class Perro:
    pass
# ######
"""imprimir los numeros del uno al 5"""
# print(1)
# print(2)
# print(3)
# print(4)
# print(5)
# print(6)
# print(7)
# print(8)
# print(9)
# print(10)
# print(11)
# print(12)

# for numero in range(1,13):
#     print(numero)

# frutas = ["manzana", "banana", "naranja", "pera", "uva", "frutilla", "kiwi" ]
# #lista, o arreglo de frutas.
# for fruta in frutas:
#     print(f"me gusta {fruta}")


#range crea listas entre el valor de partida (por defecto es 0) hasta el final -1 

# for numero in range(3,61,3):
#     print(numero)

for numero in range(1,11): #el range representa este arreglo [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]    
    print(numero)


#tupla -> es como una lista pero inmutable 
#una tupla se suele usar cuando sabemos que los datos no deben cambiar de posicion en la estructura
tupla = (1, 2, 3, 4, 5, 6, 7)
lista = [1, 2, 3, 4, 5, 6, 7]
print(tupla[0])
#lo que no puedo hacer en una tupla es
# tupla[0] = 3
# lista[0] = 3
print(lista)

# for numero in tupla:
#     print(numero)

"""
TODOS LOS NUMERO EN BOOLEANO SON CONSIDERADOS True excepto el 0
conversiones de datos
int -> numero entero
float -> numero decimal

bool -> de dato a booleano ( True o False)

"""

print(bool(1))
print(bool(10))
print(bool(200))
print(bool('hola'))
print(bool(''))
print(bool())
print(bool(0))
