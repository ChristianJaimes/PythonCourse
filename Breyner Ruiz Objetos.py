class persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
        self.notas = []

    def despedirse(self):
        print(f"Adios {self.nombre}")
  

    def saludar(self):
        print(f"hola {self.nombre}")

    def agregar_nota(self, nota):
        self.notas.append(nota)
        print(f"la nota {nota} fue agreganda a {self.nombre}")
    
    def mostrar_nota(self):
        if self.notas:
            print(f"nota de {self.nombre}: {', '.join(map(str, self.notas))}")
        else: 
            print(f"{self.nombre} no tiene notas")


    @staticmethod
    def estudiantes(personas):
        for persona in personas:
            print(f"{persona.nombre} tiene {persona.edad} años y tiene las siguientes notas: {persona.notas}")
        return personas
    
class estudiante(persona):
    def __init__(self, nombre, edad, carrera):
        super().__init__(nombre, edad)
        self.carrera = carrera
        
if __name__ == "__main__":

    persona1 = persona("Juan", 20)
    persona2 = persona("Pedro", 25)
    persona3 = persona("Maria", 30)
    persona4 = persona("Jose", 35)
    persona5 = persona("Luis", 40)
    personas = [persona1, persona2, persona3, persona4, persona5]
 
    for p in personas: 
        p.despedirse()
    
    persona2.saludar()
    persona1.saludar()
    persona1.agregar_nota(4.5)
    persona1.mostrar_nota()
    persona3.mostrar_nota()
