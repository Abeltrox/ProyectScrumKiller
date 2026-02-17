import json
import csv
import os

# CARGAR PRODUCTOS DESDE BASE DE DATOS
def cargar_productos_bd(archivo_productos):
    """
    Obtiene la información de productos desde la base de datos (archivo)
    Criterio: La información se obtiene desde la base de datos
    """
    productos = []

    try:
        with open(archivo_productos, "r", encoding="utf-8") as archivo:
            for linea in archivo:
                partes = linea.strip().split(",")
                
                # id, nombre, descripcion, precio, moneda, stock, categoria, client_id
                if len(partes) == 8:
                    producto = {
                        "id": partes[0],
                        "nombre": partes[1],
                        "descripcion": partes[2],
                        "precio": float(partes[3]),
                        "moneda": partes[4],
                        "stock": int(partes[5]),
                        "categoria": partes[6],
                        "client_id": partes[7]
                    }
                    
                    productos.append(producto)

    except FileNotFoundError:
        print("  No hay productos disponibles en la base de datos.")
    except ValueError as e:
        print(f"Error de formato en la base de datos: {e}")
    except Exception as e:
        print(f"Error al cargar productos: {e}")

    return productos


# CARGAR INFORMACIÓN DE TIENDAS/CLIENTES
def cargar_clientes_bd(archivo_clientes):
    """
    Obtiene información de las tiendas desde la base de datos
    """
    clientes = {}

    try:
        with open(archivo_clientes, "r", encoding="utf-8") as archivo:
            for linea in archivo:
                partes = linea.strip().split(",")
                
                # id, username, email, password, nombre_negocio, telefono, direccion
                if len(partes) == 7:
                    clientes[partes[0]] = {
                        "id": partes[0],
                        "nombre_negocio": partes[4]
                    }

    except FileNotFoundError:
        print("  No hay información de tiendas.")
    except Exception as e:
        print(f"Error al cargar tiendas: {e}")

    return clientes


# FILTRAR PRODUCTOS CON STOCK DISPONIBLE
def obtener_productos_disponibles(productos):
    """
    Filtra solo productos con stock > 0
    Criterio: Solo aparecen productos con stock > 0
    """
    return [p for p in productos if p['stock'] > 0]


# MOSTRAR CATÁLOGO COMPLETO (TODAS LAS TIENDAS)
def mostrar_catalogo_completo():
    """
    Muestra la lista de productos disponibles en todas las tiendas
    
    Criterios de aceptación:
    - Se muestran nombre, precio y stock
    - Solo aparecen productos con stock > 0
    - La información se obtiene desde la base de datos
    """
    print("\n" + "="*70)
    print("           CATÁLOGO DE PRODUCTOS - TODAS LAS TIENDAS")
    print("="*70)
    
    # Obtener información desde la base de datos
    productos = cargar_productos_bd("database/productos.txt")
    clientes = cargar_clientes_bd("database/clientes.txt")
    
    # Filtrar solo productos con stock > 0
    productos_disponibles = obtener_productos_disponibles(productos)
    
    if not productos_disponibles:
        print("\n📭 No hay productos disponibles en este momento")
        return productos_disponibles
    
    print(f"\nProductos disponibles: {len(productos_disponibles)}")
    print()
    
    # Mostrar nombre, precio y stock
    print(f"{'#':<5}{'NOMBRE':<25}{'PRECIO':<15}{'STOCK':<10}{'TIENDA'}")
    print("-"*70)
    
    for i, p in enumerate(productos_disponibles, 1):
        nombre_tienda = clientes.get(p['client_id'], {}).get('nombre_negocio', 'Desconocida')
        print(
            f"{i:<5}"
            f"{p['nombre'][:24]:<25}"
            f"{p['precio']} {p['moneda']:<11}"
            f"{p['stock']:<10}"
            f"{nombre_tienda}"
        )
    
    print("-"*70)
    return productos_disponibles
