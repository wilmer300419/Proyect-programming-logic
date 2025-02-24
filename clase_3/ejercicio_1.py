# Realizar un programa que tenga tres opciones
# opcioa a  sumar
# opcioa b dividir
# opcioa c salir
num1 = float(input("Ingrese un número: "))
num2 = float(input("Ingrese otro número: "))

print("""
Menú
    a. Sumar
    b. dividir
    c. salir
""")
opcion =input("Ingrese la opcion del menú: ")
solucion = 0.0
match opcion:
    case "a":
        solucion = num1 + num2
        print("Resultado de la suma: ", solucion)
    
    case "b":
        solucion = num1 / num2
        print("Resultado de la división: ", solucion)
    
    case "c":
        print("salio del programa.")
    case _:
        print("Ingreso una opción invalida del menú del programa.")

