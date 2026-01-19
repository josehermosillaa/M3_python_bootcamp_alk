"""
1. Crear una lista inicial con tareas
2. Mostrar todas las tareas actuales
3. Agregar una nueva tarea a la lista
4. Marcar una tarea como completada (eliminarla)
5. Recorrer e imprimir la lista de tareas con un for
6. Usar pop() para eliminar tareas por índice
7. Validar si la lista está vacía
8. Mostrar mensaje de cierre: "¡Todas las tareas completadas!"
"""

tareas_hogar = [
    "Barrer la casa",
    "Trapear el piso",
    "Lavar los platos",
    "Sacar la basura",
    "Hacer la cama",
    "Limpiar el baño",
    "Ordenar la habitación",
    "Lavar la ropa",
    "Tender la ropa",
    "Cocinar"
]
#usaremos break para salir del while
#o continue para volver al comienzo del ciclo
while True: 
    print("TODO")
    if len(tareas_hogar)>0:
        for indice, tarea in enumerate(tareas_hogar): #me devuelve una tupla del indice y la tarea de la lista
            print(f"{indice+1} : {tarea}")
    else:
        print("no quedan tareas por realizar :( ")
        print('Saliendo .....')
        break
    #En caso que no existan mas tareas salimos del programa tambien
    opcion = int(input("""    
    1. Agregar Tarea
    2. Marcar Tarea como completada
    3. Salir
                    
    Seleccione una opcion: """))
    
    if opcion == 1:
        nueva_tarea = input("Ingrese nueva tarea: ")
        tareas_hogar.append(nueva_tarea)
        print("Se agrego la nueva tarea")
        print()
        continue
    elif opcion == 2:
        opcion_tarea = int(input("Ingrese el numero de la tarea a eliminar: "))
        opcion_tarea -= 1

        tareas_hogar.pop(opcion_tarea)
        print(f"Se a eliminado la tarea {opcion_tarea+1}")

        continue
    elif opcion == 3 :
        total_tareas = len(tareas_hogar) #canitdad total de tareas
        print(f"Tareas por realizar {total_tareas}")
        print("Saliendo del sistema....")
        break
    else:
        print("Opcion no valida")
        continue
