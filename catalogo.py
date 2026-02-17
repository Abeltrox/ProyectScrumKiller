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


# MOSTRAR CATÁLOGO POR TIENDA ESPECÍFICA
def mostrar_catalogo_por_tienda():
    """
    Muestra productos de una tienda seleccionada
    """
    print("\n" + "="*70)
    print("           SELECCIONAR TIENDA")
    print("="*70)
    
    # Obtener tiendas desde la base de datos
    clientes = cargar_clientes_bd("database/clientes.txt")
    
    if not clientes:
        print("No hay tiendas registradas.")
        return []
    
    # Mostrar lista de tiendas
    clientes_lista = list(clientes.values())
    print("\nTiendas disponibles:")
    for i, cliente in enumerate(clientes_lista, 1):
        print(f"{i}. {cliente['nombre_negocio']} (ID: {cliente['id']})")
    
    # Seleccionar tienda
    try:
        opcion = int(input("\nSeleccione una tienda (número): ").strip())
        if 1 <= opcion <= len(clientes_lista):
            client_id = clientes_lista[opcion - 1]['id']
            nombre_tienda = clientes_lista[opcion - 1]['nombre_negocio']
        else:
            print(" Opción inválida.")
            return []
    except ValueError:
        print(" Opción inválida.")
        return []
    
    # Obtener productos de esa tienda desde la base de datos
    print("\n" + "="*70)
    print(f"           CATÁLOGO - {nombre_tienda.upper()}")
    print("="*70)
    
    productos = cargar_productos_bd("database/productos.txt")
    
    # Filtrar por tienda y stock > 0
    productos_tienda = [p for p in productos if p['client_id'] == client_id and p['stock'] > 0]
    
    if not productos_tienda:
        print(f"\n📭 No hay productos disponibles en {nombre_tienda}")
        return productos_tienda
    
    print(f"\nProductos disponibles: {len(productos_tienda)}")
    print()
    
    # Mostrar nombre, precio y stock
    print(f"{'#':<5}{'NOMBRE':<30}{'PRECIO':<15}{'STOCK'}")
    print("-"*70)
    
    for i, p in enumerate(productos_tienda, 1):
        print(
            f"{i:<5}"
            f"{p['nombre'][:29]:<30}"
            f"{p['precio']} {p['moneda']:<11}"
            f"{p['stock']}"
        )
    
    print("-"*70)
    return productos_tienda


# VER DETALLES DE UN PRODUCTO
def ver_detalles_producto(productos_disponibles):
    """
    Muestra información detallada de un producto seleccionado
    """
    if not productos_disponibles:
        print("No hay productos disponibles para ver detalles.")
        return None
    
    print("\n" + "="*50)
    print("         VER DETALLES DEL PRODUCTO")
    print("="*50)
    
    try:
        numero = int(input("Ingrese el número del producto: ").strip())
        
        if 1 <= numero <= len(productos_disponibles):
            producto = productos_disponibles[numero - 1]
            
            print("\n" + "="*50)
            print(f"📦 {producto['nombre']}")
            print("="*50)
            print(f"ID: {producto['id']}")
            print(f"Descripción: {producto['descripcion']}")
            print(f"Precio: {producto['precio']} {producto['moneda']}")
            print(f"Stock disponible: {producto['stock']} unidades")
            print(f"Categoría: {producto['categoria']}")
            print("="*50)
            
            return producto
        else:
            print(" Número de producto inválido.")
            return None
            
    except ValueError:
        print(" Entrada inválida.")
        return None


# BUSCAR PRODUCTOS
def buscar_productos():
    """
    Permite buscar productos por nombre
    """
    print("\n" + "="*50)
    print("         BUSCAR PRODUCTOS")
    print("="*50)
    
    termino = input("Ingrese el nombre del producto: ").strip().lower()
    
    if not termino:
        print(" Debe ingresar un término de búsqueda.")
        return []
    
    # Obtener productos desde la base de datos
    productos = cargar_productos_bd("database/productos.txt")
    clientes = cargar_clientes_bd("database/clientes.txt")
    
    # Filtrar por nombre y stock > 0
    resultados = [
        p for p in productos 
        if termino in p['nombre'].lower() and p['stock'] > 0
    ]
    
    if not resultados:
        print(f"\n🔍 No se encontraron productos disponibles con: '{termino}'")
        return []
    
    print(f"\n🔍 Se encontraron {len(resultados)} producto(s) disponible(s):")
    print()
    print(f"{'#':<5}{'NOMBRE':<25}{'PRECIO':<15}{'STOCK':<10}{'TIENDA'}")
    print("-"*70)
    
    for i, p in enumerate(resultados, 1):
        nombre_tienda = clientes.get(p['client_id'], {}).get('nombre_negocio', 'Desconocida')
        print(
            f"{i:<5}"
            f"{p['nombre'][:24]:<25}"
            f"{p['precio']} {p['moneda']:<11}"
            f"{p['stock']:<10}"
            f"{nombre_tienda}"
        )
    
    print("-"*70)
    return resultados


# MENÚ DE CATÁLOGO
def menu_catalogo():
    """
    Menú principal para visualizar el catálogo de productos
    Permite iniciar el proceso de compra
    """
    productos_actuales = []
    
    while True:
        print("\n" + "="*50)
        print("         CATÁLOGO DE PRODUCTOS")
        print("="*50)
        print("1. Ver catálogo completo (todas las tiendas)")
        print("2. Ver catálogo por tienda")
        print("3. Buscar productos")
        print("4. Ver detalles de un producto")
        print("5. Volver")
        print("="*50)
        
        opcion = input("Seleccione una opción: ").strip()
        
        if opcion == "1":
            productos_actuales = mostrar_catalogo_completo()
        
        elif opcion == "2":
            productos_actuales = mostrar_catalogo_por_tienda()
        
        elif opcion == "3":
            productos_actuales = buscar_productos()
        
        elif opcion == "4":
            if productos_actuales:
                ver_detalles_producto(productos_actuales)
            else:
                print(" Primero debe ver el catálogo (opción 1, 2 o 3).")
        
        elif opcion == "5":
            print("Volviendo al menú principal...")
            break
        
        else:
            print(" Opción inválida.")


if __name__ == "__main__":
    # Crear directorios si no existen
    if not os.path.exists("database"):
        os.makedirs("database")
    
    menu_catalogo()