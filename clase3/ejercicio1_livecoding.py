numero1 = input("por favor ingrese un numero decimal: ")

# numero1 = int(numero1) #esto convierte el texto a entero
#float(10) -> 10.0
#float(2) -> 2.0
# try:
#     numero1 = float(numero1)
# except:
#     print("el numero no es valido")


numero1 = float(numero1)
#alternativa de los 2 primeros pasos
# numero1 = float(input("por favor ingrese un numero decimal: "))

if numero1 > 0:
    print("el número ingresado es mayor a cero (positivo)")
elif numero1 < 0 :
    print("el número ingresado es menor que cero (negativo)")
else:
    print("El número ingresado es igual a cero")