#Es una estructura de datos mutable y no ordenada que permite almacenar una colección de elementos únicos.

frutas = {"manzana", "banana", "naranja"}       #los conjuntos se crean entre {}
numeros = set([1,2,3,4,5])                      # O se crean utilizando la funcion set()

conjunto1 = {1,2,3}
conjunto2 = {3,4,5}

union = conjunto1 | conjunto2
print(union)                        #Imprime {1,2,3,4,5}

interseccion = conjunto1 & conjunto2
print(interseccion)                 #Imprime {3}

diferencia = conjunto1 - conjunto2
print(diferencia)                   #Imprime {1,2}

diferencia_simetrica = conjunto1 ^ conjunto2 
print(diferencia_simetrica)         #Imprime {1,2,3,4,5}
