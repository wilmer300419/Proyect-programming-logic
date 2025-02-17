# Diseña un algoritmo que solicite una calificación (0 a 100) y determine si el estudiante
# ha aprobado o reprobado. Un puntaje de 60 o más es aprobado.
# Ejemplo de salida: "Aprobado" o "Reprobado."

num = int("Ingrese su nota: ")
if num < 0 or num >100:
    print("El numero debe ser entre 0 y 100")
elif num >= 60:
    print("Aprobaste")
else:
    print("Reprobaste")


