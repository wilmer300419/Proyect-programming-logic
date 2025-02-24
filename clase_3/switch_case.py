opcion = int(input("Ingrese un # del 1 al 3: "))
match opcion:
    case 1:
        print("Eligio op 1")
    case 2:
        print("Eligio op 2")
    case 3:
        print("Eligio op 3")
    case _:
        print("Opción no válida")