# Ejercicio 1
# Escribir un funcion que pregunte al usuario su edad y muestre por pantalla si es mayor de edad o no.
# Para realizar este ejercicio necesitamos conocer la funcion nativa de python input()
# Documentacion --> https://www.w3schools.com/python/ref_func_input.asp
# Tener en cuenta que la funcion input retorna un string, por lo que tenemos que convertirlo a entero(int)
def edad():
    edad=int(input("introduzca su edad"))
    if edad >= 18:
        print("mayor de edad")
    else:   
        print("menor de edad") 


# edad()

# Ejercicio 2
# Escribir una funcion que pida al usuario una palabra y la muestre por pantalla 10 veces.

# def funcion2():
#     palabra = input("inserte una palabra")
#     print(palabra)
#     for i in range(1, 11):
#         print(palabra)
# funcion2()        
# Ejercicio 3
# Escribir un funcion que pregunte al usuario un número que represente un mes, escribir el nombre del mes correspondiente.
# Para realizar este ejercicio tenemos que utilizar los indices de una lista: 
# Documentacion --> https://www.programiz.com/python-programming/list
# Puede haber error en el número dado.
# aa = ["enero", "febrero", "marzo", "abril", "mayo", "junio", "julio", "agosto", "septiembre", "octubre", "noviembre", "diciembre"]
# def funcion3():
#     aa = 
#     if aa > 12:    
#         print("no es un mes")
#     elif aa < 12: 
#         print("es un mes") 
# funcion3()

# Ejercicio 4
# Escribir una funcion que pida al usuario ingresar tres números. La funcion debera hallar el mayor numero y lo muestrarlo por pantalla.
# def funcion1():
#     numeros = input("ingresar 3 numeros")
#     maximo = max(numeros)
#     print(maximo)

# funcion1()    

# Ejercicio 5
# Escribir una funcion que almacene la cadena de caracteres "contraseña" en una variable
# Pregunte al usuario por la contraseña e imprima por pantalla si la contraseña introducida por el usuario coincide con la guardada 
# sin tener en cuenta mayúsculas y minúsculas.
# def contraseña():
#     pw_create = input("cree su contraseña")
#     pw_check = input("escriba una contraseña")
#     if pw_check == pw_create:
#         print("es corecta")
#     elif pw_check != pw_create:
#         print("es incorrecta")     

# contraseña()



# Ejercicio 6
# Teniendo la siguiente lista de barrios:
# barrios_caba = ["Barrios", "Agronomía", "Almagro", "Balvanera", "Barracas", "Belgrano", "Boedo", "Caballito", "Chacarita", "Coghlan"]
# Escribir una funcion que muestre por pantalla los barrios que incien con las letras "ba"
# Para realizar este ej. podemos utilizar el metodo .startswith("Ba") de los objetos de tipo string: string.startswith("Ba")
# Documentacion --> https://www.w3schools.com/python/ref_string_startswith.asp

# def barrios():
    # barrios_caba = ["Barrios", "Agronomía", "Almagro", "Balvanera", "Barracas", "Belgrano", "Boedo", "Caballito", "Chacarita", "Coghlan"]
    # for i in barrios_caba: 
    #     if i.startswith("Ba"):
    #         print(i)    

# barrios()



# Ejercicio 7
# Escribir una funcion para hallar la superficie de un triangulo conociendo la base y la altura.
# El programa tiene que solcitar al usuario que ingrese la base y la altura.
# Superficie = base * altura / 2
# def superficie():
#     # formula = input("ingrese la base y la altura")
#     # print(formula)
#     b=int(input("introduce el valor de base"))
#     a=int(input("introduce el valor de altura"))
#     superficie = (b*a)/2
#     print(superficie)


# superficie()




# Ejercicio 8
# Escribir una funcion que pida al usuario dos números y muestre por pantalla su división.
# Si el divisor es cero el programa debe mostrar un error.
# def division():
#     a=int(input("introducir el primer numero "))
#     b=int(input("introducir el segundo numero "))
#     division = (a/b)
#     print(division)
#     if a/b == 0:
#         print("error")

# division()    

