"""Pedir al usuario que ingrese una temperatura en grados Celsius.
Validar que la entrada sea un número.
Clasificar la temperatura usando condiciones múltiples (if, elif, else) en categorías como:
Muy frío: t < 5
Frío: 5 ≤ t < 15
Agradable: 15 ≤ t < 25
Caluroso: 25 ≤ t < 35
Extremo: t ≥ 35
Gestionar errores si el usuario ingresa un valor no numérico.
Separar la lógica en módulos de validación.
"""

from paquete.sensacion_termica import sensacion_termica
try:
    temperatura_usuario = float(input("Ingrese su temperatura en grados Celsius (C°): "))
    respuesta = sensacion_termica(temperatura_usuario)
    print(f"La sensacion termica es {respuesta}")
except:
    print("Temperatura no valida")
