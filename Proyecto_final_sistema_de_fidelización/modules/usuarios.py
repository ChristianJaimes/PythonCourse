import hashlib
from datetime import datetime
from typing import Dict, List, Optional
from modules.utils import (
    cargar_archivo_json,
    guardar_archivo_json,
    validar_email,
    mostrar_mensaje,
)

ARCHIVO_USUARIOS = "data/usuarios.json"

class Usuario:
    """Clase que representa a un usuario del sistema"""
    
    def __init__(self, usuario: str, correo: str, contrasena: str):
        self.usuario = usuario
        self.correo = correo
        self.contrasena = self.encriptar_contrasena(contrasena)
        self.puntos = 0
        self.descuento_activo = False
        self.fecha_registro = datetime.now().strftime("%Y-%m-%d")
    
    @staticmethod
    def encriptar_contrasena(contrasena: str) -> str:
        """Encripta una contraseña usando SHA-256"""
        return hashlib.sha256(contrasena.encode('utf-8')).hexdigest()
    
    def to_dict(self) -> Dict:
        """Convierte el objeto usuario a diccionario"""
        return {
            "correo": self.correo,
            "contrasena": self.contrasena,
            "puntos": self.puntos,
            "descuento_activo": self.descuento_activo,
            "fecha_registro": self.fecha_registro
        }

def cargar_usuarios() -> Dict:
    """Carga los usuarios desde el archivo JSON"""
    return cargar_archivo_json(ARCHIVO_USUARIOS, {})

def guardar_usuarios(usuarios: Dict) -> bool:
    """Guarda los usuarios en el archivo JSON"""
    return guardar_archivo_json(ARCHIVO_USUARIOS, usuarios)

def registrar_usuario_con_correo(usuarios: Dict) -> bool:
    """Registra un nuevo usuario con validación de datos"""
    print("\n=== REGISTRO DE USUARIO ===")
    
    usuario = input("Nombre de usuario: ").strip()
    if not usuario:
        mostrar_mensaje("Error: El nombre de usuario no puede estar vacío", "error")
        return False
    
    if usuario in usuarios:
        mostrar_mensaje("Error: Este usuario ya existe", "error")
        return False
    
    correo = input("Email: ").strip()
    if not validar_email(correo):
        mostrar_mensaje("Error: Email no válido", "error")
        return False
    
    contrasena = input("Contraseña (mínimo 6 caracteres): ").strip()
    if len(contrasena) < 6:
        mostrar_mensaje("Error: La contraseña debe tener al menos 6 caracteres", "error")
        return False
    
    nuevo_usuario = Usuario(usuario, correo, contrasena)
    usuarios[usuario] = nuevo_usuario.to_dict()
    
    if guardar_usuarios(usuarios):
        mostrar_mensaje("Registro exitoso. ¡Bienvenido!", "exito")
        return True
    
    mostrar_mensaje("Error: No se pudo guardar el usuario", "error")
    return False

def iniciar_sesion(usuarios: Dict) -> Optional[str]:
    """Autentica a un usuario existente"""
    print("\n=== INICIO DE SESIÓN ===")
    
    usuario = input("Usuario: ").strip()
    contrasena = input("Contraseña: ").strip()
    
    if usuario in usuarios:
        contrasena_encriptada = Usuario.encriptar_contrasena(contrasena)
        if usuarios[usuario]["contrasena"] == contrasena_encriptada:
            mostrar_mensaje(f"Bienvenido, {usuario}!", "exito")
            return usuario
    
    mostrar_mensaje("Error: Credenciales incorrectas", "error")
    return None

def menu_usuario(usuario: str, usuarios: Dict, productos: List, premios: Dict):
    """Menú principal para usuarios registrados"""
    while True:
        
        print(f"\n=== MENÚ USUARIO ({usuario}) ===")
        print(f"Puntos actuales: {usuarios[usuario]['puntos']}")
        if usuarios[usuario].get('descuento_activo', False):
            print("¡Tienes un descuento del 10% disponible para tu próxima compra!")
        
        print("\n1. Comprar producto")
        print("2. Canjear puntos")
        print("3. Ver historial")
        print("4. Cerrar sesión")
        
        opcion = input("\nSeleccione una opción: ").strip()
        
        if opcion == "1":
            from .productos import mostrar_menu_compra
            if mostrar_menu_compra(usuario, usuarios, productos):
                guardar_usuarios(usuarios)  # Guardar después de la compra
                
        elif opcion == "2":
            from .productos import mostrar_menu_canje
            if mostrar_menu_canje(usuario, usuarios, premios):
                guardar_usuarios(usuarios)  # Guardar después del canje
                
        elif opcion == "3":
            print("\n=== HISTORIAL ===")
            print(f"Usuario: {usuario}")
            print(f"Puntos acumulados: {usuarios[usuario]['puntos']}")
            print(f"Fecha de registro: {usuarios[usuario]['fecha_registro']}")
            print(f"Descuento activo: {'Sí' if usuarios[usuario].get('descuento_activo', False) else 'No'}")
            input("\nPresione Enter para continuar...")
            
        elif opcion == "4":
            mostrar_mensaje("Sesión cerrada correctamente", "info")
            break
            
        else:
            mostrar_mensaje("Opción no válida")

