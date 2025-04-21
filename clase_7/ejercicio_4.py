"""
4. Crear un programa de inventarios usando funciones y procedimientos, el programa debe de ser capaz, de agregar productos, agregar cantidades,
eliminar productos y mostrar el inventario completo
"""

# Diccionario del inventario
inventario = {}

# Funciones
# Agregar producto
def agregar_producto(nombre, cantidad):
    if nombre in inventario:
        print(f"El producto '{nombre}' ya existe.")
    else:
        inventario[nombre] = cantidad
        print(f"Producto '{nombre}' agregado con {cantidad} unidades.")

# Agregar cantidad
def agregar_cantidad(nombre, cantidad):
    if nombre in inventario:
        inventario[nombre] += cantidad
        print(f"Se agregaron {cantidad} unidades al producto '{nombre}'.")
    else:
        print(f"El producto '{nombre}' no existe.")

# Eliminar
def eliminar_producto(nombre):
    if nombre in inventario:
        del inventario[nombre]
        print(f"Producto '{nombre}' eliminado del inventario.")
    else:
        print(f"El producto '{nombre}' no existe en el inventario.")

# Inventario
def mostrar_inventario():
    if not inventario:
        print("El inventario está vacío.")
    else:
        print("Inventario actual:")
        for producto, cantidad in inventario.items():
            print(f"- {producto}: {cantidad} unidades")

# Menú
def menu():
    while True:
        print("\n--- MENÚ DE INVENTARIO ---")
        print("1. Agregar producto")
        print("2. Agregar cantidad a producto")
        print("3. Eliminar producto")
        print("4. Mostrar inventario")
        print("5. Salir")

        opcion = input("Seleccione una opción (1-5): ")

        match opcion:
            case '1':
                nombre = input("Nombre del producto: ")
                cantidad = int(input("Cantidad: "))
                agregar_producto(nombre, cantidad)
            case '2':
                nombre = input("Nombre del producto: ")
                cantidad = int(input("Cantidad a agregar: "))
                agregar_cantidad(nombre, cantidad)
            case '3':
                nombre = input("Nombre del producto a eliminar: ")
                eliminar_producto(nombre)
            case '4':
                mostrar_inventario()
            case '5':
                print("Saliendo del programa...")
                break
            case _:
                print("Opción no válida. Intente de nuevo.")

menu()
