"""
Crear un programa que le pida al usuario un número entero, el cual va a determinar el tamaño del vector, debera llenar el vector con numeros enteros
una vez lleno:
1. crear un nuevo vector que contenga los números mayores a 10
2. Multiplicar por 2 los numeros impares del vector original y almcenarlos en un nuevo vector
3. Sumar los elementos del nuevo vector
4. Verificar si en el vector original hay un numero negativo 

"""



print("Ejercicio 1")
n = int(input("Ingrese el tamaño del vector: "))

vector = []
num_mayores_a_10 = []
num_mult_impares = []
sum = 0
nums_negativos = []



for i in range(n):
    vector.append(int(input(f"Ingrese un número para el vector, para la posición {i}: ")))

for num in  vector:
    if num > 10:
        num_mayores_a_10.append(num)

for num in vector:
    if num%2 !=0:
        num_mult_impares.append(num * 2)

for num in num_mult_impares:
    sum+=num

for num in vector:
    if num < 0:
        nums_negativos.append(num)

print("Vector original: ", vector)
print("Vector números mayores a 10: ", num_mayores_a_10)
print("Vector números impares multiplicado por 2: ", num_mult_impares)
print("Vector suma total: ", sum)
print("Vector numeros negativos: ", nums_negativos)





