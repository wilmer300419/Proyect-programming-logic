"""
8. Crear un programa que me genere un numero aleatorio entre uno y cien, el programa debe de pedirle al usuario, que ingrese un número, indicar si el numero ingresado es mayor o igual al
número aleatorio generado, hasta que lo adivine

"""
import random

# Generar un número aleatorio entre 1 y 100
numero_secreto = random.randint(1, 100)

print("¡Adivina el número secreto entre 1 y 100!")

# Bucle hasta que el usuario adivine el número
while True:
    intento = int(input("Ingresa tu número: "))
    
    if intento > numero_secreto:
        print("El número es menor. Intenta de nuevo.")
    elif intento < numero_secreto:
        print("El número es mayor. Intenta de nuevo.")
    else:
        print(f"¡Felicidades! Adivinaste el número {numero_secreto}.")
        break  # Termina el bucle cuando acierta