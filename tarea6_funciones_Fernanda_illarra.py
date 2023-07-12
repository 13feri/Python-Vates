# Clase 6
# Funciones

# Ejercicio 1: Escribir una función a la que se le pase una cadena <nombre> y muestre por pantalla el saludo ¡Hola <nombre>!.


def saludar(nombre):
    print(f"Hola {nombre}")


saludar(input("Ingrese el nombre a saludar: "))

# Ejercicio 2: Escribir una función que reciba un número entero positivo y devuelva su factorial.


def factorial():
    resultado = 1
    numero = int(input("Ingrese un numero: "))
    for i in range(1, numero + 1):
        resultado *= i
    return print(resultado)


factorial()


# Ejercicio 3: Escriba una función en Python que reciba una lista de valores enteros y devuelva otra lista sólo con aquellos valores pares.


def filtrar_lista_par():
    cantidad = int(input("Ingrese la cantidad de numeros a ingresar: "))
    list1 = []
    for i in range(1, cantidad + 1):
        list1.append(int(input("Ingrese un valor: ")))
    list2 = []

    for i in list1:
        if i % 2 == 0:
            list2.append(i)
        else:
            continue
    return print(list2)


filtrar_lista_par()


# Ejercicio 4: Escribir una función que reciba una lista de números y devuelva su promedio.


def promedio():
    cantidad = int(input("Ingrese la cantidad de numeros a ingresar: "))
    list1 = []
    promedio = 0
    suma = 0

    for i in range(1, cantidad + 1):
        list1.append(int(input("Ingrese un valor: ")))

    for i in list1:
        suma += i
    promedio = round(suma / len(list1), 2)
    return print(promedio)


promedio()


# Ejercicio 5: Escribir una función que calcule el área de un círculo y otra que calcule el volumen de un cilindro usando la primera función.

import math


def area_circulo(radio):
    pi = math.pi
    area = pi * (radio**2)
    return area


def area_cilindro(radio, altura):
    volumen = area_circulo(radio) * altura
    return volumen


radio = int(input("Ingrese el radio: "))
area = area_circulo(radio)
print(f"El area del circulo es {area:.2f}")
altura = int(input("Ingrese la altura: "))
volumen = area_cilindro(radio, altura)
print(f"El volumen del cilindro es {volumen: .2f}")


# print(area_circulo(int(input("Ingrese el radio: "))))
# print(
#   area_cilindro(int(input("Ingrese el radio: ")), int(input("Ingrese la altura: ")))
# )


# Ejercicio 6:
# Escribir un programa que reciba una cadena de texto y devuelva un diccionario con cada palabra que contiene
# (usar como clave cada una de las palabra) y su frecuencia (frecuencia: la cantidad de veces que aparece la palabra en la cadena).


def cadxdic(cad_text):
    palabras = cad_text.replace(",", "").replace(".", "").split()
    diccionario = {}

    for palabra in palabras:
        if palabra in diccionario:
            diccionario[palabra] += 1

        else:
            diccionario[palabra] = 1

    return diccionario


cadena = str(input("Ingrese una cadena de texto: "))
diccionario = cadxdic(cadena)
print(diccionario)


# Ejercicio 7


def tupladic(diccionario):
    palabra_repetida = ""
    frecuencia_max = 0

    for palabra, frecuencia in diccionario.items():
        if frecuencia > frecuencia_max:
            palabra_repetida = palabra
            frecuencia_max = frecuencia

        return palabra_repetida, frecuencia_max


tupla = tupladic(diccionario)
print(tupla)


# Ejercico 8


def aplicar_funcion(funcion, lista):
    resultados = []

    for elemento in lista:
        resultado = funcion(elemento)
        resultados.append(resultado)
    return resultados


def mas_dos(numero):
    return numero + 2


lista = [2, 3, 6, 5, 0]
print(f"Lista original: {lista}")
res = aplicar_funcion(mas_dos, lista)
print(f"Lista con funcion: {res}")


# Ejercicio 9


def palabras_comunes(oracion1, oracion2):
    palabras1 = oracion1.split()
    palabras2 = oracion2.split()

    palabras_comunes = []

    for palabra in palabras1:
        if palabra in palabras2 and palabra not in palabras_comunes:
            palabras_comunes.append(palabra)

    return palabras_comunes


oracion1 = input("Ingrese una oración: ")
oracion2 = input("Ingrese otra oración: ")
palabras = palabras_comunes(oracion1, oracion2)


print(palabras)


# Ejercicio 10


def buscar_inmuebles_por_presupuesto(inmuebles, presupuesto):
    inmuebles_en_presupuesto = []

    for inmueble in inmuebles:
        zona = inmueble["zona"]
        metros = inmueble["metros"]
        habitaciones = inmueble["habitaciones"]
        garaje = inmueble["garaje"]
        antiguedad = 2023 - inmueble["año"]

        if zona == "A":
            precio = (metros * 1000 + habitaciones * 5000 + garaje * 15000) * (
                1 - (antiguedad / 100)
            )
        elif zona == "B":
            precio = (
                (metros * 1000 + habitaciones * 5000 + garaje * 15000)
                * (1 - (antiguedad / 100))
                * 1.5
            )

        inmueble["precio"] = precio

        if precio <= presupuesto:
            inmuebles_en_presupuesto.append(inmueble)

    return inmuebles_en_presupuesto


inmuebles = [
    {"año": 2000, "metros": 100, "habitaciones": 3, "garaje": True, "zona": "A"},
    {"año": 2012, "metros": 60, "habitaciones": 2, "garaje": True, "zona": "B"},
    {"año": 1980, "metros": 120, "habitaciones": 4, "garaje": False, "zona": "A"},
    {"año": 2005, "metros": 75, "habitaciones": 3, "garaje": True, "zona": "B"},
    {"año": 2015, "metros": 90, "habitaciones": 2, "garaje": False, "zona": "A"},
]

presupuesto = 100000
inmuebles_en_presupuesto = buscar_inmuebles_por_presupuesto(inmuebles, presupuesto)
for inmueble in inmuebles_en_presupuesto:
    print(inmueble)
