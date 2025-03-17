"""
Crear un programa, que me muestre por pantalla los primeros n números, de la serie fibonacci
"""


n = int(input("Ingrese la cantidad de números de la serie fibonacci: "))

a= 0
b = 1
c = 0

for i in range(n):
    print(a)
    c= a + b
    a = b
    b = c

