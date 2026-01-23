print("Este sitio es para mayores de 18 años")

def validacion_edad(edad):
    if edad >= 18:
        print("Bienvenido al sitio Web")
    else:
        print("Usuario menor de edad, adios")



try:
    edad_usuario = int(input("Ingrese su edad: "))
    validacion_edad(edad_usuario)
except:
    print("Valor ingresado no valido")
