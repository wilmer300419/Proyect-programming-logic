"""
Crear un algoritmo que le pida al usuario un número entero mayor a 1
y determine si es primo o no. El programa se deberá realizar con divisiones
sucesivas. 
"""
contador = 2
n = int(input("Ingrese un nímero entero positivo mayor a 1: "))
for i in range(n):
    if(i!=n and i!=1 and i!=0 and n % i ==0 ):
        contador+=1
if (contador == 2):
    print(f"El número {n} es primo ")
else:
    print(f"El número {n} no es primo ")