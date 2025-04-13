"""
Crear un  programa que reciba un número 
entero positivo y lo invierta
"""
n = input("Ingrese el número que quiere inversar: ")

n_reverso = ""
contador = 0

for i in n:
    n_reverso+= n[-1-contador]
    contador+=1

print(f"El número inverso es {n_reverso}")