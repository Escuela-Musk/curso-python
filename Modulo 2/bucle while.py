
# # BUCLE WHILE

# # Usamos la palabra reservada while para hacer un bucle while. Se utiliza para ejecutar un bloque de declaraciones 
# # repetidamente hasta que se cumpla una condición determinada. 
# # Cuando la condición se vuelve falsa, las líneas de código después del bucle continuarán ejecutándose. 
# # Tambien se puede sustituir la condición directamente por un dato booleano o por una variable que contenga un 
# # tipo booleano

#   # sintasis

# # while condicion:
# #      pass


# # Ejemplo, haz un programa que muestre por pantalla todos los numeros del 0 al 5

# num = 0
# while num <= 5:
#   print(num)
#   num += 1



# # En el ciclo while anterior, la condición se vuelve falsa cuando el recuento es mayor a 5. 
# # Ahí es cuando el ciclo se detiene. 
# # Si estamos interesados ​​en ejecutar un bloque de código una vez que la condición ya no sea cierta, 
# # podemos usar else .

#   # syntax
# # while condition:
# #     code 
# # else:
# #     code 


# # Ejemplo
# num = 10
# while num <= 5:
#   print(num)
#   num += 1

# else:
#   print("todo ha ido bien")

# # Break: Usamos break cuando queremos salir o detener el ciclo.

# # syntax

# # while condicion:
# #     if otra_condicion:
# #         break
    
# num = 0
# while num <= 5:
#   if num == 3:
#     break
    
#   print(num)
#   num += 1

# else:
#   print("fin")

# # Continue: Con la instrucción continuar podemos omitir la iteración actual y continuar con la siguiente:
#   # syntax

# # while condicion:
# #     if otra_condicion:
# #         continue

# # Ejemplo, printa todos numeros impares del 1 al 10

# print("---------------")
# num = 1
# while num <= 10:
#   if num % 2 != 0:
#     print(num)


# El bucle while anterior solo imprime 0, 1, 2 y 4 (salta 3).




while True:
    print("\n--- Menú ---")
    print("1. Saludar")
    print("2. Mostrar fecha")
    print("3, Salir")


    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        print("¡Hola! ")
    
    elif opcion == "2":
      print("adios")
    
    elif opcion == "3":
      break
    
    else:
      print("opcion no valida")

while True:
  for

# EJERCICIOS 

# 1-	Imprimir Números: Imprime los números del 1 al 10. 



# 2-	Tabla de Multiplicar Específica: Pide al usuario un número y 
# luego imprime la tabla de multiplicar de ese número del 1 al 10.



# 3-	Contar letras: Pide al usuario una palabra y cuenta cuántas letras hay en esa palabra.
    


# 5-	Escriba un programa que pregunte una y otra vez si desea continuar con el programa, 
#     siempre que se conteste exactamente sí (en minúsculas y con tilde).


# 7-	Patrón de Estrellas: Imprime el siguiente patrón de estrellas:
# *
# **
# ***  
# **** 
# *****
    

