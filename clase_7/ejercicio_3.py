"""
3. Crear una función que reciba una cadena de texto y me devuelva la cantidad de vocales que contiene
"""

def cantidad_vocales(texto):
    vocales = ("aeiou")
    cantidad = 0
    for i in texto.lower():
        if i in vocales:
            cantidad +=1
    return cantidad

texto = input("Ingrese el texto del cual desea identificar la cantidad de vocales: ")
total_vocales = cantidad_vocales(texto)
print(f"La cantidad total de vocales de su texto es: {total_vocales}")


