import json
import csv
import os

# CARGAR PRODUCTOS
def cargar_productos(archivo_productos):
    productos = []
    ids_registrados = set()
    categorias = set()

    try:
        with open(archivo_productos, "r", encoding="utf-8") as archivo:
            for linea in archivo:
                partes = linea.strip().split(",")
                
                # id, nombre, descripcion, precio, moneda, stock, categoria
                if len(partes) == 7:
                    producto = {
                        "id": partes[0],
                        "nombre": partes[1],
                        "descripcion": partes[2],
                        "precio": float(partes[3]),
                        "moneda": partes[4],
                        "stock": int(partes[5]),
                        "categoria": partes[6]
                    }
                    
                    productos.append(producto)
                    ids_registrados.add(partes[0])
                    categorias.add(partes[6])

    except FileNotFoundError:
        print("  Archivo de productos no encontrado. Se creará uno nuevo al guardar.")
    except ValueError:
        print("Error de formato en el archivo.")
    except Exception as e:
        print(f"Error inesperado: {e}")

    return productos, ids_registrados, categorias


def buscar_producto(productos, id_buscar):
    for p in productos:
        if p["id"] == id_buscar:
            return p
    return None


# CREAR PRODUCTO (ADMIN)
def crear_producto(productos, ids_registrados):
    id_p = input("ID del producto: ").strip()

    if id_p in ids_registrados:
        print(" Ese ID ya está registrado.")
        return

    nombre = input("Nombre: ").strip()
    descripcion = input("Descripción: ").strip()
    
    try:
        precio = float(input("Precio: "))
    except ValueError:
        print(" Precio inválido.")
        return
    
    print("\nMoneda:")
    print("1. USD")
    print("2. EUR")
    print("3. COP")
    print("4. MXN")
    moneda_op = input("Seleccione (1/2/3/4): ").strip()
    
    if moneda_op == "1":
        moneda = "USD"
    elif moneda_op == "2":
        moneda = "EUR"
    elif moneda_op == "3":
        moneda = "COP"
    elif moneda_op == "4":
        moneda = "MXN"
    else:
        moneda = "USD"
    
    try:
        stock = int(input("Stock disponible: "))
    except ValueError:
        print(" Stock inválido.")
        return
    
    categoria = input("Categoría: ").strip()

    producto = {
        "id": id_p,
        "nombre": nombre,
        "descripcion": descripcion,
        "precio": precio,
        "moneda": moneda,
        "stock": stock,
        "categoria": categoria
    }

    productos.append(producto)
    ids_registrados.add(id_p)
    print("✓ Producto creado correctamente.")

# LISTAR PRODUCTOS
def listar_productos(productos):
    if not productos:
        print("No hay productos registrados.")
        return

    print(f"\n{'ID':<10}{'Nombre':<20}{'Precio':<12}{'Stock':<8}{'Estado':<15}{'Categoría'}")
    print("-" * 90)

    for p in productos:
        estado = "✅ Disponible" if p['stock'] > 0 else "❌ Agotado"
        print(
            f"{p['id']:<10}"
            f"{p['nombre']:<20}"
            f"{p['precio']} {p['moneda']:<8}"
            f"{p['stock']:<8}"
            f"{estado:<15}"
            f"{p['categoria']}"
        )

# ACTUALIZAR PRODUCTO
def actualizar_producto(productos):
    id_p = input("Ingrese el ID del producto a actualizar: ").strip()

    for p in productos:
        if p["id"] == id_p:
            p["nombre"] = input(f"Nuevo nombre [{p['nombre']}]: ").strip() or p["nombre"]
            p["descripcion"] = input(f"Nueva descripción [{p['descripcion']}]: ").strip() or p["descripcion"]
            
            try:
                nuevo_precio = input(f"Nuevo precio [{p['precio']}]: ").strip()
                if nuevo_precio:
                    p["precio"] = float(nuevo_precio)
            except ValueError:
                print("Precio no modificado.")
            
            try:
                nuevo_stock = input(f"Nuevo stock [{p['stock']}]: ").strip()
                if nuevo_stock:
                    p["stock"] = int(nuevo_stock)
            except ValueError:
                print("Stock no modificado.")
            
            p["categoria"] = input(f"Nueva categoría [{p['categoria']}]: ").strip() or p["categoria"]

            print("✓ Producto actualizado correctamente.")
            return

    print(" Producto no encontrado.")