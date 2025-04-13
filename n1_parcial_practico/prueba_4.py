"""
Crear un programa donde el usuario ingrese un texto,
el programa deberá indicarme cuantas vocales tiene ese texto 
"""

vocales = "aeiouAEIOU"
contador_vocales = 0
texto = input("Ingrese un texto: ")

for i in texto:
    if i in vocales:
        contador_vocales +=1

print(f"La cantidad de vocales del texto es {contador_vocales}")
