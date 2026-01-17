def sensacion_termica(temperatura):
    if temperatura < 5:
        return "Muy frio"
    elif 5<= temperatura < 15:
        return "Frio"
    elif 15<= temperatura < 25:
        return "Agradable"
    elif 25<= temperatura < 35:
        return "Caluroso"
    elif 35 <= temperatura :
        return "Extremo"
