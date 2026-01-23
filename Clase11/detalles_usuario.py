"""Crear un procedimiento que imprima los detalles de un usuario:
El primer procedimiento mostrará en pantalla información personal de un usuario: su nombre, edad y una lista de intereses.
 Se enfatizará cómo recibir múltiples parámetros y recorrer una lista con un bucle para imprimir cada interés individualmente.
"""

nombre = input("Ingrese su nombre: ")
edad = input("Ingrese su edad: ")
intereses = []

while True:
    print("""
Ingresa tus intereses personales:
    1 Ingresar nuevo interes
    2 Salir
""")
    opcion = input("Ingrese una opcion de la lista: ")

    if opcion == "1":
        interes = input("Escribe tu interes aqui: ")
        intereses.append(interes)
        continue
    elif opcion == "2":
        print("Saliendo..")
        break

def detalles_usuario(nombre,edad, intereses):
    print(f"Hola {nombre} de edad {edad}")
    print("tus intereses son :")

    for interes in intereses:
        print(interes)

detalles_usuario(nombre, edad, intereses)