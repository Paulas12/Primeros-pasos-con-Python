#Aunque las tuplas son inmutables, Python proporciona varios métodos útiles para trabajar con ellas:

mi_tupla = (1,2,3,2,4,2)

print(mi_tupla.count(2))            #Devuelve el numero de veces que aparece el elemento en la tupla

print(mi_tupla.index(2))            #Devuelve el indice de la primera aparicion de un elemento en la tupla. Ee puede especificar el inicio y fin. 
print(mi_tupla.index(2, 2))   
print(mi_tupla.index(2, 2, 4)) 

print(len(mi_tupla))               ##Devuelve la longitud de la tupla, aunque no es un método de tupla propiamente dicho.