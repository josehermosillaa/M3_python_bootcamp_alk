"""
Crear un menú con while True que permita al usuario interactuar con una lista de tareas.
Las opciones del menú deben incluir: agregar tarea, ver tareas, marcar tarea como hecha, y salir.
Utilizar break para salir del programa y continue para volver al menú sin ejecutar código extra.
Simular la gestión de tareas usando listas y diccionarios con campos como "tarea" y "completado".
Separar el código en módulos menu.py y gestion_tareas.py.
"""

tareas = []
# {
#     "tarea":"limpiar la cocina"
#     "estado": "Realizada" #no realiza
# }
while True:

    opcion = int(input(
"""
Tareas !
1. Agregar tarea
2. Ver tareas
3. Marcar tarea como Realizada
4. Salir
"""
    ))

    if opcion == 1:
        print("Agregando Tarea.....")
        nueva_tarea = input("Ingrese la tarea a realizar: ")

        tareas.append({
            "tarea":nueva_tarea,
            "estado":"No Realizada"
        })
        continue
    elif opcion == 2:
        if len(tareas)>0:
            print("Lista de tareas")
            
            for posicion,elemento in enumerate(tareas): #(posicion, elemento de la lista)
                print(f"{posicion+1} : {elemento["tarea"]}, Estado: {elemento["estado"]} ")
                
            print()
            continue
        else:
            print("No ha agregado ninguna tarea")
            print()
            continue
    elif opcion == 3:
        print("Lista Tareas")
        for posicion,elemento in enumerate(tareas): #(posicion, elemento de la lista)
                print(f"{posicion+1} : {elemento["tarea"]}, Estado: {elemento["estado"]} ")
        print() 
        opcion_realizada = int(input("Seleccione la tarea Realizada: "))
        opcion_realizada -= 1
        tarea_a_cambiar = tareas[opcion_realizada] #selecciona el diccionario de la lista de tareas
        
        if tarea_a_cambiar["estado"] =='Realizada':
             print("La tarea ya se encontraba como Realizada")
             continue
        else:
             tareas[opcion_realizada]["estado"] = "Realizada"
             continue
    elif opcion == 4:
         print("Saliendo del programa......")
         break
    else:
         print("opcion no valida")
         continue