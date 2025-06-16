# TIPOS DE DATOS
"""
STRIGNS => SON CADENAS TEXTO Y SIEMPRE VAN ENTRE COMILLAS DOBLES O SIMPLES "  '
NUMEROS:
    - INT => NUMEROS ENTEROS  EJ : 54
    - FLOAT => NUMEROS DECIMALES EJ : 5.2
    - COMPLEX => NUMEROS COMPLEJOS EJ 1 + 5J
BOOLEAN => SON DE TIPO BOLEANO EJ: True False  (verdadero o false)

"""
# EJEMPLOS
# print("Hola gente")
# print(23)

print(type("hola gente"))
print(type(34))
print(type(4.5))
print(type(1 + 5J))
print(type(True))

# VARIABLES

"""
Una variable es una "caja" donde almaceno un dato en concreto
"""


# EJEMPLOS
nombre = "Jose Antonio"
edad = 38
casado = True

print(nombre)
print(edad)

print(nombre, edad, casado)
print('mi nombre es jose antonio y mi alias es   "josan"   ')
print("she's")


print("------------------")
#DAR FORMATO A UN STRING

print("mi nombre es", nombre, "y mi edad es",edad)
print("mi nombre es {} y mi edad es {}".format(nombre, edad))
print(f"mi nombre es {nombre} y mi edad es {edad}")


# declar variables en una linea (NO ES RECOMENDABLE USARLO, PERO HAY QUE SABER QUE SE PUEDE HACER)
 
nombre, edad, casado , color, animal, cp, = "jose antonio", 29, False, 56, "perro", ""


# USO DEL INPUT (ENTRADAS DE DATOS POR TERMINAL)
# nombre = input("dime tu nombre: ")
# print(f"tu nombre es {nombre}")

# edad = int(input("dime tu edad:"))
# print(type(edad))

# altura = float(input("dime tu altura:"))
# print(type(altura))

# OPERADORES ARITMETICOS CON NUMEROS
"""
suma : +
resta : -
multiplicacion  *
division /   ME DA EL RESULTADO REAL DE LA DIVISION
division entera //  ME DA LA PARTE ENTERA DE LA DIVISION
residuo %    ME DA EL RESTO DE LA DIVISION  se usa sobre todo cuando quereis averiguar si un numero es multiplo de otro
potencia **  ELEVAMOS A LA POTENCIA INDICADA
"""
# EJEMPLOS
num1 = 10
num2 = 3
print("--------")
print(num1 + num2)  # 13
print(num1 - num2) # 7
print(num1 * num2) #30
print(num1 / num2) #3.3333
print(num1 // num2) #3
print(num1 % num2) #1
print(num1 ** num2) #1000



# OPERADORES ARITMETICOS CON CADENAS DE TEXTO (STRINGS)

palabra1 = "hola"
palabra2 = "Adios"

print(palabra1 + palabra2)  #concatenar
# print(palabra1 - palabra2)
# print(palabra1 * palabra2)
print (palabra1 * 5)

print("hola" + "adios")



# OPERADORES COMPARACIÓN 

"""
< menor que
> mayor que
>= mayor igual que
<= menor igual que
== igualdad
!= diferente
"""

# EJEMPLOS
print("--------")
num1 = "5"
num2 = "a"

print(num1 < num2)  # 
print(num1 <= num2) # 
print(num1 >= num2) # 
print(num1 > num2) # 
print(num1 == num2) #  
print(num1 != num2) # 

print(nombre)
nombre = "luis"
print(nombre)

# ejercicios

# 1.	declara 3 variables diferentes, para obtener datos personales de una persona y 
# luego haz un print de ellos en una misma linea



    
# 2.	declara 2 variables numericas y haz la suma y mulipliación de ellas



# Declara dos variables numéricas y averigua cual es su residuo y su división entera


# 4.	dada esta variable, num1 = 4.5 dime su tipo



# declara dos variables que sean comida, luego compara si ambas comidas son iguales "ñ"

