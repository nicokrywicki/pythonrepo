# EJercicios While --> https://www.tutorialspoint.com/python3/python_while_loop.htm

# Ejercicio 1
"""
Escriba una funcion que le pida al usuario un número entero
y que compruebe si el número es menor que 10.
Si no lo es, debe volver a leer el número repitiendo la operación hasta que el usuario escriba un valor correcto.
Finalmente, debe escribir por pantalla el valor leído cuando este sea correcto.
"""
def edad():
    edad = int(input("introduzca su edad "))
    while edad >= 10:
        print("vuelva a introducir la edad que sea menor a 10 ")
        edad = int(input("introduzca su edad "))
    print(str(edad))    
# edad()    

# Ejercicio 2
"""
Modifique la funcion del ejercicio anterior para que, en vez de comprobar que el número sea menor que 10, compruebe que se encuentre en el rango 0 a 20.
"""
def modificacion():
    edad = int(input("introduzca su edad "))
    while edad<=0 or edad>20:
        print("vuelva a introducir la edad que se encuentre entre 0 y 20 ")
        edad = int(input("introduzca su edad "))
    print(str(edad))    
# modificacion()


# Ejercicio 3
"""
Modifique la funcion del ejercicio anterior para que cuente las veces que ha leído un número de teclado y escriba el resultado por pantalla.
"""
def modificacion():
    count = 0
    edad = int(input("introduzca su edad "))
    while edad<=0 or edad>20:
        print("vuelva a introducir la edad que se encuentre entre 0 y 20 ", count + 1) 
        count = count + 1
        edad = int(input("introduzca su edad "))
    print( "se repite",count, "veces")    
# modificacion()



#Ejercicio 4
"""
Modifique la funcion del ejercicio anterior para que se realicen 5 lecturas por teclado como máximo.
Documentacion --> https://www.ionos.com/digitalguide/websites/web-development/python-break-continue/
"""
def modificacion():
    count = 0
    edad = int(input("introduzca su edad "))
    while edad<=0 or edad>20:
        print("vuelva a introducir la edad que se encuentre entre 0 y 20 ", count + 1) 
        count = count + 1
        while  count >= 5:
            print (" son 5 lecturas")
            break
        edad = int(input("introduzca su edad "))
    print("edad",edad, "el contador se repite",count, "veces") 
  
# modificacion()


#Ejercicio 5
"""
Escriba una funcion que calcule e imprima la suma de los n primeros números enteros positivos.
El valor de n debe leerse del teclado y ser ingresado por el usuario.
"""

