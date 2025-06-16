# Script main.py

# Crea un profesor, un curso, varios alumnos y los inscribe en el curso.

# Ejecuta los métodos para mostrar información de forma ordenada.

from profesor import Profesor
from alumno import Alumno
from curso import Curso
from ad.a import Empleado

import random

if __name__ == "__main__":

    profesor1 = Profesor("luis", "Mates")

    alumno1 = Alumno("maria", 13)
    alumno2 = Alumno("noa", 12)
    alumno3 = Alumno("felipe", 13)


    curso1 = Curso("1º-ESO",profesor1)

    curso1.agregar_alumno(alumno1)
    curso1.agregar_alumno(alumno2)
    curso1.agregar_alumno(alumno3)

    print(profesor1.saludar())

    curso1.mostrar_alumnos()



# 📚 Proyecto 2: Sistema de Reservas de Biblioteca
# 📝 Enunciado:
# Vas a crear un sistema de reservas para una biblioteca. El objetivo es que los usuarios puedan reservar 
# libros disponibles.

# Los métodos deben usar return en lugar de print para devolver información útil. Este enfoque permite 
# reutilizar los métodos y testearlos fácilmente.

# 🎯 Requisitos:
# Clase Libro

# Atributos: titulo, autor, disponible (booleano)

# Métodos:

# reservar() → cambia el estado del libro y devuelve True o False

# estado() → devuelve "Disponible" o "Reservado"

# Clase Usuario

# Atributos: nombre, libros_reservados (lista)

# Métodos:

# reservar_libro(libro) → intenta reservar el libro y devuelve un mensaje

# obtener_resumen() → devuelve un diccionario con nombre y lista de libros reservados

# Clase Biblioteca

# Atributos: nombre, libros (lista)

# Métodos:

# agregar_libro(libro)

# buscar_libro(titulo)

# listar_libros() → devuelve una lista de tuplas con título y estado

# Script main.py

# Crea una biblioteca, agrega libros, crea un usuario y realiza algunas reservas.

# Imprime el resultado de las reservas y el resumen del usuario.




