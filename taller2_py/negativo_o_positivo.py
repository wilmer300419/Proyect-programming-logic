# Solicita al usuario que ingrese un número y lo convierte a tipo flotante
num = float(input("Ingrese un número: "))

# Verifica si el número es positivo, negativo o cero
if num > 0:
    print("El número ingresado es positivo.")
elif num < 0:
    print("El número ingresado es negativo.")
elif num == 0:
    print("El número ingresado es 0.")
else:
    print("Ingreso un dato erróneo")
