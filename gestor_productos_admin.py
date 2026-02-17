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

# ACTUALIZAR STOCK
def actualizar_stock(productos):
    id_p = input("ID del producto: ").strip()
    
    for p in productos:
        if p["id"] == id_p:
            try:
                nuevo_stock = int(input(f"Nuevo stock [{p['stock']}]: "))
                p["stock"] = nuevo_stock
                print("✓ Stock actualizado correctamente.")
                return
            except ValueError:
                print(" Stock inválido.")
                return
    
    print(" Producto no encontrado.")


    
# ELIMINAR PRODUCTO
def eliminar_producto(productos, ids_registrados):
    id_p = input("Ingrese el ID del producto a eliminar: ").strip()

    for p in productos:
        if p["id"] == id_p:
            confirmacion = input(f"¿Está seguro de eliminar '{p['nombre']}'? (s/n): ").lower().strip()
            if confirmacion == 's':
                productos.remove(p)
                ids_registrados.remove(id_p)
                print("✓ Producto eliminado correctamente.")
            else:
                print("Operación cancelada.")
            return

    print(" No se encontró un producto con ese ID.")

    # GUARDAR PRODUCTOS
def guardar_productos(archivo_productos, productos):
    # Guardar en TXT
    try:
        with open(archivo_productos, "w", encoding="utf-8") as archivo:
            for p in productos:
                archivo.write(
                    f"{p['id']},{p['nombre']},{p['descripcion']},"
                    f"{p['precio']},{p['moneda']},{p['stock']},{p['categoria']}\n"
                )
        print("✓ Productos guardados en TXT.")
    except Exception as e:
        print(f" Error al guardar en TXT: {e}")

    # Guardar en JSON
    try:
        with open("productos.json", "w", encoding="utf-8") as archivo:
            json.dump(productos, archivo, indent=4, ensure_ascii=False)
        print("✓ Productos guardados en JSON.")
    except Exception as e:
        print(f" Error al guardar en JSON: {e}")

    # Guardar en CSV
    try:
        with open("productos.csv", "w", newline="", encoding="utf-8") as archivo:
            if productos:
                writer = csv.DictWriter(archivo, fieldnames=["id", "nombre", "descripcion", "precio", "moneda", "stock", "categoria"])
                writer.writeheader()
                writer.writerows(productos)
        print("✓ Productos guardados en CSV.")
    except Exception as e:
        print(f" Error al guardar en CSV: {e}")

# MENÚ ADMINISTRADOR DE PRODUCTOS
def menu_admin_productos():
    archivo = "productos.txt"
    productos, ids_registrados, categorias = cargar_productos(archivo)

    while True:
        print("\n" + "="*40)
        print("    ADMINISTRACIÓN DE PRODUCTOS")
        print("="*40)
        print("1. Listar productos")
        print("2. Crear producto")
        print("3. Buscar producto")
        print("4. Actualizar producto")
        print("5. Actualizar stock")
        print("6. Eliminar producto")
        print("7. Guardar cambios")
        print("8. Salir")
        print("="*40)

        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":
            listar_productos(productos)

        elif opcion == "2":
            crear_producto(productos, ids_registrados)

        elif opcion == "3":
            id_buscar = input("Ingrese el ID del producto: ").strip()
            producto = buscar_producto(productos, id_buscar)
            if producto:
                print("\n✓ Producto encontrado:")
                print(f"ID: {producto['id']}")
                print(f"Nombre: {producto['nombre']}")
                print(f"Descripción: {producto['descripcion']}")
                print(f"Precio: {producto['precio']} {producto['moneda']}")
                print(f"Stock: {producto['stock']}")
                print(f"Categoría: {producto['categoria']}")
            else:
                print(" Producto no encontrado.")

        elif opcion == "4":
            actualizar_producto(productos)

        elif opcion == "5":
            actualizar_stock(productos)

        elif opcion == "6":
            eliminar_producto(productos, ids_registrados)

        elif opcion == "7":
            guardar_productos(archivo, productos)

        elif opcion == "8":
            guardar = input("¿Desea guardar antes de salir? (s/n): ").lower().strip()
            if guardar == "s":
                guardar_productos(archivo, productos)
            print("Saliendo del administrador de productos...")
            break

        else:
            print(" Opción no válida. Intente nuevamente.")


if __name__ == "__main__":
    menu_admin_productos()
