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

    opcion = int(input(
        """
        1. Agregar ciudad
        2. Salir y Mostrar
        """
    ))