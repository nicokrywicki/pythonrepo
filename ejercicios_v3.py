#Ejercicios Diccionarios --> https://ellibrodepython.com/diccionarios-en-python

#Ejercicio 1
"""
Escribir un programa que guarde en una variable el diccionario {'Euro':'€', 'Dollar':'$', 'Yen':'¥'}.
Preguntar al usuario por una divisa y muestre su símbolo o un mensaje de aviso si la divisa no está en el diccionario.

"""
def divisa():
    divisa = {'euro':'€', 'dolar':'$', 'yen':'¥'}
    a = input("escriba su divisa ")
    if a in divisa.keys():   
        print(divisa[a])




    else:
        print("no existe su divisa")    


# divisa()



#Ejercicio 2
"""
Escribir un programa que pregunte al usuario su nombre, edad, dirección y teléfono y lo guarde en un diccionario.
Después debe mostrar por pantalla el mensaje <nombre> tiene <edad> años, vive en <dirección> y su número de teléfono es <teléfono>.

"""
def datos():
    datos = {
    "nombre": input("ingrese su nombre "),
    "edad": input("ingrese su edad "),
    "direccion": input("ingrese su direccion "),
    "telefono": input("ingrese su telefono ")
    }
    print(
        datos.get("nombre"), "tiene ",
        datos.get("edad"), "años, vive en ",
        datos.get("direccion"), "y su número de teléfono es ",
        datos.get("telefono")
        )
# datos()

#Ejercicio 3
"""
Escribir un programa que guarde en un diccionario los precios de las frutas de la tabla.
Preguntar al usuario por una fruta, un número de kilos y muestre por pantalla el precio de ese número de kilos de fruta.
Si la fruta no está en el diccionario debe mostrar un mensaje informando de ello.
    Fruta	    Precio
    banana	    1.35
    Manzana	    0.80
    Pera	    0.85
    Naranja	    0.70
"""
def frutas():
    frutas = {
        "plátano":	    "1.35",
        "manzana":	    "0.80",
        "pera":	        "0.85",
        "naranja":	    "0.70",
    }
    a=input("escriba el nombre de una fruta ")
    frutas_keys = frutas.keys()
    frutas_values = frutas.values()
    if a in frutas_keys:
        print("El precio por kilo de la", a, "es", frutas[a])
        b=int(input("escriba el peso "))
        kilos = (b*frutas[a])
        print(kilos)    
    else:
        print("no existe esa fruta en el diccionario")
   
    


# frutas()

#Ejercicio 4

"""
Escribir un programa que guarde en un diccionario los precios de las frutas de la tabla.
Preguntar al usuario por una fruta, un número de kilos y muestre por pantalla el precio de ese número de kilos de fruta.
Si la fruta no está en el diccionario debe mostrar un mensaje informando de ello.
    Fruta	    Precio
    Plátano	    1.35
    Manzana	    0.80
    Pera	    0.85
    Naranja	    0.70
"""

def mes():
    int(input("escriba el peso "))
    if mes == 1
        print("enero")
    elif mes == 2
        print("febrero")
    elif mes == 3 
        print(marzo)

mes()


#Ejercicio 5
"""
Escribir un programa que almacene el diccionario con los créditos de las asignaturas de un curso 
{'Matemáticas': 6, 'Física': 4, 'Química': 5} 
Después muestre por pantalla los créditos de cada asignatura en el formato <asignatura> tiene <créditos> créditos, 
donde <asignatura> es cada una de las asignaturas del curso, y <créditos> son sus créditos. 
Al final debe mostrar también el número total de créditos del curso.
"""

