"""
6. Pedir al usuario un número entero positivo, este programa me debe indicar cuantos dígitos tiene el número ingresado

"""
num = int(input("Ingrese un número entero positivo: "))

# Verificar que sea positivo
if num > 0:
    # Contar los dígitos usando un ciclo while
    contador = 0
    temp = num
    while temp > 0:
        temp //= 10  # Eliminar el último dígito
        contador += 1
    
    print(f"El número {num} tiene {contador} dígitos.")
else:
    print("Debe ingresar un número entero positivo.")