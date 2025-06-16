class Profesor:
    def __init__(self, nombre, materia):
        self.nombre = nombre
        self.materia = materia

    def saludar(self):
        return f"hola, mi nombre es {self.nombre} y soy el nuevo profesor"

    def __str__(self):
        return f"{self.nombre}"
    

profesor1 = Profesor("luis", "Mates")
print(profesor1)