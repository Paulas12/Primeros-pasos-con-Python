""" Se puede definir funciones que acepten un número variable de argumentos. 
Esto se logra utilizando el operador * antes del nombre del parámetro.
"""

def suma_variable(*numeros):
    total = 0
    for numero in numeros: 
        total += numero
    return total

#print(funcion(argumentos))
print(suma_variable(1,2,3))     # Imprime 6
print(suma_variable(4,5,6,7))   # Imprime 22