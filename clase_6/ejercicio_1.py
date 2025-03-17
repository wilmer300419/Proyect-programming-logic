numeros = [10, 15, 23, 42, 8, 17, 30]

max_numero = numeros[0]
for numero in numeros:
    if numero >max_numero:
        max_numero = numero

suma = 0
for numero in numeros:
    suma += numero

promedio = suma / len(numeros)

numeros_pares = []
for numero in numeros:
    if numero%2 ==0:
        numeros_pares.append(numero)

print("Número máximo: ", max_numero)
print("Promedio: ", promedio)
print("Número pares: ", numeros_pares)
