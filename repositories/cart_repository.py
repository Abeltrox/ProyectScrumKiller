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