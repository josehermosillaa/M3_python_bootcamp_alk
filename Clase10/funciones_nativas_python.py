"""Parte 1 – Funciones de conversión y tipo
int(), float(), str(), bool()
Convertir strings a números y viceversa
¿Qué devuelve bool(""), bool(0), bool("Hola")?
"""
#type() #medice class "tipo del dato que tenemos"

numero = 1
print(numero,"es de tipo",type(numero))
numero = float(numero)#convierte a decimal
print(numero,"es de tipo",type(numero))
numero = str(numero) #convierte numerop a string o texto
print(numero,"es de tipo",type(numero))
numero = bool(numero) #transformo a bool
print(numero,"es de tipo",type(numero))
print(bool("")) # False  #texto vacio se considera False
print(bool(0)) #False los 0 se consideran False
print(bool("Hola")) #True # cualquiero otro texto que no sea vacio
print(bool("False")) #True # cualquiero otro texto que no sea vacio se considera True

#puedo verificar un texto vacio asi 
# if texto == "" :

"""Parte 2 – Verificación de tipos
type() e isinstance()
Mostrar cómo saber el tipo de una variable
Preguntar: ¿Cuál es la diferencia entre type() e isinstance()?
"""
print()
print("parte 2")
texto = "Hola mundo"
print(type(texto))
print(isinstance(texto,str))
print(isinstance(texto,int))
print(isinstance(texto,float))
print(isinstance(texto,list))
print(isinstance(texto,dict))

if isinstance(texto,list):
    #accion a realizar
    pass


"""Parte 3 – Colecciones
len(), list(), dict(), tuple()
Mostrar la longitud de listas o strings
Convertir una cadena a lista de caracteres
"""
print()
print("parte 3")
lista = [1, "a", 2,"b"]
print(len(lista)) #obtenemos el largo de la lista, se puede usar en tuplas y en conjuntos
tupla_lista = tuple(lista)
print(tupla_lista)
print("Largo tupla",len(tupla_lista))
lista_2 = list(tupla_lista)
print(lista_2)

#tambien podemos convertir a conjunto con set()

#podemos convertir elementos a diccionarios, pero debe ser una lista de tuplas

datos = [(1,"a"),(2,"b"),(3,"c")]
nuevo_diccionario = dict(datos)
print(nuevo_diccionario, "de largo", len(nuevo_diccionario)) # el len cuenta la cantidad de pares llave valor que existen
# print(dict(lista))

"""Parte 4 – Entrada y salida
input() y print()
Pedimos al usuario su edad y mostramos una respuesta formateada
"""
print()
print("Parte 4")
edad = input("Ingrese su edad: ")
print(f"su edad es {edad}")


"""Parte 5 – Números y rango
range(), round()
Imprimir números del 1 al 5 con range()
Redondear valores decimales a entero y a n decimales
"""
for numero in range(7):
    print(numero)
print('aqui usamos round')
PI = 3.141516
print(round(PI,3)) #primer argumento el numero a redondear, segundo argumento cantidad de decimales
