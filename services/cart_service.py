from datetime import datetime

def agregar_producto_carrito(usuario_id, producto_id, cantidad, carrito, todos_carritos, productos):
    """
    Agrega un producto al carrito con validaciones
    
    Validaciones:
    - Producto debe existir
    - Debe haber stock suficiente
    - Cantidad debe ser válida
    
    Args:
        usuario_id: ID del usuario
        producto_id: ID del producto a agregar
        cantidad: Cantidad a agregar
        carrito: Carrito del usuario actual
        todos_carritos: Todos los carritos
        productos: Diccionario de productos disponibles
    
    Returns:
        tuple: (carrito_actualizado, todos_carritos_actualizado, exito)
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
