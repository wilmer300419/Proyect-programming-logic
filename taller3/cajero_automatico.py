import time as t

print("El programa constara del funcionamiento de un proyecto orientado al uso interactivo de un cajero automatico.\n")

saldo_tarjeta_1 = 5000.0
saldo_tarjeta_2 = 7000.0
variable_de_operaciones = 0.0
resultado = 0.0
tarjeta_1 = 403100200
tarjeta_2 = 403000001
clave_1 = 12345
clave_2 = 67890
num_tel_tarjeta_1 = 3123456789
num = 0


while(True):
    t.sleep(2)
    print("""Bienvenido al Cajero Automático  
    Seleccione una opción:  
        1. Consultar saldo  
        2. Depositar dinero  
        3. Retirar dinero con tarjeta  
        4. Retirar dinero con tu cuenta movil
        5. Salir  
        """) 
    
    opcion = int(input("Ingrese una de las opciones del menu: "))
 
    match opcion: 
        case 1:
            num = int(input("Ingrese el numero de la tarjeta que desea consultar el saldo: \n"))
            if num == tarjeta_1:

                for i in range(3,0,-1):

                    clave = int(input("Ingrese la clave de su tarjeta: \n"))                

                    if clave_1 == clave:
                        print(f"Su saldo actual es: ${saldo_tarjeta_1}\n")
                        break
                    else:
                        print(f"La clave es incorrecta le quedan {i-1} intentos.\n")

            elif num == tarjeta_2:

                for i in range(3,0,-1):

                    clave = int(input("Ingrese la clave de su tarjeta: \n"))                

                    if clave_2 == clave:
                        print(f"Su saldo actual es: ${saldo_tarjeta_2}\n")
                        break

                    else:
                        print(f"La clave es incorrecta le quedan {i-1} intentos.\n")

            else:
                print("Ingreso una tarjeta invalida\n")
                
        case 2:
  
            cantidad = float(input("Ingrese la cantidad de dinero que desea deposita: \n"))
            num = int(input("Ingrese el numero de la tarjeta que desea depositar: \n"))
            
            if cantidad > 1000000:
                print("La cantidad de deposito no puede ser mayor a $1.000.000")
            elif cantidad >= 10:
                if num == tarjeta_1:
    
                    for i in range(3,0,-1):

                        clave = int(input("Ingrese la clave de su tarjeta: \n"))                

                        if clave_1 == clave:
                            saldo_tarjeta_1 +=cantidad
                            print("¡El deposito a sido exitoso!\n")
                            break
    
                        else:
                            print(f"La clave es incorrecta le quedan {i-1} intentos.\n")
    
                elif num == tarjeta_2:
    
                    for i in range(3,0,-1):
    
                        clave = int(input("Ingrese la clave de su tarjeta: \n"))                
    
                        if clave_2 == clave:
                            saldo_tarjeta_2 += cantidad
                            print("¡El deposito a sido exitoso!\n")
                            break
    
                        else:
                            print(f"La clave es incorrecta le quedan {i-1} intentos.\n")
        
                else:
                    print("Ingreso una tarjeta invalida\n")
            else:
                print("La cantidad no puede ser menor a $10...\n")
        
        case 3:
            cantidad = float(input("Ingrese la cantidad de dinero que desea retirar de su tarjeta: \n"))
            num = int(input("Ingrese el numero de la tarjeta a la que desea retirar: \n"))

            if cantidad > 100000:
                print("La cantidad de retiro no puede ser mayor a $100.000")
            elif cantidad >= 10:
                if num == tarjeta_1:
    
                    for i in range(3,0,-1):

                        clave = int(input("Ingrese la clave de su tarjeta: \n"))                

                        if clave_1 == clave:
                            if saldo_tarjeta_1 < cantidad:
                                print(f"El retiro no pudo ser exitoso, ya que usted solo posee ${saldo_tarjeta_1}")
                                break
                            else: 
                                print("¡El retiro fue exitoso!")
                                saldo_tarjeta_1 -= cantidad
                                break
    
                        else:
                            print(f"La clave es incorrecta le quedan {i-1} intentos.\n")
    
                elif num == tarjeta_2:
    
                    for i in range(3,0,-1):
    
                        clave = int(input("Ingrese la clave de su tarjeta: \n"))                
    
                        if clave_2 == clave:
                            if saldo_tarjeta_2 < cantidad:
                                print(f"El retiro no pudo ser exitoso, ya que usted solo posee ${saldo_tarjeta_1}")
                                break
                            else: 
                                saldo_tarjeta_2 -= cantidad
                                print("¡El retiro fue exitoso!")
                                break
    
                        else:
                            print(f"La clave es incorrecta le quedan {i-1} intentos.\n")
        
                else:
                    print("Ingreso una tarjeta invalida\n")
            else:
                print("La cantidad no puede ser menor a $10...\n")
            
        case 4:
            cantidad = float(input("Ingrese la cantidad de dinero que desea retirar: \n"))
            num = int(input("Ingrese el numero de telefono al que le desea retirar: \n"))

            if cantidad > 100000:
                print("La cantidad de retiro no puede ser mayor a $100.000")
            elif cantidad >= 10:
                if num == num_tel_tarjeta_1:
    
                    for i in range(3,0,-1):

                        clave = int(input("Ingrese la clave de su numero o tarjeta: \n"))                

                        if clave_1 == clave:
                            if saldo_tarjeta_1 < cantidad:
                                print(f"El retiro no pudo ser exitoso, ya que usted solo posee ${saldo_tarjeta_1}")
                                break
                            else: 
                                print("¡El retiro fue exitoso!")
                                saldo_tarjeta_1 -= cantidad
                                break
    
                        else:
                            print(f"La clave es incorrecta le quedan {i-1} intentos.\n")
    
                else:
                    print("Ingreso un numero de telefono invalido\n")
            else:
                print("La cantidad no puede ser menor a $10...\n")    
            
        case 5:
            print("Usted decidio salir del programa.\n")
            break
        
        case _:
            print("Ingreso un opcion invalida, vuelva a intentarlo.\n")