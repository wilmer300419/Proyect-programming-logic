"""
Crear un programa, que me muestre por pantalla los primeros n números, de la serie fibonacci
"""

# # Función con recursiva
# def fibonacci(n, a=0, b=1):
#     while n!=0:
#         print(a)
#         return fibonacci(n-1, b, a + b)
#     return a

# # Función con ciclo for
# def fibonacci_1(n):
#     a= 0
#     b = 1
#     c = 0

#     for i in range(n):
#         print(a)
#         c= a + b
#         a = b
#         b = c


# n = int(input("Ingrese la cantidad de numeros de la serie fibonacci: "))

# print("Función recursiva")
# fibonacci(n)

# print("Función por ciclo for: ")
# fibonacci_1(n)

n = int(input("Ingrese la cantidad de numeros de la serie fibonacci: "))

a= 0
b = 1
c = 0

for i in range(n):
    print(a)
    c= a + b
    a = b
    b = c

