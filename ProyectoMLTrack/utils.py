# utils.py
import json
import os

def cargar_datos(nombre_archivo):
    if not os.path.exists(nombre_archivo):
        return []
    with open(nombre_archivo, "r", encoding="utf-8") as f:
        return json.load(f)

def guardar_datos(nombre_archivo, datos):
    with open(nombre_archivo, "w", encoding="utf-8") as f:
        json.dump(datos, f, indent=4)

def cargar_usuarios():
    return cargar_datos("usuarios.json")

def guardar_usuarios(usuarios):
    guardar_datos("usuarios.json", usuarios)

def cargar_productos():
    return cargar_datos("productos.json")

def guardar_productos(productos):
    guardar_datos("productos.json", productos)

def cargar_pedidos():
    return cargar_datos("pedidos.json")

def guardar_pedidos(pedidos):
    guardar_datos("pedidos.json", pedidos)