# FUNCIONES

# Hasta ahora hemos visto muchas funciones integradas de Python. 
# En esta sección, nos centraremos en las funciones personalizadas. 
# ¿Qué es una función? Antes de comenzar a crear funciones, aprendamos qué es una función y por qué las necesitamos.

# Definiendo una función
# Una función es un bloque reutilizable de código o declaraciones de programación diseñadas 
# para realizar una determinada tarea. Para definir o declarar una función, 
# Python proporciona la palabra clave def . La siguiente es la sintaxis para definir una función. 
# El bloque de funciones de código se ejecuta solo si se llama o invoca la función.




# Declarar y llamar a una función
# Cuando creamos una función, lo llamamos declarar una función. 
# Cuando comenzamos a usarlo, lo llamamos llamar o invocar una función. 
# La función se puede declarar con o sin parámetros.

# SINTASIS

def nombre_funcion():
    #cuerpo de la función
    pass

# EJEMPLO  Función sin parámetros

def saludar():
    print("hola a todos")

#llamar a una funcion
saludar()
saludar()

# EJEMPLO función con un parametro

def saludo_persona(nombre):
    print(f"hola {nombre}")

saludo_persona("luis")
saludo_persona("maria")

# persona = input("Dime tu nombre")
# saludo_persona(persona)


# USO DEL RETURN Y DIFERENCIA CON EL PRINT
def saludo_persona(nombre):
    return f"hola {nombre}"

saludo = saludo_persona("Ana")
print(saludo)

print(saludo_persona("felipe"))


# EJEMPLO función con dos parametro

def sumar(a,b,c):
    if a > 5:
        operacion = a + b +c
    else:
        operacion = a - b - c

    return operacion

print(sumar(5,7,5))
print(sumar(15,8,2))



# FUNCIONES argumentos con clave y valor

print(sumar(6, c = 9, b = 8))

# FUNCIONES Función con parámetros predeterminados o por defecto

def multi(x , y = 2):
    return x * y

print( multi(5,5) )
print(multi(5))
print(multi(50))

# FUNCIONES Número arbitrario de parametros

# Si no sabemos la cantidad de argumentos que pasamos a nuestra función, 
# podemos crear una función que pueda tomar una cantidad arbitraria de argumentos 
# agregando * antes del nombre del parámetro.
print("---------------------")
def sumar (*numeros):
    resu = 0
    for i in numeros:
        resu += i
    return resu

    # return sum(numeros)

print(sumar(1,2,3,5,6,8))
print(sumar(1))

# Si queremos pasar argumentos en clave valor o directamente un diccionario podemos usar **kwargs NOOOOO


# ANOTACIONES EN FUNCIONES
def sumar(x ,y) :
    return x + y

def pares(numeros:list):
    lista_numeros = []
    for i in numeros:
        if i % 2 == 0:
            lista_numeros.append(i)
    
    return lista_numeros

print(pares([3,4,6,2,1,7,9]))


def pares(numeros:dict):
    for clave, valor in numeros.items():
        print(clave, valor)


#funciones dentro de funciones

def calculo(a, b, operacion):
    def sumar():
        return a + b

    def restar():
        return a - b

    def multiplicar():
        return a * b

    if operacion == "+":
        return sumar()
    elif operacion == "-":
        return restar()
    elif operacion == "*":
        return multiplicar()
    else:
        return "Operación no válida"


print(calculo(6,3,"-") )


def buscar(lista:list, elemento):
    for i in lista:
        if i == elemento:
            return True

print(buscar([1,2,3], 6))


# 6.- Declare una función llamada add_item. El objetivo es buscar un elemento a una lista




# 7.- Declare una función llamada remove_item. El objetivo es borrar un elemento a una lista



# 8.- Declare una función llamada pares_y_impares. Debe retornar cuantos pares hay en una lista.



# 2.	La temperatura en °C se puede convertir a °F usando esta fórmula: °F = (°C x 9/5) + 32. 
# Escribe una función que convierta °C a °F, convert_celsius_to -fahrenheit .

# 6.	  Crea una única función (importante que sólo sea una) que sea capaz
#   de calcular y retornar el área de un polígono.
#  - La función recibirá por parámetro sólo UN polígono a la vez.
#   - Los polígonos soportados serán Triángulo, Cuadrado y Rectángulo.
#   - Imprime el cálculo del área de un polígono de cada tipo.


