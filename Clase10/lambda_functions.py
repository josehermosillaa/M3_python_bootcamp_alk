
suma = lambda a,b: a + b
resultado = suma(10,9)

# print(resultado)

numeros = [1,2,3,4,5,6,7,8,9]
cuadrados = list(map(lambda x: x**2, numeros)) #lo que hace map es aplicar la funcion a cada elemnto del iterable
#mapeo
print(cuadrados)


cuadrado_pares = list(filter(lambda x: x%2 == 0, cuadrados ))#filter deja los valores que devuelvan true a la funcion del primer argumento
#[1,4,9,16,25,36,49,64,81], cuales son pares
#[False, True, False, True, False, True, False,True, False]
#filter me dejaria solo los elementos con True [4,16,36,64]
print(cuadrado_pares)

#NO CONFUNDIR CON COMPRESION DE LISTAS
# [x**2 for x in range(10)]