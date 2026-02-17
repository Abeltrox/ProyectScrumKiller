import hashlib


def encriptar_contrasena(contrasena):
    return hashlib.sha256(contrasena.encode()).hexdigest()


def verificar_contrasena(contrasena, contrasena_encriptada):
    return encriptar_contrasena(contrasena) == contrasena_encriptada
