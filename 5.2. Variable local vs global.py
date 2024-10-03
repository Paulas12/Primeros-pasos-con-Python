def funcion():
    variable_local = 10
    print(variable_local)  # Definida dentro de la función: solo se puede acceder a ella dentro de la funcion 


variable_global = 20


def funcion2():
    print(variable_global)  # Definida fuera de la función: Accesible desde cualquier parte del programa 


funcion()  # Imprime 10
funcion2()  # Imprime 20
print(variable_global)  # Imprime 20
print(variable_local)  # Genera un error, la variable no está definida en este alcance.