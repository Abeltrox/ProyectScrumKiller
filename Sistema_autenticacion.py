import json
import csv
import os
import hashlib

# CARGAR USUARIOS FINALES
def cargar_usuarios(archivo_usuarios):
    """
    Carga los usuarios finales (compradores) desde archivo
    """
    usuarios = []
    ids_registrados = set()
    emails_registrados = set()

    try:
        with open(archivo_usuarios, "r", encoding="utf-8") as archivo:
            for linea in archivo:
                partes = linea.strip().split(",")
                
                # id, nombre, email, password_hash
                if len(partes) == 4:
                    usuario = {
                        "id": partes[0],
                        "nombre": partes[1],
                        "email": partes[2],
                        "password": partes[3]
                    }
                    
                    usuarios.append(usuario)
                    ids_registrados.add(partes[0])
                    emails_registrados.add(partes[2])

    except FileNotFoundError:
        print("  Archivo de usuarios no encontrado. Se creará uno nuevo al registrarse.")
    except Exception as e:
        print(f"Error al cargar usuarios: {e}")

    return usuarios, ids_registrados, emails_registrados


# ENCRIPTAR CONTRASEÑA CON HASH (SHA256)
def encriptar_password(password):
    """
    Encripta la contraseña usando SHA256
    Criterio: Contraseña almacenada con hash
    """
    return hashlib.sha256(password.encode()).hexdigest()


# VALIDAR EMAIL
def validar_email(email):
    """
    Valida formato básico de email
    """
    if "@" not in email or "." not in email:
        return False
    
    # Validar que tiene texto antes y después del @
    partes = email.split("@")
    if len(partes) != 2 or not partes[0] or not partes[1]:
        return False
    
    return True


# REGISTRAR USUARIO FINAL
def registrar_usuario(usuarios, ids_registrados, emails_registrados):
    """
    Permite a un usuario final crear una cuenta para realizar compras
    
    Criterios de aceptación:
    - Se solicita nombre, email y contraseña
    - Validación de email único
    - Contraseña almacenada con hash
    - Registro exitoso confirmado
    """
    print("\n" + "="*50)
    print("        REGISTRO DE USUARIO")
    print("="*50)
    
    # Generar ID automático
    if usuarios:
        ultimo_id = max([int(u["id"].replace("USR", "")) for u in usuarios if u["id"].startswith("USR")], default=0)
        id_usuario = f"USR{ultimo_id + 1:04d}"
    else:
        id_usuario = "USR0001"
    
    # SOLICITAR NOMBRE
    nombre = input("Nombre completo: ").strip()
    if not nombre:
        print(" El nombre es obligatorio.")
        return None
    
    # SOLICITAR EMAIL
    email = input("Email: ").strip()
    if not email:
        print(" El email es obligatorio.")
        return None
    
    # VALIDAR FORMATO DE EMAIL
    if not validar_email(email):
        print(" Email inválido. Debe tener formato: ejemplo@dominio.com")
        return None
    
    # VALIDAR EMAIL ÚNICO
    if email in emails_registrados:
        print(" Este email ya está registrado.")
        return None
    
    # SOLICITAR CONTRASEÑA
    password = input("Contraseña (mínimo 6 caracteres): ").strip()
    if len(password) < 6:
        print(" La contraseña debe tener al menos 6 caracteres.")
        return None
    
    password_confirm = input("Confirmar contraseña: ").strip()
    if password != password_confirm:
        print(" Las contraseñas no coinciden.")
        return None
    
    # ALMACENAR CONTRASEÑA CON HASH
    password_hash = encriptar_password(password)
    
    # Crear usuario
    usuario = {
        "id": id_usuario,
        "nombre": nombre,
        "email": email,
        "password": password_hash
    }
    
    usuarios.append(usuario)
    ids_registrados.add(id_usuario)
    emails_registrados.add(email)
    
    # CONFIRMACIÓN DE REGISTRO EXITOSO
    print("\n" + "="*50)
    print("        ✓ REGISTRO EXITOSO")
    print("="*50)
    print(f"ID: {id_usuario}")
    print(f"Nombre: {nombre}")
    print(f"Email: {email}")
    print("\nYa puede iniciar sesión para realizar compras")
    print("="*50)
    
    return usuario


