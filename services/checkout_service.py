from repositories.cart_repository import (
    cargar_carrito,
    guardar_carrito,
    cargar_productos_para_carrito
)


def procesar_checkout(archivo_carrito, archivo_productos, usuario_id):

    # 1️ Cargar carrito
    mi_carrito, todos_carritos = cargar_carrito(archivo_carrito, usuario_id)

    if not mi_carrito:
        print("\nEl carrito está vacío. No se puede continuar con el checkout.")
        return False

    # 2️ Cargar productos
    productos = cargar_productos_para_carrito(archivo_productos)

    print("\n=========== RESUMEN DE COMPRA ===========")

    total = 0

    for item in mi_carrito:
        producto_id = item["producto_id"]
        cantidad = item["cantidad"]

        if producto_id in productos:
            producto = productos[producto_id]
            precio = producto["precio"]
            subtotal = precio * cantidad
            total += subtotal

            print(
                f"Producto: {producto['nombre']} | "
                f"Cantidad: {cantidad} | "
                f"Precio: {precio} {producto['moneda']} | "
                f"Subtotal: {subtotal} {producto['moneda']}"
            )

    print("-----------------------------------------")
    print(f"TOTAL A PAGAR: {total}")
    print("=========================================")

    # 3️ Confirmación
    confirmacion = input("\n¿Desea confirmar la compra? (s/n): ")

    if confirmacion.lower() != "s":
        print("\nCompra cancelada.")
        return False

    # 4️ Eliminar items del usuario del carrito
    todos_carritos = [
        item for item in todos_carritos
        if item["usuario_id"] != usuario_id
    ]

    guardar_carrito(archivo_carrito, todos_carritos)

    print("\nCompra realizada con éxito.")
    return True
# Fin de checkout_service.py
