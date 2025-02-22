# Solicita al usuario que ingrese un número y lo convierte a tipo flotante
num = float(input("Ingrese un número: "))

# Verifica si el número es par o impar
if num % 2 == 0:  # Si el residuo de la división entre 2 es 0, es un número par
    print("El número ingresado es par.")
elif num < 0:  # Si el el numero es negativo es un dato erroneo
    print("Ingreso un dato erróneo")
else: 
    print("El número ingresado es impar.") 
