# Atributos: nombre, edad, profesor (se asignará automáticamente desde el curso)

# Método: presentarse() → devuelve una presentación con su nombre, edad y profesor

class Alumno:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
        self.profesor = None

    def presentacion (self):
        return f"Hola me llamo {self.nombre} tengo {self.edad} y mi profesor es {self.profesor}"