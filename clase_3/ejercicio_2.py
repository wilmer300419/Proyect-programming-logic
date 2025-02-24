print("El programa constara del funcionamiento de un proyecto orientado al uso interactivo de un cajero automatico.")

saldo = 5000.0
variable_de_operaciones = 0.0
resultado = 0.0

while(True):
    print("""
        Bienvenido al Cajero Automático  
        Seleccione una opción:  
            1. Consultar saldo  
            2. Depositar dinero  
            3. Retirar dinero con tarjeta  
            4. Retirar dinero con tu cuenta movil
            5. trasferencias de dinero  
            6. Pago dinero  
            7. Salir  
        """) 
    opcion = int(input("Ingrese una de las opciones del menu: "))
    match opcion: 
        case 1:
            print(f"Su saldo actual es: ${saldo}")
        # case 2:
            