habitaciones = {
    1: "Habitación individual - $45.000 por noche",
    2: "Habitación doble - $65.000 por noche",
    3: "Habitación matrimonial - $70.000 por noche",
    4: "Habitación suite - $120.000 por noche",
    5: "Habitación familiar - $150.000 por noche"
}

##### preguntar al usuario el tipo de habitacion 
##### preguntar la cantidad de noches que alojara

tipo_habitacion  = int(input(""))
cantidad_de_noches = int(input(""))
print(f"cantidad de noches seleeccionadas : {cantidad_de_noches}")
match tipo_habitacion:
    case 1:
        print(f"Usted selecciono : {habitaciones.get(tipo_habitacion)}")
        total = cantidad_de_noches * 45000
        print(f"El total a pagar seran ${total}")
    case 2:
        pass
    case 3:
        pass
    #no olvidar el caso por defecto