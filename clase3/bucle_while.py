###ejemplos de while

# contador = 0

# while contador < 5:
#     print("la cuenta es: ", contador)
#     #actualizador de la varible
#     # contador = contador + 1
#     contador += 1


decision = True

while decision:
    
    entrada = input("Para ganar pulsa 7: ")

    if entrada == '7':
        print("HAS GANADO EL JUEGO !!!!")
        decision = False
        # break #detiene la ejecucion del bucle
    else:
        print("HAS PERDIDO INTENTALO NUEVAMENTE")