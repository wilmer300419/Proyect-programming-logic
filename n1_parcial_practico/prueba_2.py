"""
Realizar una simulación de un cajero automático en donde el 
usuario ingresa la cantidad a retirar y en donde se debe validar: Que solo se pueda 
retirar múltiplos de 10, que el monto no supere la cuenta y 
que el sistema entregue la menor cantidad de billetes posibles.
"""
cantidad_retiro = int(input("Ingrese la cantidad de retiro: "))
cuenta_saldo = 400
billetes = [100,50,20,10]
if(cantidad_retiro%10!=0):
    print("La cantidad a retirar no es multiplo de 10")
elif(cantidad_retiro>cuenta_saldo):
    print(f"La cantidad de retiro es mayor al saldo de la cuenta que es {cuenta_saldo}")
else:
    for billete in billetes:
        cantidad = cantidad_retiro//billete
        if cantidad_retiro>0:
            print(f"{cantidad} billete(s) de {billete}")
            cantidad_retiro%=billete
            print("Retiro exitoso")