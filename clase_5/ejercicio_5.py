"""
5. Hacer un programa que le pida al usuario ingresar el número de la tabla de multiplicar que quiere, la respuesta debe de mostrarse como tabla

"""


num = int(input("Ingrese el número de la tabla de multiplicar que desea ver: "))

# Mostrar la tabla de multiplicar
print(f"\nTabla de multiplicar del {num}:\n")
for i in range(1, 11):
    print(f"{num} x {i} = {num * i}")