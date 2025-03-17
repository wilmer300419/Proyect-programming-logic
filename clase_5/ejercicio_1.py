"""
Hacer un programa y un diagrama de flujo que determine si el año 2025 es un año bisiesto o no 
"""

year = 2025

if year % 100 != 0 and year % 4 == 0 or year % 400 == 0 :
    print(f"El año {year} es bisiesto.")
else:
    print(f"El año {year} no es biciesto.")
    