# Ejercicio 9
# Volvemos a utilizar la lista de barrios:
# barrios_caba = ["Barrios", "Agronomía", "Almagro", "Balvanera", "Barracas", "Belgrano", "Boedo", "Caballito", "Chacarita", "Coghlan"]
# Escribir un programa que muestre por pantalla todos los barrios dentro de la lista pero en mayuscula
# Para realizar este ej. podemos utilizar el metodo .upper() de los objetos de tipo string string.upper() 
# Documentacion --> https://www.w3schools.com/python/ref_string_upper.asp


# Ejercicio 10
# Escribir una funcion que pida al usuario un número entero y muestre por pantalla si es par o impar.
# def parimpar():
#     numero = 0
#     numero=int(input("introduzca un numero"))
#     if numero%2 == 0:
#         print("par")
#     else:
#         print("inpar")
# parimpar()    



# Ejercicio 11
# Dada la siguiente lista de frutas:
# frutas = ["manzana", "banana", "pera", "anana"]
# Escribir un programa que le solicite al usuario una fruta y verifique si esta existe dentro de la lista de frutas.
# Para realizar este ejercicio podemos utilizar la palabra reservada in.
# Documentacion --> https://www.w3schools.com/python/ref_keyword_in.asp

# def frutas ():
#     frutas = ["manzana", "banana", "pera", "anana"]
#     a = input("introduzca el nombre de la fruta ")
#     if a in frutas:
#         print("si")
#     else:
#         print("no")    

# frutas()


# Ejercicio 12
# Para tributar un determinado impuesto se debe ser mayor de 18 años y tener unos ingresos iguales o superiores a $300.000 mensuales.
# Escribir una funcion que pregunte al usuario su edad, sus ingresos mensuales y muestre por pantalla si el usuario tiene que tributar o no.
# def impuestos ():
#     tributar = int(input("introduzca su edad"))
#     print(tributar)
#     if not tributar >= 18:
#         print("usted no debe tributar impuestos")
#     else:
#     sueldo= int(input("introduzca su sueldo mensual"))  
#     if sueldo >= 300000:
#         print("usted debe pagar impuestos")
#     else:
#         print("zafó")          
# impuestos()


# Ejercicio 13
# Escribir una funcion que pida al usuario una frase y luego imprimir un listado de las vocales que aparecen en esa frase (sin repetirlas)

def vocales():
    vocales = ["a", "e", "i", "o", "u"]
    frase=input("escriba una frase ")
    for x in vocales:
        contador=0  
        for i in frase:
            if x==i:
                contador=1
        print(x, "aparece =", contador)


    

# vocales()

# Ejercicio 14
# Los alumnos de un curso se han dividido en dos grupos A y B de acuerdo al sexo y el nombre.
# El grupo A esta formado por las mujeres con un nombx  re anterior a la M y los hombres con un nombre posterior a la N y el grupo B por el resto.
# Escribir una funcion que pregunte al usuario su nombre y sexo, y muestre por pantalla el grupo que le corresponde.


# Ejercicio 15cmd
# Los tramos impositivos para la declaración de la renta en un determinado país son los siguientes:
# 			Renta					Tipo impositivo
#		Menos de 10000€					5%
#		Entre 10000€ y 20000€			15%
#		Entre 20000€ y 35000€			20%
#		Entre 35000€ y 60000€			30%
#		Más de 60000€					45%
# Escribir una funcion que pregunte al usuario su renta anual y muestre por pantalla el tipo impositivo que le corresponde.

def renta():
    renta=int(input("introduzca su renta anual "))
    if renta < 10000:
        print("tipo impositivo 5%")
    elif 10000 <= renta <= 20000:
        print("tipo impositivo 15%")
    elif 20000 <= renta <= 35000:
        print("tipo impositivo 20%")  
    elif 35000 <= renta <= 60000:
        print("tipo impositivo 30%")      
    else:
        print("tipo impositivo 45%")
# renta()
# Ejercicio 16
# Escribir una funcion que pida al usuario un número entero positivo
# y muestre por pantalla todos los números impares desde 1 hasta ese número separados por comas.
# Para realizar este ej. podemos utilizar la funcion nativa de python range(start, stop, step).
# Documentacion --> https://www.w3schools.com/python/ref_func_range.asp 
# La funcion range utiliza 2 variables numericas start, stop como incio y fin.
# La tercer variable tambien numerica step especifica el incremento.
def numeros():
     m=int(input("introducir un numero mayor a 0"))
     print(m)
     if m > 0: 
         x = range(1, m, 2)
         for n in x:
              print(n)    
    

