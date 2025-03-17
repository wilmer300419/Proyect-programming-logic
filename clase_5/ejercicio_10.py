"""
10. Crear un programa que pida al usuario, dos números enteros positivos y calcular el resultado de su multiplicación, 
pero usando solo sumas repetitivas 

"""
# Solicitar dos números enteros positivos al usuario
num1 = int(input("Ingrese el primer número entero positivo: "))
num2 = int(input("Ingrese el segundo número entero positivo: "))

# Verificar que ambos números sean positivos
if num1 > 0 and num2 > 0:
    resultado = 0
    
    # Realizar la multiplicación con sumas repetitivas
    for i in range(num2):
        resultado += num1  # Sumar num1 repetidamente

    # Mostrar el resultado
    print(f"{num1} x {num2} = {resultado}")
else:
    print("Ambos números deben ser enteros positivos.")

