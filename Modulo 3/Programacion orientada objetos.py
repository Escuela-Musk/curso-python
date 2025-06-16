# QUE ES POO Y QUE ES UN OBJETO EN PYTHON

# POO (Programación Orientada a Objetos) es un paradigma de programación que organiza el código en torno a objetos, 
# que son instancias de clases. Cada objeto representa una entidad con estado (atributos) y comportamiento (métodos).

# Un objeto en Python es una instancia de una clase que agrupa datos y funciones que operan sobre esos datos. 
# Por ejemplo, un coche puede ser un objeto con atributos como color y marca, y métodos como acelerar() o frenar().




# COMO SE CREA UNA CLASE?¿ 

# En Python, una clase se define con la palabra clave class. Es como un plano o molde para crear objetos.
# Las clases deben empezar con mayúscula por convención (CamelCase).

class Coche:
    pass


# QUE ES INSTANCIAR UN OBJETO?¿

# Instanciar significa crear un objeto a partir de una clase. La clase define la estructura, pero no ocupa memoria hasta que se instancia.

coche1 = Coche()
coche2 = Coche()

# COMO SE AÑADEN ATRIBUTO DE INSTANCIA? CONSTRUCTOR, SELF....

# Los atributos de instancia se definen dentro de un método especial llamado __init__, que es el constructor. 
# Se ejecuta automáticamente al instanciar un objeto.
# El parámetro self representa al objeto actual.
        
class Coche:
    def __init__(self,color:str, marca:str, num_puertas:int):
        self.color = color
        self.marca = marca
        self.num_puertas = num_puertas

# COMO SE INSTANCIA UN OBJETO CON ATRIBUTOS DE INSTANCIA? COMO SE LLAMA A UN ATRIBUTO DE INSTANCIA? 
coche1 = Coche("rojo", "fiat", 5)
coche2 = Coche("verde", "citroen", 3)

print(coche2.color, coche2.marca)
print(f"tu coche es de color {coche2.color}")


# ATRIBUTOS POR DEFECTO sin opción a cambio por parte del usuario

class Coche:
    def __init__(self,color:str, marca:str, num_puertas:int):
        self.color = color
        self.marca = marca
        self.num_puertas = num_puertas
        self.num_ruedas = 8


coche3 = Coche("gris", "renault", 5)
print(coche3.num_ruedas)
coche3.num_ruedas = 99
print(coche3.num_ruedas)

# ATRIBUTOS POR DEFECTO con opción a cambio por parte del usuario
class Coche:
    def __init__(self,color:str, marca:str, num_puertas:int,num_ruedas = 4):
        self.color = color
        self.marca = marca
        self.num_puertas = num_puertas
        self.num_ruedas = num_ruedas

coche4 = Coche("azul", "mercedes", 3,56565635635)
print(coche4.num_ruedas)

# ATRIBUTOS DE CLASE. COMO SE LLAMA A UN ATRIBUTO DE CLASE? 

class Persona:
    raza = "humano"

    def __init__(self, nombre):
        self.nombre = nombre

Persona.raza
per1 = Persona("felipe")
per1.raza




# COMO SE CREA UN METODO DE INSTANCIA? COMO LLAMARLO? 

# Un método de instancia es una función definida dentro de una clase que opera sobre una instancia específica (es decir, un objeto concreto) 
# de esa clase.
# Estos métodos pueden acceder y modificar los atributos del objeto usando el parámetro self.

# Siempre reciben self como primer parámetro.

# Se llaman usando el nombre del objeto, no de la clase.

class Persona:
   
    def __init__(self, nombre,apellido,edad,nacimiento):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.nacimiento = nacimiento

    def hablar(self,mensaje):
        return mensaje
    
    def saludar(self):
        return "hola"

    def calculo_edad(self):
        edad = 2025 - self.nacimiento
        return edad
    
    def informacion(self):
        print(f"tu nombre es {self.nombre} y tu apellido es {self.apellido}, y tu edad es {self.calculo_edad()}")

    def cumpleanyos(self):
        self.edad = self.edad + 1

    def categoria_edad(self):
        categoria = ""
        if self.edad < 18:
            categoria = "niño"
        elif self.edad < 80:
            categoria = "adulto"
        else:
            categoria = "tercera edad"
        
        return categoria


per1 = Persona("felipe", "martinez", 79,2001)
per2 = Persona("Kristina", "garcia", 34,2001)

print(per1.hablar("hola como estas?¿"))
mensaje = "Estas seguro que esto funciona¿?¿?"

print(per1.hablar(mensaje))

print(per1.saludar())

per1.informacion()
per2.informacion()

print("-------------")
print(per2.edad)
per2.cumpleanyos()
print(per2.edad)

print(per1.categoria_edad())
per1.cumpleanyos()
print(per1.categoria_edad())












# Ejercicio

# 1.- CREA UNA CLASE LLAMADA PERRO, CON TRES ATRIBUTOS. INSTANCIA UN PERRO Y MUESTRA SUS ATRIBUTOS

# 2.- AÑADE A TU CLASE ANTERIOR UN METODO, UNO QUE SEA LADRAR. LLAMA AL METODO LADRAR

# 3.- Crea una clase “Persona”. Con atributos nombre y edad. Además, hay que crear un método “cumpleaños”, 
# que aumente en 1 la edad de la persona cuando se invoque sobre un objeto creado con “Persona”.

# 4.- Crea una clase llamada Cuenta que tendrá los siguientes atributos: titular (que es una persona) y 
# cantidad (puede tener decimales). El titular será obligatorio y la cantidad es opcional. 
# Construye los siguientes métodos para la clase:

# mostrar(): Muestra los datos de la cuenta.
# ingresar(cantidad): se ingresa una cantidad a la cuenta, si la cantidad introducida es negativa, no se hará nada.
# retirar(cantidad): se retira una cantidad a la cuenta. La cuenta NO puede estar en números rojos.
