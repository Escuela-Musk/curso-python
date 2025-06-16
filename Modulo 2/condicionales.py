# # OPERADORES DE COMPARACIÓN
# < MENOR QUE
# <= MENOR IGUAL QUE
# > MAYOR QUE
# >= MAYOR IGUAL QUE

# == IGUALDAD
# != DIFERENTE


# 1.- CONDICIONALES
"""
Vamos a trajabar con condicionales, es decir si se cumple una condición determinada el programa que hagamos
realizará una acción en concreto, sino se cumple hará otra. Un ejemplo de la vida real puede se:
    - Si salgo a la calle y llueve cojo el paraguas y sino llueve lo dejo en casa. 
        En este ejemplo hay dos condiciones, si llueve y sino llueve cierto?
    
    Pero en otras ocasiones tenemos más de dos opciones, como puede ser esta:
    - Si llueve a la calle cojo el paraguas, si salgo a la calle llueve y hace mucho viento cojo el chubasqueros
      pero sino llueve ni hace viento, no me lleva nada.
      En este ejemplo tenemos tres condiciones, sabrias decirme cuales son?

    Para acabar, comentar que podemos poner tantas condiciones como se nos pida o se nos ocurra a la hora de 
    hacer nuestro programa, puede haber 1 condición, 2 condiciones, 3 condiciones, 4 condiciones...
"""

#1.1.- Sintasis de un condicional en python

# 1.1.1 - Una condicion
"""
Usaremos siempre la palabra reservada "if" seguida de la condicion que queramos valorar, esto será siempre obligatorio
es decir la primera condición empieza con el "if" siempre.

sintasis del if:
    if condicion:
        accion

"""
num1 = 13

if num1 < 10:
    print("es menor que 10")



# 1.1.2 - Dos condiciones
"""
Usaremos siempre la palabra reservada "if" seguida de la condicion que queramos valorar, esto será siempre
 obligatorio
es decir la primera condición empieza con el "if" siempre. 
Pero si tenemos DOS condiciones, en la primera usamos el "if" y en la segunda usamos el "else", el "else" 
es como decir
si no ocurre lo anterior pasará esto.
A diferencia del "if" el "else" no necesita valorar condición, por lo que la sintasis es:
    -else:
        acción

"""

num1 = 13

if num1 < 10:
    print("es menor que 10")

else:
    print("mayor que 10")



# 1.1.3 - tres condiciones o más

"""
Usaremos siempre la palabra reservada "if" seguida de la condicion que queramos valorar, esto será siempre obligatorio
es decir la primera condición empieza con el "if" siempre. 
Pero si tenemos TRES O MAS condiciones, en la primera usamos el "if", en la segunda
usamos el "elif" y en la utlima usamos el "else".
En caso de tener cuatro condiciones sería, primera con "if", segunda con "elif", tercera con "elif" y ultimo "else"

"""
# EJEMPLO

num1 = 3

if num1 < 10:
    print("es menor que 10")

elif num1 > 10:
    print("es mayor que 10")

else:
    print("es igual que 10")


comida = "pera"

if comida == "manzana":
    print("tu comida es una manzana")
elif comida == "melon":
    print("tu comida es melon")
elif comida == "sandia":
    print("es una sandia")
elif comida == "pera":
    print("es una pera")
else:
    print("no ninguna de las anteriores")

num1 = 3
if num1 <= 10:
    print("es menor o igual")
elif num1 > 10:
    print("es mayor que 10")

if num1 % 2 == 0:
    print("el numero es par")
else:
    print("es impar")



# OPERADORES LOGICOS

"""
and : es igual que y  
        SINTASIS DEL AND:
            IF CONDICION 1 and CONDICION 2:
            PARA QUE EL RESULTADO SE TRUE AMBAS CONDICIONES TIENEN QUE SER TRUE

            TABLA DE LA VERDAD DEL AND:

                |CONDICION 1 | CONDICION 2 | RESULTADO |

                |    TRUE    |   TRUE      |    TRUE   |
                |    TRUE    |   FALSE     |    FASLE  | 
                |    FALSE   |   TRUE      |    FALSE  |
                |    FALSE   |   FALSE     |    FALSE  |

or : es igual que o 

        SINTASIS DEL OR:
           if CONDICION 1 or CONDICION 2
            PARA QUE EL RESULTADO SEA TRUE, BASTA CON QUE UNA DE LAS  CONDICIONES SEA VERDADERAS

            TABLA DE LA VERDAD DEL OR

                |CONDICION 1 | CONDICION 2 | RESULTADO |

                |    TRUE    |   TRUE      |    TRUE   |
                |    TRUE    |   FALSE     |    TRUE   |
                |    FALSE   |   TRUE      |    TRUE   |
                |    FALSE   |   FALSE     |    FALSE  |
"""




# 2. CONDICIONALES CON OPERADORES LOGICOS

# EJEMPLO

# Verificar si una persona tiene  saldo en su cuenta bancaria y es mayor de edad
print("----------------")
saldo = float(input("introduce el saldo de tu cuenta: "))
edad = int(input("dime tu edad: "))

if saldo > 0 and edad >= 18:
    print(f"Su saldo en cuenta es positivo {saldo} y usted es mayor de edad {edad}")

else:
    print(f"❌ No cumple una de las condiciones ")



# Verificar si una persona tiene suficiente saldo en su cuenta bancaria o es cliente VIP

saldo = 0
vip = False
visa = "normal"

if saldo >= 70000:
    vip = True

if vip:
    if saldo >100000:
        visa = "platino"
    elif saldo > 200000:
        visa = "oro"
    else:
        print("")






# Par o impar: Crea un programa que solicite al usuario ingresar un número entero y luego determine 
# si el número ingresado es par o impar. Imprime un mensaje indicando el resultado.





# Escribir un programa que almacene la cadena de caracteres contraseña en una variable,
    #  pregunte al usuario por la contraseña e imprima por pantalla si la contraseña introducida 
    # por el usuario coincide con la guardada en la variable.




# Clasificador de triángulos: Escribe un programa que solicite al usuario ingresar las longitudes de 
# los tres lados de un triángulo. Luego, determine y muestre si el triángulo es equilátero 
# (todos los lados son iguales), isósceles (dos lados son iguales) o escaleno (todos los lados son diferentes).


# # Escribe un programa que solicite al usuario ingresar su edad y si tiene un carnet de estudiante 
#     # (responde "s" para sí y "n" para no. verificar si la persona es menor de 25 años y tiene un carnet
#     #   de estudiante. Si ambas condiciones se cumplen, imprime "Eres elegible para el descuento de estudiante", 
#     #   de lo contrario, imprime "No eres elegible para el descuento de estudiante".




# # 1.	Clasificación de Edad: Solicita al usuario que ingrese su edad y clasifícala
# # en "niño" (0-12 años), "adolescente" (13-17 años), "adulto joven" (18-25 años), 
# # "adulto" (26-64 años), o "adulto mayor" (65 años en adelante).



