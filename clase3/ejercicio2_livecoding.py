"""Pide al usuario un número entero.
-Convierte la entrada con int.
-Usa una condición if con un operador lógico (and) para verificar si el número es divisible por 2 y por 3.
-Si no se cumple, agrega más condiciones para verificar si es par solamente, o si es impar y múltiplo de 3.
-En el caso contrario, indica que es impar y no múltiplo de 3.
-Usa mod (%) para evaluar divisibilidad.
"""

numero = int(input("Ingrese un numero entero: ")) 

"""
por ahora confiamos en el usario, ya que veremos el manejo de errores mas adelante (try/except)
"""

if numero % 2 == 0 and numero % 3 == 0:
    print("el numero ingresado es par y divisible  por 2 y por 3")

elif numero % 2 == 0:
    print("el numero ingresado es par")

elif numero % 2 != 0 and numero % 3 == 0:
    print("El numero es impar y divisible por 3")

else:
    print("el numero es impar y no es divisible por 3")
    