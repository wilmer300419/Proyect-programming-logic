# Crear un programa que permita registrar la asistencia, de un estudiante a una clase, el programa debe de hacer lo siguiente
# Solicitar el nombre del estudiante
# Preguntar cuantas clases se han dictado en el mes
# Pedir cuantas clases ha asistido el estudiante 
# Calcular el porcentaje de asistencia
# Si el porcentaje de asistencia es menor a 75% indicar que el estudiante esta en riesgo de perdida, mostrar el informe final 
# nombre, total de clases, total de clases asistidas y el porcentaje de asistencia

# Definición de variables
nombre = ""
num_clases_mes = 0
asistencia=0
cont_clases_asistidas = 0
valor = True


while valor:
    
    # Solicitud de datos
    nombre = input("Ingrese el nombre del estudiante: ")
    num_clases_mes = int(input("Ingrese el numero de clases totales del mes: "))

    # Validación clases del mes
    if num_clases_mes  <= 0:
        print("\nEl número de clases del mes no puede ser menor o igual a 0.")
    else:  
        
        # Solicitud clases asistidas
        cont_clases_asistidas = int(input(f"Ingrese la cantidad de clases a las cuales el estudiante {nombre} ha asistido: "))

        if cont_clases_asistidas > num_clases_mes:
            print("El número de clases asistidas no puede ser mayor a las clases del mes.")
        elif cont_clases_asistidas <0:
            print("\nEl número de clases asistidas no puede ser menor a 0.")
        else: 
            # Calculo de porcentaje de asistencia
            asistencia = cont_clases_asistidas * 100 // num_clases_mes

            # Mensaje de advertencia
            if asistencia < 75:
                print("\nEl porcentaje debe de ser mayor o igual al 75% para no correr riesgo de perdida.")
                print(f"¡Advertencia! el estudiante {nombre} corre el riesgo de perdida con un {asistencia}% de asistencias.")
            else:
                # Informe
                print(f"\nEl estudiante {nombre} tenía un total de {num_clases_mes} clases, de las cuales asistio { cont_clases_asistidas} veces, por lo cual su porcentaje es {asistencia}%. ")

    # Validación de menú de opciones
    while(True):
        opcion = int(input("""
¿Desea continuar usando el programa?
Menú:
    1. Si
    2. No
Ingrese: 
    """))
        match opcion:
            case 1: 
                valor = True
                break
            case 2: 
                valor = False
                break
            case _: 
                print("\nEscogio una opcion invalida.") 

print("Gracias por usar nuestro programa.")