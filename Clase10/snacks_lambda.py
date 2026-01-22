"""1. Contexto inicial:
Simulamos que tenemos una lista de calorías quemadas por distintas personas tras hacer ejercicio.
2. Uso de map() con lambda:
Queremos transformar esa lista a categorías según el gasto energético:
    Menos de 150 → "Snack liviano"
    Entre 150 y 300 → "Barrita energética"
    Más de 300 → "Smoothie o batido"
3. Usamos map() con una lambda que contenga un condicional con if...else.
4. Uso de filter() con lambda:
5. Extraer solo los entrenamientos intensos (más de 300 cal).
6. Refuerzo del concepto de expresión única:
Mostrar por qué no podemos tener múltiples líneas o print()s dentro de una lambda.
"""
#1. 

calorias = [100,200,300,200,100,450, 350]

#2 y 3
categorias = list(map(lambda x: "Batido" if x>300 else "Barrita Energetica" if 300>= x >=150 else "Snack Liviano", calorias ))

print(categorias)

# #4
# entrenamientos_intensos = list(filter(lambda x: x > 300, calorias))
# print(entrenamientos_intensos)

#5
intensos = list(filter(lambda x: x>300, calorias))

print(intensos)

# f = lambda x: x+1 x+2

# f = lambda x: print(x) 
# x+1