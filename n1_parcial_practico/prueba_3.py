"""
Crear un algoritmo, donde el usuario ingrese una contraseña. El programa deberá validar al menos 8 caracteres,
contener un número y contener una letra mayúscula.
"""
contador_caracteres = 0
contador_numeros = 0
password = input("Ingrese una contraseña: ")
contador_mayusculas = 0

numeros = "0123456789"

for i in password:
    if i in numeros:
        contador_numeros += 1
        
    if i.isupper():
        contador_mayusculas += 1
    contador_caracteres += 1
    
if (contador_numeros == 0 or contador_mayusculas == 0 or contador_caracteres <8):
    print(f"La contraseña {password} no cumple con las condiciones de: minimo 8 caracteres, minimo 1 mayuscula, minimo 1 número")
else:
    print("Contraseña válida")    