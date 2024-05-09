#Este es un programa simple en Python que saluda al usuario.
#Pide al usuario que ingrese su nombre.

nombre = input("Por favor, ingrese su nombre: ")

#Imprime un saludo personalizado.
print(f"Hola, {nombre}! Bienvenido a la programación en Phyton")

#Pedimos los datos al usuario
numero1 = input("Introduzca el primer número: ")
numero2 = input("Introduzca el segundo número: ")

#Convierte los números introducidos a enteros.
numero1 = int(numero1)
numero2 = int(numero2)

if numero1 > numero2:
    print(f"El numero 1 es mayor que el numero 2")
elif numero1 < numero2:
    print(f"El numero 1 es mayor que el numero 2")
else: 
    print(f"Los numeros son iguales")