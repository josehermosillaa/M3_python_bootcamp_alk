"""
1. Simular un cajero automático que solicite un PIN al usuario.
    a. Permitir hasta 3 intentos antes de bloquear el acceso.
2. Configurar variables iniciales
    a. Almacenar un PIN correcto (ejemplo: pin_correcto = "1234").
3. Usar un ciclo while para validar intentos
    a. Permitir al usuario ingresar el PIN.
    b. Reducir el número de intentos después de cada intento fallido.
    c. Bloquear el acceso tras 3 intentos incorrectos.
4. Usar break para finalizar el ciclo
    a. Si el usuario ingresa el PIN correcto, terminar el ciclo.
    b. Mostrar un mensaje de bienvenida si el PIN es correcto.
5. Ejecutar y Validar.
"""

pin_correcto = "1234"
intentos = 1

while intentos <= 3:
    pin = input("Ingrese su PIN de 4 digitos: ")
    #podemos contar la cantidad de letras de un texto con el metodo len() de python
    if len(pin) == 4: #permite validar que el texto ingresado tenga 4 elementos
        if pin == pin_correcto:
            print("El PIN es correcto. Bienvenido.")
            break
        else:
            print("El PIN Ingresado no es correcto")
            intentos +=1
            if intentos == 4:
                print("Se ha alcanzado el limite de intetos, clave bloqueada")
            continue

    else:
        print("El PIN debe tener 4 dígitos.")
        intentos +=1
        if intentos == 4:
            print("Se ha alcanzado el limite de intetos, clave bloqueada")
        continue   
    