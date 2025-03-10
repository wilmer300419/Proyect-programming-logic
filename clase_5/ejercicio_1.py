"""
Hacer un programa y un diagrama de flujo que determine si el año 2025 es un año bisiesto o no 

Modificar el programa para poder determinar si un año ingresado por teclado es biciesto, adicional el programa debe de ejecutarse mientras el usuario lo deicda 
"""

while(True):
    year = int(input("Ingrese el año que desea consultar: "))

    if year % 100 != 0 and year % 4 == 0 or year % 400 == 0 :
        print(f"El año {year} es bisiesto.")
    else:
        print(f"El año {year} no es biciesto.")
        
    option = input("Ingrese si desea continuar usando el programa (s/n): ") 

    if option == "n":
        break
