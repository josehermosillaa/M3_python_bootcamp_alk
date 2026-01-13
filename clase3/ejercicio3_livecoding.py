"""Pide al usuario que ingrese su edad.
Convierte la entrada a entero (int).
Verifica que sea un número válido (mayor o igual a cero).
Si la edad es de 0 a 12, imprime que es un niño o niña.
Si está entre 13 y 17, indica que es adolescente.
Si está entre 18 y 64, que es adulto.
Si tiene 65 años o más, clasificalo como adulto mayor.
Muestra el resultado final en pantalla."""

edad = int(input("Ingrese su edad: "))

if edad >= 0:
    print("edad valida")
    if 0 <= edad <= 12:
        print("el usuario es un niño(a)") 
    elif 13 <= edad <= 17:
        print("el usuario es adolescente")
    elif 18 <= edad <= 64:
        print("el usuario es adulto")
    elif  edad >= 65:
        print("el usuario es adulto mayor")
    
else:
    print("edad invalida, intentelo nuevamente")
