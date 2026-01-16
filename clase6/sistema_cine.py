"""Mostrar una lista de películas disponibles con horarios.
Permitir al usuario seleccionar una película y la cantidad de boletos.
Validar la disponibilidad de boletos.
Mostrar el resumen final con la película, el número de boletos y el precio total.
Permitir nuevas reservas hasta que el usuario decida salir."""
"""
1️⃣ Definir un diccionario con películas y horarios.
2️⃣ Usar un while para mostrar el menú y permitir que el usuario haga selecciones repetidas hasta que decida salir.
3️⃣ Solicitar la película y la cantidad de boletos.
4️⃣ Verificar disponibilidad de boletos antes de confirmar la compra.
5️⃣ Calcular el precio total basado en la cantidad de boletos comprados.
6️⃣ Permitir agregar más reservas o finalizar la compra.
7️⃣ Mostrar un resumen final con todas las reservas realizadas y el costo total.
"""

peliculas = {
    "Avatar": ["15:00","16:00"],
    "Titanic": ["16:00","17:00"] ,
    "Matrix": ["17:00","18:00"], 
}

boletos = {
    "Avatar": [10,5], #cantidad de boletos por funcion
    "Titanic": [5,4] ,
    "Matrix": [7,20], 
}
# boletos['Avatar']
# horario = peliculas["Avatar"]
valor_boleto = 8000
reservas = []  #-> list()
while True:
    pelicula = '' 
    horario = ''
    cantidad_boletos = 0

    opcion = int(input("""
    BIENVENIDOS AL SISTEMA DE CINE:
    SELECCIONE SU PELICULA:
        1. Avatar
        2. Titanic
        3. Matrix
        4. Salir
    """))
    
    if opcion == 1:
        pelicula = "Avatar"
    elif opcion == 2:
        pelicula = "Titanic"
    elif opcion == 3:
        pelicula =="Matrix"
    elif opcion == 4:
        if len(reservas) >0:
            print("El resumen de las reservas  realizadas es")
            for indice, reserva in enumerate(reservas): # indice del elemento, valor
                print(f"""
                        {indice + 1} : {reserva["pelicula"]},en el horario {reserva["horario"]},con  {reserva["boletos"]} boletos,por un total {reserva["total"]} 
                        """)

        print("saliendo del sistema ....")
        break
    else:
        print("Opcion no valida")
        print()
        continue

    print("Horarios disponibles: ")
    print() #salto de linea

    for index, horario in enumerate(peliculas[pelicula]):  #peliculas[pelicula] -> accedo a los horarios disponibles
        print(f"{index+1} : {horario}")

    opcion_horario = int(input("Seleccione el horario: "))
    opcion_horario -= 1
    horario = peliculas[pelicula][opcion_horario] 
            #peliculas['Avatar'][1] -> 16:00

    print(f"La cantidad de boletos para ese horario es {boletos[pelicula][opcion_horario]}")

    boletos_usuario = int(input("Ingrese la cantidad de boeltos a comprar: "))
    cantidad_boletos = boletos[pelicula][opcion_horario]
    if cantidad_boletos < boletos_usuario:
        print("la cantidad ingresada de boletos supera a los disponibles")
        continue

    total_a_pagar = boletos_usuario * valor_boleto

    print(f"El total a pagar seran de {total_a_pagar} ")
    boletos[pelicula][opcion_horario] = cantidad_boletos - boletos_usuario

    reservas.append({
        "pelicula" : pelicula,
        "horario" : horario,
        "boletos" : boletos_usuario,
        "total" :total_a_pagar

    })