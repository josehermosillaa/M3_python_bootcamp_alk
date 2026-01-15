habitaciones = {
    1: "Habitación individual - $45.000 por noche",
    2: "Habitación doble - $65.000 por noche",
    3: "Habitación matrimonial - $70.000 por noche",
    4: "Habitación suite - $120.000 por noche",
    5: "Habitación familiar - $150.000 por noche"
}
precio_por_noche = {
    1: 45000,
    2: 65000,
    3: 70000,
    4: 120000,
    5: 150000
}

##### preguntar al usuario el tipo de habitacion 
##### preguntar la cantidad de noches que alojara

tipo_habitacion  = int(input("""
Tipo de habitación:
    1. - Individual
    2. - Doble
    3. - Matrimonial
    4. - Suite
    5. - Familiar                                                    
Que habitacion desea: """))
cantidad_de_noches = int(input("Ingrese la cantidad de noches: " ))
print(f"cantidad de noches seleeccionadas : {cantidad_de_noches}")
match tipo_habitacion:
    case 1:
        print(f"Usted selecciono : {habitaciones.get(tipo_habitacion)}")
        total = cantidad_de_noches * precio_por_noche.get(tipo_habitacion)
        print(f"El total a pagar seran ${total}")
    
    case 2:
        print(f"Usted selecciono : {habitaciones.get(tipo_habitacion)}")
        total = cantidad_de_noches * precio_por_noche.get(tipo_habitacion)
        print(f"El total a pagar seran ${total}")
    
    case 3:
        print(f"Usted selecciono : {habitaciones.get(tipo_habitacion)}")
        total = cantidad_de_noches * precio_por_noche.get(tipo_habitacion)
        print(f"El total a pagar seran ${total}")

    case 4:
        print(f"Usted selecciono : {habitaciones.get(tipo_habitacion)}")
        total = cantidad_de_noches * precio_por_noche.get(tipo_habitacion)
        print(f"El total a pagar seran ${total}")

    case 5:
        print(f"Usted selecciono : {habitaciones.get(tipo_habitacion)}")
        total = cantidad_de_noches * precio_por_noche.get(tipo_habitacion)
        print(f"El total a pagar seran ${total}")
    case _:

        print("Se ingreso una opcion invalida")
    #no olvidar el caso por defecto