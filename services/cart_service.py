from datetime import datetime

def agregar_producto_carrito(usuario_id, producto_id, cantidad, carrito, todos_carritos, productos):
    """
    Agrega un producto al carrito con validaciones
    
    
    """
    # Validar que el producto existe
    if producto_id not in productos:
        print(" Producto no encontrado.")
        return carrito, todos_carritos, False
    
    producto = productos[producto_id]
    
    # Validar stock disponible
    if producto['stock'] <= 0:
        print(" Este producto no tiene stock disponible.")
        return carrito, todos_carritos, False
    
    # Validar cantidad
    if cantidad <= 0:
        print(" La cantidad debe ser mayor a 0.")
        return carrito, todos_carritos, False
    
    # Verificar cantidad en carrito
    cantidad_en_carrito = 0
    for item in carrito:
        if item["producto_id"] == producto_id:
            cantidad_en_carrito = item["cantidad"]
            break
    
    cantidad_total = cantidad_en_carrito + cantidad
    
    # Validar stock suficiente
    if cantidad_total > producto['stock']:
        print(f" Stock insuficiente. Disponible: {producto['stock']}, en carrito: {cantidad_en_carrito}")
        return carrito, todos_carritos, False
    
    # Agregar o actualizar en carrito
    producto_existe = False
    for item in carrito:
        if item["producto_id"] == producto_id:
            item["cantidad"] += cantidad
            producto_existe = True
            break
    
    # Si no existe, agregarlo como nuevo item
    if not producto_existe:
        nuevo_item = {
            "usuario_id": usuario_id,
            "producto_id": producto_id,
            "cantidad": cantidad,
            "fecha_agregado": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
        carrito.append(nuevo_item)
        todos_carritos.append(nuevo_item)
    else:
        # Actualizar en todos_carritos también
        for item in todos_carritos:
            if item["usuario_id"] == usuario_id and item["producto_id"] == producto_id:
                item["cantidad"] += cantidad
                break
    
    # Mostrar confirmación
    print("\n" + "="*50)
    print("   ✓ PRODUCTO AGREGADO AL CARRITO")
    print("="*50)
    print(f"Producto: {producto['nombre']}")
    print(f"Cantidad: {cantidad}")
    print(f"Precio unitario: {producto['precio']} {producto['moneda']}")
    print(f"Subtotal: {producto['precio'] * cantidad} {producto['moneda']}")
    print("="*50)
    
    return carrito, todos_carritos, True

def modificar_cantidad_producto(usuario_id, numero_producto, nueva_cantidad, carrito, todos_carritos, productos):
    """
    Modifica la cantidad de un producto en el carrito
    """
    if not carrito:
        print("\n🛒 Tu carrito está vacío")
        return carrito, todos_carritos, False
    
    if numero_producto < 1 or numero_producto > len(carrito):
        print(" Número de producto inválido.")
        return carrito, todos_carritos, False
    
    item = carrito[numero_producto - 1]
    producto = productos.get(item["producto_id"])
    
    if not producto:
        print(" Producto no disponible.")
        return carrito, todos_carritos, False
    
    # Validar nueva cantidad
    if nueva_cantidad < 0:
        print(" La cantidad no puede ser negativa.")
        return carrito, todos_carritos, False
    
    if nueva_cantidad > producto['stock']:
        print(f" Stock insuficiente. Disponible: {producto['stock']}")
        return carrito, todos_carritos, False
    
    if nueva_cantidad == 0:
        # Eliminar del carrito
        carrito.remove(item)
        # Eliminar de todos_carritos
        todos_carritos = [
            c for c in todos_carritos 
            if not (c["usuario_id"] == usuario_id and c["producto_id"] == item["producto_id"])
        ]
        print("✓ Producto eliminado del carrito.")
    else:
        # Actualizar cantidad
        item["cantidad"] = nueva_cantidad
        # Actualizar en todos_carritos
        for c in todos_carritos:
            if c["usuario_id"] == usuario_id and c["producto_id"] == item["producto_id"]:
                c["cantidad"] = nueva_cantidad
                break
        print("✓ Cantidad actualizada.")
    
    return carrito, todos_carritos, True


def vaciar_carrito_usuario(usuario_id, carrito, todos_carritos):
    """
    Elimina todos los productos del carrito del usuario
    
    """
    if not carrito:
        print("\n🛒 Tu carrito ya está vacío")
        return carrito, todos_carritos
    
    # Eliminar todos los items del usuario de todos_carritos
    todos_carritos = [c for c in todos_carritos if c["usuario_id"] != usuario_id]
    carrito = []
    print("✓ Carrito vaciado.")
    
    return carrito, todos_carritos


def calcular_total_carrito(carrito, productos):
    """
    Calcula el total del carrito
    
    """
    total = 0
    moneda = "USD"
    
    for item in carrito:
        producto = productos.get(item["producto_id"])
        if producto:
            subtotal = producto['precio'] * item['cantidad']
            total += subtotal
            moneda = producto['moneda']
    
    return total, moneda


def obtener_productos_disponibles(productos):
    """
    Filtra productos con stock > 0

    """
    return {k: v for k, v in productos.items() if v['stock'] > 0}
