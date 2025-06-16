
# Clase Curso

# Atributos: nombre, profesor, alumnos (lista)

# Métodos:

# agregar_alumno(alumno) → añade un alumno y le asigna el profesor del curso

# mostrar_alumnos() → muestra todos los alumnos del curso


class Curso:
    def __init__(self, nombre, profesor):
        self.nombre = nombre
        self.profesor = profesor
        self.alumnos = []
    
    def agregar_alumno(self, alumno):
        self.alumnos.append(alumno)
        alumno.profesor = self.profesor

    def mostrar_alumnos(self):
        print("alumnos inscritos: ")
        for alumno in self.alumnos:
            print(f"- {alumno.presentacion()}")

