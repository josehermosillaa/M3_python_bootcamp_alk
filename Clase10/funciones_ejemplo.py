#funcion de ejemplo 

"""Parte 1 – Crear una función básica sin parámetros
Mostramos cómo usar def
Escribimos una función saludar() que imprima un mensaje
Ejecutamos varias veces su invocación
Discutimos por qué es útil reutilizar funciones

"""

def saludar(): #funcion sin argumentos
    #instrucciones
    print("Hola a todos los presentes!")
    #funcion no retorna nada

# saludar()

#nos permiten reducir y reutilizar el codigo


"""Parte 2 – Función que retorna un valor
Creamos una función multiplicar(a, b) que retorne el resultado
Leemos dos números con input()
Mostramos el resultado llamando a la función
Explicamos la diferencia entre mostrar y retornar"""

def multiplicar(a,b):
    print("Resultado: ", a * b)
    return a * b #si no retorno nada al querer almacenar la funcion obtendremos un None

# print("vamos a multiplicar")
# numero_1 = int(input("Ingrese el primer numero: "))
# numero_2 = int(input("Ingrese el Segundo numero: "))
# multiplicar(numero_1, numero_2) #lo que se almacena en resultado es el retorno de la funcion

# print(multiplicar(numero_1, numero_2))
# print("el resultado de la multiplicacion es: ", resultado)

"""
Parte 3 – Crear una función con parámetros
Definimos una función bienvenida(nombre)
Le pedimos al usuario su nombre
Llamamos a la función pasándole ese valor
Mostramos cómo el mensaje cambia dinámicamente

"""

def bienvenida(nombre):
    print(f"Bienvenid@ {nombre}, que disfrute su estadia!")

bienvenida("juan")
bienvenida("jose")
nombre_usuario = input("Ingrese su nombre: ")
bienvenida(nombre_usuario)