# INICIAR SESIÓN
def iniciar_sesion(usuarios):
    """
    Permite a un usuario final iniciar sesión
    """
    print("\n" + "="*50)
    print("           INICIAR SESIÓN")
    print("="*50)
    
    email = input("Email: ").strip()
    password = input("Contraseña: ").strip()
    
    if not email or not password:
        print(" Email y contraseña son obligatorios.")
        return None
    
    # Encriptar password ingresada para comparar con el hash
    password_hash = encriptar_password(password)
    
    # Buscar usuario por email y validar password
    for u in usuarios:
        if u["email"] == email and u["password"] == password_hash:
            print("\n✓ Inicio de sesión exitoso")
            print(f"Bienvenido, {u['nombre']}!")
            return u
    
    print(" Email o contraseña incorrectos.")
    return None


# GUARDAR USUARIOS
def guardar_usuarios(archivo_usuarios, usuarios):
    """
    Guarda usuarios en TXT, JSON y CSV
    """
    # Guardar en TXT
    try:
        with open(archivo_usuarios, "w", encoding="utf-8") as archivo:
            for u in usuarios:
                archivo.write(f"{u['id']},{u['nombre']},{u['email']},{u['password']}\n")
        print("✓ Usuarios guardados en TXT.")
    except Exception as e:
        print(f" Error al guardar en TXT: {e}")

    # Guardar en JSON
    try:
        with open("usuarios.json", "w", encoding="utf-8") as archivo:
            json.dump(usuarios, archivo, indent=4, ensure_ascii=False)
        print("✓ Usuarios guardados en JSON.")
    except Exception as e:
        print(f" Error al guardar en JSON: {e}")

    # Guardar en CSV
    try:
        with open("usuarios.csv", "w", newline="", encoding="utf-8") as archivo:
            if usuarios:
                writer = csv.DictWriter(archivo, fieldnames=["id", "nombre", "email", "password"])
                writer.writeheader()
                writer.writerows(usuarios)
        print("✓ Usuarios guardados en CSV.")
    except Exception as e:
        print(f" Error al guardar en CSV: {e}")


# MENÚ PRINCIPAL
def menu_principal():
    """
    Menú principal para registro e inicio de sesión de usuarios finales
    """
    archivo_usuarios = "usuarios.txt"
    usuarios, ids_usuarios, emails_usuarios = cargar_usuarios(archivo_usuarios)
    
    while True:
        print("\n" + "="*50)
        print("    SISTEMA DE COMERCIO ELECTRÓNICO")
        print("="*50)
        print("1. Registrarse")
        print("2. Iniciar sesión")
        print("3. Salir")
        print("="*50)
        
        opcion = input("Seleccione una opción: ").strip()
        
        if opcion == "1":
            usuario = registrar_usuario(usuarios, ids_usuarios, emails_usuarios)
            if usuario:
                # Guardar automáticamente después del registro
                guardar_usuarios(archivo_usuarios, usuarios)
        
        elif opcion == "2":
            usuario = iniciar_sesion(usuarios)
            if usuario:
                # Retornar usuario logueado
                return usuario
        
        elif opcion == "3":
            print("\n👋 Hasta pronto!")
            break
        
        else:
            print(" Opción inválida.")
    
    return None


if __name__ == "__main__":
    usuario_logueado = menu_principal()
    
    if usuario_logueado:
        print(f"\nUsuario activo: {usuario_logueado['nombre']}")
        print(f"ID: {usuario_logueado['id']}")
        print(f"Email: {usuario_logueado['email']}")