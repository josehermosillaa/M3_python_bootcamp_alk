"""Podemos devolver mas de un valor en la funcion"""
#se usara para explicar el ambito de una variable
#una variable global es aquella que se puede acceder en cualquier parte del script

variable_global = "Perrito"

def calculos_varios(numero_1, numero_2):

    suma = numero_1 + numero_2
    resta = numero_1 - numero_2
    division = numero_1/numero_2
    multiplicacion = numero_1 * numero_2
    potencia = numero_1**numero_2

    print(variable_global)

        
        
    return suma, resta, division, multiplicacion, potencia

def otra_suma(a,b):
    suma = a + b


tupla = (1,2,3)
tupla_igual = 1,2,3
print(tupla == tupla_igual)

resultado_suma, resultado_resta, resultado_division,resultado_multiplicacion, resultado_potencia = calculos_varios(2,3)
print(resultado_suma)
print(resultado_resta)
print(resultado_division)
print(resultado_multiplicacion)
print(resultado_potencia)



def procedimiento():

    print("Bienvenido al sistema")
    print("Seleccione una de las opciones disponibles")
