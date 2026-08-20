productos = []


def agregar_producto():
    print("\n--- AGREGAR PRODUCTO ---")

    id_producto = int(input("ID del producto: "))
    nombre = input("Nombre: ")
    precio = float(input("Precio: "))
    stock = int(input("Stock: "))

    producto = {
        "id": id_producto,
        "nombre": nombre,
        "precio": precio,
        "stock": stock
    }

    productos.append(producto)

    print("Producto agregado correctamente.")


def listar_productos():
    print("\n--- LISTA DE PRODUCTOS ---")

    if len(productos) == 0:
        print("No hay productos registrados.")
        return

    for producto in productos:
        print(
            f"ID: {producto['id']} | "
            f"Nombre: {producto['nombre']} | "
            f"Precio: ${producto['precio']:.2f} | "
            f"Stock: {producto['stock']}"
        )


def buscar_producto():
    print("\n--- BUSCAR PRODUCTO ---")

    id_producto = int(input("Ingrese el ID: "))

    for producto in productos:
        if producto["id"] == id_producto:
            print(f"Nombre: {producto['nombre']}")
            print(f"Precio: ${producto['precio']:.2f}")
            print(f"Stock: {producto['stock']}")
            return

    print("Producto no encontrado.")


def eliminar_producto():
    print("\n--- ELIMINAR PRODUCTO ---")

    id_producto = int(input("Ingrese el ID: "))

    for producto in productos:
        if producto["id"] == id_producto:
            productos.remove(producto)
            print("Producto eliminado correctamente.")
            return

    print("Producto no encontrado.")


def menu():
    while True:
        print("\n==========================")
        print("     GESTIÓN DE TIENDA")
        print("==========================")
        print("1. Agregar producto")
        print("2. Listar productos")
        print("3. Buscar producto")
        print("4. Eliminar producto")
        print("5. Salir")
        print("==========================")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            agregar_producto()

        elif opcion == "2":
            listar_productos()

        elif opcion == "3":
            buscar_producto()

        elif opcion == "4":
            eliminar_producto()

        elif opcion == "5":
            print("Saliendo del programa...")
            break

        else:
            print("Opción inválida.")


menu()