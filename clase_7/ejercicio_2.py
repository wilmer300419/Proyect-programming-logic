"""
2. Crear una función que reciba un numero entero y le indique si es par o impar

"""

def par_impar(num):
    if num%2 == 0:
        return "El número es par"
    return "El número es impar"
n = int(input("Ingrese un número para identificar si es par o impar: "))
par_impar1 = par_impar(n)

print(par_impar1)


