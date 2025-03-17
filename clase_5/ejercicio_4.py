"""
4. Realizar un programa que le pida al usuario un número entero positivo y calcule la suma de todos los números

"""
num = int(input("Ingrese un número entero positivo: "))

if num > 0:
    suma = 0
    for i in range(1, num + 1):
        suma += i
    print(f"La suma de todos los números hasta {num} es: {suma}")
else:
    print("El número ingresado no es positivo.")
