# EJERCICIO1

area_circulo = lambda radio: 3.14159 * radio**2

radio = float(input("Ingrese el radio del círculo: "))

area = area_circulo(radio)
print("El área del círculo es:", area)

# Ejercicio2

# Lista original de números enteros
numeros = []
longitud_lista = int(input("Ingrese la longitud de la lista: "))

for i in range(1, longitud_lista + 1):
    numeros.append(int(input("Ingrese un valor: ")))

# Utilizar la función map y una función lambda para filtrar los números pares
numeros_pares = list(map(lambda x: x if x % 2 == 0 else None, numeros))
numeros_pares = list(filter(None, numeros_pares))

print(f"Lista original: {numeros}")
print(f"Números pares: {numeros_pares}")


# Ejercicio3

tuplas = [(3, 5), (6, 2), (9, 7), (4, 1), (8, 6), (7, 3)]

tuplas_ordenadas = sorted(tuplas, key=lambda x: x[1])

print(f"Lista de tuplas ordenadas: {tuplas_ordenadas}")


# Ejercicio4

personas = {"Miguel": 20, "Norma": 25, "Elizabeth": 19, "Esteban": 31, "Jorge": 21}

nuevo_diccionario = {nombre: edad + 1 for nombre, edad in personas.items()}

print(f"Lista original: {personas}")
print(f"Lista con edades incrementadas: {nuevo_diccionario}")


# Ejercicio5

suma = lambda a, b: a + b
resta = lambda a, b: a - b
multiplicacion = lambda a, b: a * b
division = lambda a, b: a / b

while True:
    print("BIENVENIDA A LA CALCULADORA")
    print("*" * 30)

    print(" 1 - SUMA")
    print(" 2 - RESTA")
    print(" 3 - MULTIPLICACION")
    print(" 4 - DIVISION")
    print(" 5 - SALIR")

    opcion = input("Seleccione una operacion (1 al 5): ")

    if opcion == "5":
        print(" BYE, HASTA LUEGO")
        break

    if opcion not in ["1", "2", "3", "4"]:
        print("ERROR! OPCION INVÁLIDA. Por favor seleccione una operación válida.")
        continue

    num_1 = float(input("Ingrese el primer número:"))
    num_2 = float(input("Ingrese el segundo número:"))

    if opcion == "1":
        resultado = suma(num_1, num_2)
        print(f"El resultado de la suma es: {resultado}")

    elif opcion == "2":
        resultado = resta(num_1, num_2)
        print(f"El resultado de la resta es: {resultado}")

    elif opcion == "3":
        resultado = multiplicacion(num_1, num_2)
        print(f"El resultado de la multiplicacion es: {resultado}")

    elif opcion == "4":
        if num_2 == 0:
            print("ERROR, NO SE PUEDE DIVIDIR POR CERO")
        else:
            resultado = division(num_1, num_2)
            print(f"El resultado de la division es: {resultado}")

print()
