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
    "Avatar": "15:00",
    "Titanic": "16:00" ,
    "Matrix": "17:00", 
}

boletos = {
    "Avatar": 10,
    "Titanic": 5 ,
    "Matrix": 7, 
}
# boletos['Avatar']
# horario = peliculas["Avatar"]
valor_boleto = 8000
