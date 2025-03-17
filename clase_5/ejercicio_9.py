"""
9. Crear un programa que pida al usuario, una frase, el programa debera mostrarme cuantas vocales tiene.

"""
frase = input("Ingrese una frase: ")

# Definir las vocales
vocales = "aeiouAEIOU"

# Contador de vocales
contador = 0

# Recorrer la frase y contar vocales
for letra in frase:
    if letra in vocales:
        contador += 1

# Mostrar el resultado
print(f"La frase tiene {contador} vocal(es).")