notas = [6.0, 4.5, -1, 7.0, 0,-6, 5.8, 3.9]

for nota in notas:
    print("Inicio del ciclo")

    # Validación: nota inválida
    if nota <= 0:
        print("Nota inválida, se salta el resto del código")
        continue  # vuelve al inicio del for con la siguiente nota

    # Este código NO se ejecuta si se activó continue
    print("Procesando nota:", nota)

    if nota >= 4.0:
        print("Alumno aprobado")
    else:
        print("Alumno reprobado")

    print("Fin del ciclo")

print("Bucle terminado")