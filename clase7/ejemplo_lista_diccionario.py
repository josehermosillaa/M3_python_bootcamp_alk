reservas = [
    {'nombre':'Avatar',
     'horario':'16:00',
     },
     
    {'nombre':'Titanic',
     'horario':'22:00',
     }
]

for elemento in reservas:
    print(f"las reservas realizadas son:{elemento['nombre']}, {elemento['horario']}")