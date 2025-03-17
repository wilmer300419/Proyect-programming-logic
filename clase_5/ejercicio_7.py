"""
7. Crear un programa que pida al usuario dos numeros, uno para el inicio y el otro para el final, el programa debera determinar dentro de ese rango cuales son los números pares
y mostrarlos por pantalla

"""
inicio = int(input("Ingrese el número de inicio: "))
fin = int(input("Ingrese el número final: "))

# Verificar que el inicio sea menor que el final
if inicio <= fin:
    print(f"\nNúmeros pares en el rango de {inicio} a {fin}:\n")
    for num in range(inicio, fin + 1):
        if num % 2 == 0:
            print(num)
else:
    print("El número de inicio debe ser menor o igual al número final.")


