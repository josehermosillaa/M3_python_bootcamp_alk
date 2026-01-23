#argumentos en python

def suma_varios_numeros(*args): #*args me permite ingresar varios parametros y todos ellos seran considerados como una tupla
    resultado = 0
    print(args)
    for numero in args:
        resultado += numero #numerica

    return resultado

print(suma_varios_numeros(1,2,3,4,5,6,7,8,9))
print(suma_varios_numeros(1))
# print(suma_varios_numeros(1,2,"tres", 4,5)) #arroja error


##kwargs key 

def datos_usuario(**kwargs):
    
    #limitar las llaves
    print(kwargs)
    for llave, valor in kwargs.items():
        print(f"llave: {llave}, valor: {valor}")

datos_usuario(nombre="juan", apellido = "perez", edad=35)

#diccionarios con default
def saludo(nombre, apellido = "Perez"):
    print(f"bienvenido {nombre} {apellido}")

saludo("jose", "hermosilla")
saludo("Pablo")