# numeros()    


# Ejercicio 17
# En una determinada empresa, sus empleados son evaluados al final de cada año.
# Los puntos que pueden obtener en la evaluación comienzan en 0.0 y pueden ir aumentando, traduciéndose en mejores beneficios.
# Los puntos que pueden conseguir los empleados pueden ser 0.0, 0.4, 0.6 o más, pero no valores intermedios entre las cifras mencionadas.
# A continuación se muestra una tabla con los niveles correspondientes a cada puntuación.
#			Nivel					Puntuación
#		Inaceptable						0.0
#		Aceptable						0.4
#		Meritorio						0.6 o más
# La cantidad de dinero conseguida en cada nivel es de $100.000 multiplicada por la puntuación del nivel.
# Escribir una funcion que lea la puntuación del usuario e indique su nivel de rendimiento, así como la cantidad de dinero que recibirá el usuario.
def empleado():

    plata = 100000
    inaceptable = 0.0
    aceptable = 0.4
    meritorio = 0.7   


    puntaje=float(input("introducir su puntaje "))
    print(puntaje)
    if puntaje == 0.0:
        rendimiento = "inaceptable"
    elif puntaje == 0.4:
        rendimiento = "aceptable"
    elif puntaje >= 0.7:
        rendimiento = "meritorio"
    else:
        print("el numero tiene que ser 0.0, 0.4, 0.7 o superior") 
    
    print("el nivel de rendimiento", rendimiento)  
    print("la remurenación es de:", plata*puntaje)   

# empleado()


# Ejercicio 18
# Escribir una funcion que pregunte al usuario su edad y muestre por pantalla todos los años que ha cumplido (desde 1 hasta su edad).
def edad():
    edad=int(input("introduzca su edad"))
    x = range(0, edad, 1)
    for n in x:             
        print(n+1)

    
# edad()

# Ejercicio 19
# Escribir una funcion para una empresa que tiene salas de juegos para todas las edades 
# y quiere calcular de forma automática el precio que debe cobrar a sus clientes por entrar. 
# El programa debe preguntar al usuario la edad del cliente y mostrar el precio de la entrada. 
# Si el cliente es menor de 4 años puede entrar gratis, si tiene entre 4 y 18 años debe pagar $1200 y si es mayor de 18 años, $2000.
def juegos():
    edad=int(input("introduzca su edad "))
    if edad <= 4:
        print("no paga")
    elif 4 < edad <= 18:
        print("debe pagar $1200 ")
    else:
        print("debe pagar $2000 ")        

# juegos()

# Ejercicio 20
# La pizzería Bella Napoli ofrece pizzas vegetarianas y no vegetarianas a sus clientes. Los ingredientes para cada tipo de pizza aparecen a continuación.
# 		- Ingredientes vegetarianos: Morron y tofu.
#		- Ingredientes no vegetarianos: Longaniza, Jamón y Salmón.
# Escribir una funcion que pregunte al usuario si quiere una pizza vegetariana o no
# y en función de su respuesta le muestre un menú con los ingredientes disponibles para que elija.
# Solo se puede eligir un ingrediente además de la mozzarella y el tomate que están en todas la pizzas.
# Al final se debe mostrar por pantalla si la pizza elegida es vegetariana o no y todos los ingredientes que lleva.
# def pizzas():


# pizzas()

# Ejercicio 21
# Escribir un programa que pida al usuario una palabra y luego muestre por pantalla una a una las letras de la palabra introducida empezando por la última.
# Para realizar este ejercicio tenemos que entender los indices de un objeto iterable
# Documentacion --> https://www.digitalocean.com/community/tutorials/how-to-index-and-slice-strings-in-python-3
def palabra():
    palabra=input("introduzca una palabra ")
    print(palabra[::-1])
# palabra()

def numereo():
    numero=int(input("escriba un numero mayor a 0"))
    if numero > 0: 
        print("es un numero positivo")
    else:    
        print("numero negativo")


numero()
