# Solicita al usuario que ingrese el número de horas de estacionamiento
horas = int(input("Ingrese el número de horas de estacionamiento: "))
tarifa = 0,0

# Calcula la tarifa según las reglas establecidas
if horas <= 2:
    tarifa = 0  # Las primeras 2 horas son gratuitas
    print(f"La tarifa total es: ${tarifa}")
elif horas <= 5:
    tarifa = (horas - 2) * 5  # De la hora 3 a la 5 cuestan $5 cada una
    print(f"La tarifa total es: ${tarifa}")
else:
    tarifa = (3 * 5) + ((horas - 5) * 10)  # Horas adicionales cuestan $10 cada una
    print(f"La tarifa total es: ${tarifa}")

# Muestra el resultado
print(f"La tarifa total es: ${tarifa}")
