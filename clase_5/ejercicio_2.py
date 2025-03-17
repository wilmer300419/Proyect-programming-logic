"""
Desarrollar un programa para poder determinar si un año ingresado por teclado es bisiesto, adicional el programa debe de ejecutarse mientras el usuario lo decida 
"""
option = "s"
while(option != "n"):
    year = int(input("Ingrese el año que desea consultar: "))

    if year % 100 != 0 and year % 4 == 0 or year % 400 == 0 :
        print(f"El año {year} es bisiesto.")
    else:
        print(f"El año {year} no es bisiesto.")
        
    option = input("Ingrese si desea continuar usando el programa (s/n): ") 


