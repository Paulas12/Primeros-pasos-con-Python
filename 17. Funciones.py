#Para definir la funcion usamos la palabra clave def seguida del nombre de la función y paréntesis.

def saludo ():
    print("¡Hola mundo!")

saludo()    #Imprime ¡Hola mundo!. Se llama a la función.


#Funciones con parámetros y argumentos
def saludo(nombre): 
    print(f"¡Hola, {nombre}!")          #Las funciones pueden aceptar parámetros, que son valores que se pasan a la función cuando se la llama. 
                                        #Los parámetros se especifican dentro de los paréntesis en la definición de la función.

    saludo("Juan")                      #Al llamar a la función, proporcionamos los argumentos correspondientes a los parámetros.
    saludo("María")
