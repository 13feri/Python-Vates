# EJERCICIO1 
'''
area_circulo = lambda radio: 3.14159 * radio**2

radio = float(input("Ingrese el radio del círculo: "))

area = area_circulo(radio)
print("El área del círculo es:", area)

#Ejercicio2 

# Lista original de números enteros
numeros = []
longitud_lista = int(input('Ingrese la longitud de la lista: '))

for i in range(1, longitud_lista + 1):
    numeros.append(int(input('Ingrese un valor: ')))

# Utilizar la función map y una función lambda para filtrar los números pares
numeros_pares = list(map(lambda x: x if x % 2 == 0 else None, numeros))
numeros_pares = list(filter(None, numeros_pares))

print(f'Lista original: {numeros}')
print(f"Números pares: {numeros_pares}")


#Ejercicio3

tuplas = [(3, 5), (6, 2), (9, 7), (4, 1), (8, 6), (7, 3)]

tuplas_ordenadas = sorted(tuplas, key=lambda x: x[1])

print(f"Lista de tuplas ordenadas: {tuplas_ordenadas}")

'''

#Ejercicio4

personas = {'Miguel': 20, 'Norma': 25, 'Elizabeth': 19, 'Esteban': 31, 'Jorge': 21}

nuevo_diccionario = {nombre: edad + 1 for nombre, edad in personas.items()}

print(f'Lista original: {personas}')
print(f'Lista con edades incrementadas: {nuevo_diccionario}')
