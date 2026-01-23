"""
Calculo del factorial
!0 = 1
!1 = 1
!2 =1*2 = !1*2
!3 = 1*2*3 = !2*3
!4 = 1*2*3*4 = !3*4
!5 = 1*2*3*4*5 = !4*5
!6 = 1*2*3*4*5*6 = !5*6 .... 
                factorial(n-1) *n
"""

def factorial(numero):
    """el factorial sirve para los numeros > 0"""

    if numero<0:
        print("No se puede calcular el factorial de un numero negativo")
        return
    # elif numero == 0:
    #     return 1
    # elif numero == 1:
    #     return 1    
    elif numero == 0 or  numero ==1 :
        return 1
    else:
        return factorial(numero-1)*numero