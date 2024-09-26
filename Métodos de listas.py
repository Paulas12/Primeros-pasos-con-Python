frutas = ["manzana", "banana", "naranja"] #[]

frutas.append("pera")       #agrega un elemento al final de la lista
print(frutas)

frutas.insert(1, "uva")     #insert(indice, elemento): inserta un elemento en una posicion especifica de la lista
print(frutas)

frutas.remove("banana")     #elimina la primera aparicion del elemento en la lista
print(frutas)

fruta_eliminada = frutas.pop(2)  #elimina y devuelve el elemento en una posición específica de la lista
print(frutas)
print(fruta_eliminada)

numeros = [7,2,3,6,1,5,8,4,0]
numeros.sort()  #ordena los elementos de la lista en orden ascendente
print(numeros)

frutas.reverse()    #invierte el orden de los elementos en la lista
print(frutas)