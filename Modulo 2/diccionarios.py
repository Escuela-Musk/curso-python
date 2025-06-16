# Un diccionario es una colección de tipos de datos emparejados (clave: valor) modificables (mutables) desordenados.

# crear un diccionarios ( se crea con {})

mi_diccionario = {"nombre" : "angel", 
                  "edad" : 34,
                  "casado" : True, 
                  "aficiones" : ["pintar", "leer"],
                  }

# ver la longitud

print(len(mi_diccionario))

# acceder a los elementos

aficciones = ["pintar", "leer"]

aficciones[0]
mi_diccionario["aficiones"]


#modificar valores

mi_diccionario["Edad"] = 35

print(mi_diccionario)


otro_dicc = {"nombre":"Luis", "hijos" : 2}

mi_diccionario.update(otro_dicc)
print(mi_diccionario)

# añadir elementos

mi_diccionario["telefono"] = 123456789



#borrar elementos

# Eliminar pares de clave y valor de un diccionario
#     pop(clave) : elimina el elemento con el nombre de clave especificado:
#     popitem() : elimina el último elemento
#     del : elimina un elemento con el nombre de clave especificado


mi_diccionario.pop("edad")
print(mi_diccionario)

mi_diccionario.popitem()
print(mi_diccionario)

mi_diccionario.clear()
print(mi_diccionario)

# Diccionario Anidado

biblioteca = {"el señor de los anillos": { "autor": [1,4], "fecha_publicacion": 1954 },
               "en las montañas de la locura":{ "autor": "H.P.Lovecraft", "fecha_publicacion": 1931 }, 
               "el maestro del prado":{ "autor": "Javier Sierrat", "fecha_publicacion": 2013 },
               }

print(biblioteca["el señor de los anillos"]["autor"][0])

mi_pirmer_libro = { "autor": "J.R.R.Tolkien", "fecha_publicacion": 1954 }



print("--------")

biblioteca = {"el señor de los anillos": { "autor": "J.R.R.Tolkien", "fecha_publicacion": 1954 },
               "en las montañas de la locura":{ "autor": "H.P.Lovecraft", "fecha_publicacion": 1931 }, 
               "el maestro del prado":{ "autor": "Javier Sierrat", "fecha_publicacion": 2013 },
               }





# acceder a las claves usando .keys()
 # nos devuelve las keys en formato lista

mi_diccionario = {"nombre" : "angel", 
                  "edad" : 34,
                  "casado" : True, 
                  "aficiones" : ["pintar", "leer"],
                  }
print(mi_diccionario.keys())

# acceder a los valores usando values()
 # nos devuelve las values en formato lista

print(mi_diccionario.values())

# bucle for con diccionarios
# bucle para acceder a claves y valores
for clave, valor in mi_diccionario.items():
    if type(valor) == list:
        for x in valor:
            print(x, end = ",")
    else:
        print(f"tu clave es {valor}")


# bucle para acceder a claves 
for clave in mi_diccionario.keys():
    print(clave)

#  # bucle para acceder a  valores  
for valor in mi_diccionario.values():
    print(valor)


biblioteca = {"el señor de los anillos": { "autor": "J.R.R.Tolkien", "fecha_publicacion": 1954 },
               "en las montañas de la locura":{ "autor": "H.P.Lovecraft", "fecha_publicacion": 1931 }, 
               "el maestro del prado":{ "autor": "Javier Sierrat", "fecha_publicacion": 2013 },
               }
print("Aaaaaaaaaaaa")
for clave, valor in biblioteca.items():
    print(clave,valor)
    for claves_segundo_dicc, valores_segundo_dicc in valor.items():
        if claves_segundo_dicc == "autor":
            print(f"el autor es {valores_segundo_dicc}")
        else:
            print(f"la fecha de publicacion es {valores_segundo_dicc}")

print("Aaaaaaaaaaaa")
for clave in biblioteca:
    print(clave)


# EJERCICIOS

# Crea un diccionario vacío llamado perro



# Agregue nombre, color, raza, patas y edad al diccionario de perros



# Obtener la longitud del diccionario del estudiante


# agrega un clave habilidades con una lista de habilidades como valores



# Obtenga el valor de las habilidades y verifique el tipo de datos, debería ser una lista



