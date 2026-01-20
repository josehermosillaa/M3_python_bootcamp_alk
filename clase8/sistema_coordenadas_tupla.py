"""
1. Crear una tupla con las coordenadas de una ciudad
2. Mostrar las coordenadas por pantalla
3. Acceder al valor de latitud y longitud por índice
4. Intentar modificar la tupla (y provocar un error)
5. Reemplazar la tupla completa si es necesario (no un solo valor)
6. Usar tuplas dentro de una lista para múltiples registros
7. Iterar sobre la lista de tuplas y mostrar cada ciudad
8. Imprimir mensajes como: "La ciudad está ubicada en (lat, long)"
"""
# Aysen
# Austin texas
# Antofagasta
# Romeral

#(nombre, lat, long)
ciudades = []

while True:
    if len(ciudades) >0:
        for ciudad in ciudades:
            #opcion 1 # ciudad = (nombre, lat, lon)
            nombre, lat, lon = ciudad
            print(f"Ciudad de {nombre}, ubicada en Lat: {lat}, Lon: {lon}")

            # #opcion 2 accediendo a la tupla atraves de los indices
            # nombre = ciudad[0]
            # lat = ciudad[1]
            # lon = ciudad[2]
            # print(f"Ciudad de {ciudad[0]}, ubicada en Lat: {ciudad[1]}, Lon: {ciudad[2]}")
            
    else:
        print("No hay ciudades que mostrar")
    try:

        opcion = int(input(
            """
            1. Agregar ciudad
            2. Salir
            Ingrese una opcion: """
        ))

    except:
        print("Se ha seleccionado una opcion invalida")
    #en caso de existir un error de python, por que al convertir el dato a numero entero no es posible
    #por ejemplo si ingreso un texto, entonces nos manda al bloque except 
    match opcion:
            case 1:
                nombre_ciudad = input("Ingrese el nombre de la Ciudad : ")
                latitud_ciudad = input("Ingrese la  Latitud de la ciudad: ") #se alamacena como texto por simplicidad, en caso de ser numerica se debe validar
                longitud_ciudad = input("Ingrese la Longitud de la ciudad: ")

                ciudades.append((nombre_ciudad, latitud_ciudad, longitud_ciudad))
                print("Se ha ingresado la ciudad de", nombre_ciudad, "correctamente !")
                print()
                continue
            case 2:
                print("Saliendo ....")
                break
            case _:
                print("La opcion ingresada no es valida")
                continue
        
## Implementar un boton para reemplazar una ciudad (tupla completa, ver ejercicio de la lista )