#programa que muestra las calificaciones de los estudiantes

# Definición de la clase Estudiante
class Estudiante:
    def __init__(self, nombre, calificacion):
        self.nombre = nombre
        self.calificacion = calificacion
        # Inicializar la lista de estudiantes
        self.estudiantes = []
        # Inicializar la lista de calificaciones
        self.calificaciones = []
        
    # Método para mostrar la información del estudiante
    def mostrar_informacion(self):
        print(f"Nombre: {self.nombre}, Calificación: {self.calificacion}")
            
if __name__ == "__main__":
    # Ciclo para pedir la información de los estudiantes y almacenarla en una lista
    estudiantes = []
    for i in range(5):
        nombre = input("Ingrese el nombre del estudiante: ")
        calificacion = input("Ingrese la calificación del estudiante: ")
        estudiante = Estudiante(nombre, calificacion)
        estudiantes.append(estudiante)
        

    # Mostrar la información de cada estudiante
    for estudiante in estudiantes:
        estudiante.mostrar_informacion()
