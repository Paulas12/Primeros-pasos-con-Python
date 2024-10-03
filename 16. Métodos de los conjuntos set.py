#Métodos para manipular y acceder a los elementos:

colores = {"rojo", "azul", "verde"}

colores.add("morado")       # Agrega un elemento al conjunto.
print(colores)                  #Imprime {'azul', 'morado', 'verde', 'rojo'}

colores.remove("rojo")      # Elimina un elemento del conjunto. Si el elemento no existe, genera error.
print(colores)                  #Imprime {'azul', 'morado', 'verde'}

#colores.remove("auto")
#print(colores)

colores.discard("azul")     #Elimina un elemento del conjunto si está presente.Si el elemento no existe, no hace nada.
print(colores)              # Imprime {'morado', 'verde'}

colores.discard("arbol")        #Imprime {'morado', 'verde'}
print(colores)
