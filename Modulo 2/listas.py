# Lista: es una colección ordenada y modificable (modificable). Permite miembros duplicados.

# 1.- Como crear una lista
mi_lista = ["sandia", "verde", 123, True]
print(type(mi_lista))

#2.-  como acceder a los elmentos de una lista
colores = ["verde", "rojo", "azul", "blanco", "negro"]
color1 = (colores[1])
print(colores[-1])

print("------------")
#3.-  modificar un elemento de la lista
colores[1] = "lila" # rojo = lila
print(colores)
print("------------")

#4.-  Comprobación de elementos en una lista
    # Verificar un elemento si es miembro de una lista usando el operador in . Vea el ejemplo a continuación.
existe = "azul" in colores
print("azul" in colores)


# 5.- Longuitd de lista: con len vemos la longuid de la lista, siempre empieza a contar en 1
colores = ["verde", "rojo", "azul", "blanco", "negro"]
print(len(colores))

#6.- añadir un nuevo elemento

# con el metodo append añadimos el elemento al final de la lista
colores.append("amarillo")
print(colores)
 # con el insert, añadimos el elemento en una posición en concreto,
    # siempre ponemos primero el indice donde queremos insertar y luego el elemento
colores.insert(1,"gris")
print(colores)
# 7.- Eliminar elementos de una lista
#7.1-  El método remove elimina un elemento específico de una lista
colores = ["verde", "rojo", "azul", "blanco", "negro"]
colores.remove("negro")
print(colores)
# 7.2- Eliminar elementos usando Pop
    # El método pop() elimina el índice especificado (o el último elemento si no se especifica el índice):
color_borrado = colores.pop(0)
print(color_borrado)


alumnos = ["pepe", "luis","soraya","luis"]
alumnos_borrados = []
for indice in range(len(alumnos)-1):
    if alumnos[indice] == "luis":
        borrado = alumnos.pop(indice)
        alumnos_borrados.append(borrado)

print(alumnos)
print(alumnos_borrados)

# uso del del !!!! OJO!!!!!!

del colores[0]

# 8.- Contar elementos en una lista
    #   El método count() devuelve el número de veces que aparece un elemento en una lista:
alumnos = ["pepe", "luis","soraya","luis"]
print(alumnos.count("luis"))

# 9.- Invertir una lista
    # El método reverse() invierte el orden de una lista. 
alumnos.reverse()
print(alumnos)
print("-----------")
#  10.- Ordenar elementos de la lista
    # Para ordenar listas podemos usar el método sort() o las funciones integradas sorted() . 
num = [2,65,35,5]

#  10.1.- El método sort() reordena los elementos de la lista en orden ascendente y modifica la lista original. 
    # Si un argumento del método sort() inverso es igual a verdadero, organizará la lista en orden descendente.
    # sort(): este método modifica la lista original
num.sort(reverse=True)
print(num)


    #sorted(): devuelve la lista ordenada sin modificar la lista original Ejemplo:
num = ["aadf","zdfsa","cdasf"]
num_ordenada = sorted(num)
print(num_ordenada)

# 11.- Cortar elementos de una lista
    #  podemos especificar un rango de índices positivos especificando el inicio, 
    # el final y el salto, el valor de retorno será una nueva lista. 
    # (valores predeterminados para inicio = 0, fin = len(lst) - 1 (último elemento), salto = 1)
    # listas de listas
fruits = ['banana', 'orange', 'mango', 'lemon']

all_fruits = fruits[0:4]


all_fruits = fruits[:] 

orange_and_mango = fruits[1:3] 

orange_mango_lemon = fruits[:2]

orange_and_lemon = fruits[2:-1:-1]
print(orange_and_lemon)

# 12.- listas de listas
matriz = [[1,2,3], [4,5,6]]

print(matriz[1][0])

    # aqui accedemos a la primera sublista


    # aqui accedemos al primer elemento de la primera sublista


    # modificar elementos de una sublista


    # añadir elementos a una sublista







# EJERCICIOS

#1.	Declarar una lista vacía


#2.	Declarar una lista con más de 7 elementos



#3.	Encuentra la longitud de tu lista




# 4.	Corta tu lista, muestra los 2 primeros elementos, luego muestra los dos últimos



# 5.	Obtenga el primer elemento, el elemento del medio y el último elemento de la lista.



# 7.	Suma de elementos: Escribe un programa que sume todos los elementos de una lista de números enteros.


    
