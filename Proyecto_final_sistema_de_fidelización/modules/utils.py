import json
import os
import re
from datetime import datetime
from typing import Any, Dict, List, Optional


def cargar_archivo_json(ruta_archivo: str, valor_por_defecto: Any = None) -> Dict:
    """Carga datos desde un archivo JSON"""
    try:
        os.makedirs(os.path.dirname(ruta_archivo), exist_ok=True)
        if not os.path.exists(ruta_archivo):
            return valor_por_defecto if valor_por_defecto is not None else {}
        
        with open(ruta_archivo, 'r', encoding='utf-8') as f:
            return json.load(f)
    except (json.JSONDecodeError, FileNotFoundError):
        return valor_por_defecto if valor_por_defecto is not None else {}

def guardar_archivo_json(ruta_archivo: str, datos: Any) -> bool:
    """Guarda datos en un archivo JSON"""
    try:
        os.makedirs(os.path.dirname(ruta_archivo), exist_ok=True)
        with open(ruta_archivo, 'w', encoding='utf-8') as f:
            json.dump(datos, f, indent=4)
        return True
    except Exception as e:
        print(f"Error al guardar archivo: {e}")
        return False

def validar_email(email: str) -> bool:
    """Valida si un email tiene formato correcto"""
    patron = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(patron, email) is not None


def mostrar_mensaje(mensaje: str, tipo: str = "info"):
    """Muestra mensajes formateados según su tipo"""
    colores = {
        "error": "\033[91m",  # Rojo
        "exito": "\033[92m",  # Verde
        "info": "\033[94m",   # Azul
    }
    reset = "\033[0m"
    print(f"{colores.get(tipo, '')}{mensaje}{reset}")

def validar_entero(valor: str) -> Optional[int]:
    """Valida si un string puede convertirse a entero"""
    try:
        return int(valor)
    except ValueError:
        return None
