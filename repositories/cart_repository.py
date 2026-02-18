def cargar_carrito(archivo_carrito, usuario_id):
    """
    Carga el carrito de compras del usuario desde la base de datos
    
   
    """
    carritos = []
    
    try:
        with open(archivo_carrito, "r", encoding="utf-8") as archivo:
            for linea in archivo:
                partes = linea.strip().split(",")
                
                # usuario_id, producto_id, cantidad, fecha_agregado
                if len(partes) == 4:
                    carritos.append({
                        "usuario_id": partes[0],
                        "producto_id": partes[1],
                        "cantidad": int(partes[2]),
                        "fecha_agregado": partes[3]
                    })
    
    except FileNotFoundError:
        # Archivo no existe aún, retornar listas vacías
        pass
    except Exception as e:
        print(f"Error al cargar carrito: {e}")
    
    # Filtrar solo items del usuario actual
    mi_carrito = [item for item in carritos if item["usuario_id"] == usuario_id]
    return mi_carrito, carritos

def guardar_carrito(archivo_carrito, todos_carritos):
    """
    Guarda todos los carritos en la base de datos

    """
    try:
        with open(archivo_carrito, "w", encoding="utf-8") as archivo:
            for item in todos_carritos:
                archivo.write(
                    f"{item['usuario_id']},{item['producto_id']},"
                    f"{item['cantidad']},{item['fecha_agregado']}\n"
                )
        print("✓ Carrito guardado.")
    except Exception as e:
        print(f" Error al guardar carrito: {e}")


def cargar_productos_para_carrito(archivo_productos):
    """
    Carga productos como diccionario para acceso rápido por ID
    """
    productos = {}

    try:
        with open(archivo_productos, "r", encoding="utf-8") as archivo:
            for linea in archivo:
                partes = linea.strip().split(",")
                
                if len(partes) == 8:
                    productos[partes[0]] = {
                        "id": partes[0],
                        "nombre": partes[1],
                        "descripcion": partes[2],
                        "precio": float(partes[3]),
                        "moneda": partes[4],
                        "stock": int(partes[5]),
                        "categoria": partes[6],
                        "client_id": partes[7]
                    }

    except FileNotFoundError:
        print("  No hay productos disponibles.")
    except Exception as e:
        print(f"Error al cargar productos: {e}")

    return productos
