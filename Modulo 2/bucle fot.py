# # #Bucle FOR
# # # Un bucle o loop en python es una acción que se repite muchas veces
# # # La palabra clave for se utiliza para crear un bucle for, similar a otros lenguajes de programación, 
# # # pero con algunas diferencias de sintaxis. El bucle se utiliza para iterar sobre una secuencia 
# # # (es decir, una lista, una tupla, un diccionario, un conjunto o una strings) estos son llamados objetos iterables.

# # # SINTASIS
# # # for x in objeto_iterable:  # x es una variable interna para el bucle, su valor varía en cada iteración del bucle
# # #     pass        # que hacemos dentro del bucle


# # # BUCLE SOBRE UN STRING
# saludo = "Hola"

# for letra in saludo:
#     print(letra)


# # # BUCLE SOBRE UNA LISTA

# comidas = ["pera", "manzana", "uva"]    

# for comida in comidas:
#     print(comida)


# # # bucle sobre un numero entero

# num = 123


# for n in str(num):
#     print(n)

# # print("-----------")
# # # La función de rango
    
# # # La función range() se utiliza como lista de números. [1,2,3,4,5,6]
# # # El rango  toma tres parámetros: 
# # # inicio, fin e incremento (inicio, fin, paso). De forma predeterminada, comienza desde 0 y el incremento es 1.
# # # Hay que tener en cuenta que el fin nunca se incluye, es decir si se hace range(1,10) este rango acaba en 9. 
# # # La secuencia de rango necesita al menos 1 argumento (fin). 

# # # range con un parametro
# num = 20

# for numero in range(num+1):
#     print(numero)

# for numero in range(11):
#     print(numero)

# # print("-----------")
# # # range con dos parametro

# for numero in range(5,11):
#     print(numero)

# # print("-----------")


# # # range con tres parametro

# for numero in range(1,21,3):
#     print(numero)


# # print("------")

# # # salto hacia atras

# for numero in range(2):
#     print(numero)

# # # usar el else con bucle for, el else solo se ejecuta si el bucle acaba de forma natural
# # print("------")

# name = "luis"

# for letra in name:
#     if  letra == "w":
#         break
#     else:
#         print(letra)
# else:
#     print("todo ha ido bien")






# # BUCLE FOR - MISION ESPACIAL 🚀
# # Explicación simplificada para alumnos sin listas, tuplas ni diccionarios.
# # Un bucle for permite repetir una acción varias veces sin escribirla de nuevo.
# # Vamos a usarlo para viajar por el espacio y explorar tierras.

print("🚀 Bienvenidos a la Misión Espacial de Python! 🌌\n")

# 🔹 Cuenta regresiva para el despegue
print("Iniciamos la cuanta atras para el despegue...")

for fff in range(5,-1,-1):
    print(f"T-{fff} segundos...")

print("🔥 ¡Despegue! Hacia la exploración espacial... 🚀\n")

# 🔹 Explorando tierras usando un bucle for con range
print("🛰️ Viajaremos a 8 tierras en esta misión.")

for gggg in range(1,3):
    print(f"Explorando el tierra número {gggg}...")
    pregunta = input("Quieres recoger una muestra (si/no): ")

    if pregunta == "si":
        print(f"🔬 Recolectando muestras en el Tierra {gggg}... ¡Misión cumplida!\n")
    else:
        print(f"🚀 Saliendo del tierra {gggg} hacia el siguiente destino...\n")

# 🔹 Contando los tierras explorados
tierras_explorados = 0
for numero in range(1, 3):
    tierras_explorados += 1
print(f"✅ Misión completada. Se exploraron {tierras_explorados} tierras.\n")

# 🔹 Desafíos extra
print("\n🌟 Desafíos para astronautas avanzados:")
print("1. Modifica el código para hacer una cuenta regresiva desde un número elegido por el usuario.")
print("2. Crea un contador que solo cuente los tierras en los que se recolectaron muestras.")


print("👨‍🚀 ¡Felicitaciones, astronautas! Han completado su entrenamiento en bucles FOR. 🌍")




#EJERCICIOS

# 1.	Escribe un programa que imprima los números del 1 al 10 




# 2.	Escribe un programa que imprima los números pares del 1 al 20.



# 3.	Escribe un programa que calcule la suma de los primeros 10 números naturales.



# 4.	Escribe un programa que imprima la tabla de multiplicar del 5.


# Escribe un programa que imprima los números del 1 al 100, 
# pero que reemplace los múltiplos de 3 por "Fizz", los múltiplos de 5 por "Buzz" y
# los múltiplos de ambos por "FizzBuzz".
   



# EJERCICIOS PARA TRABAJAR EN CASA
   
# Escribe un programa que imprima la serie de Fibonacci hasta el décimo término. 

# Escribe un programa que encuentre e imprima todos los números primos menores que 100.


