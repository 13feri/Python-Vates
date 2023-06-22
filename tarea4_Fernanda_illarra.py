# Ejercicio 1

mul = int(input("Ingrese un número: "))

for num in range(mul):
    contador = num * 5

    if contador > mul:
        break
    print(contador)


# Ejercicio 2

numero = int(input("Ingrese un número: "))

if numero < 2:
    print("No es primo")
else:
    es_primo = True
    for divisor in range(2, numero):
        if numero % divisor == 0:
            es_primo = False
            break
    if es_primo or numero == 2:
        print("Es primo")
    else:
        print("No es primo")

# Ejercicio 3


valor = int(input("Ingresa un número: "))

suma = 0


for num in range(valor):
    contador = num * 3
    suma += contador

    if suma > valor:
        break

    print(contador)


# Ejercicio 4


for i in range(1, 10):
    num = int("1" * i)
    result = num * num
    print(f"{num} * {num} = {result}")


# Ejercicio5

str1 = input("Ingrese la primera cadena de texto: ")
str2 = input("Ingrese la segunda cadena de texto: ")

cartesian_product = [f"{c1}{c2}" for c1 in str1 for c2 in str2]

print("Producto cartesiano letra a letra:")
print(" ".join(cartesian_product))


# Ejercicio6

x = int(input("X:"))
y = int(input("Y:"))

while x <= 8 and y <= 8:
    print(f"({x}, {y})")
    x += 2
    y += 1
    if x <= 8 and y <= 8:
        print(f"({x}, {y})")
        x += 1
        y += 2


# Ejercicio7


cadena1 = input("Ingrese la primera cadena de texto: ")
cadena2 = input("Ingrese la segunda cadena de texto: ")

contador = 0
hamming = 0


if len(cadena1) != len(cadena2):
    print("Las cadenas no tienen la misma longitud")
else:
    for caracter in cadena1:
        if caracter != cadena2[contador]:
            hamming = hamming + 1

        contador = contador + 1

    print(f"La distancia de Hamming entre las cadenas es: {hamming}")


# Ejercicio8

a = int(input("Primer número: "))
b = int(input("Segundo número: "))
divisor = min(a, b)
for i in range(1, divisor + 1):
    if a % i == 0 and b % i == 0:
        mcd = i
print(mcd)

# Ejercicio9


min_value = 1e10
min_x = 0

# Evaluar la función para cada valor entero en el rango [-9, 9]
for x in range(-9, 10):
    result = x**2 - 6 * x + 3
    if result < min_value:
        min_value = result
        min_x = x

print(f"El resultado es: x = {min_x} y f({min_x}) = {min_value}")

# Ejercicio 10

contador = 0

for num in range(33, 128):
    letra = chr(num)
    print(f"{num} {letra}", end="   ")

    if contador == 5:
        print("\n")
        contador = 0


# Ejercicio11
for i in range(6):
    for j in range(10):
        if i == 0 or i == 5 or j == 0 or j == 9:
            print("0", end="")
        elif i == 1 or i == 4 or j == 1 or j == 8:
            print("1", end="")
        else:
            print("2", end="")
    print()


# Ejercicio12

num = int(input("Ingrese un número entre 0 y 100: "))
intentos = 0

while True:
    intentos += 1
    num2 = int(input("Introduzca un número: "))

    if num2 < num:
        print("Mayor")
    elif num2 > num:
        print("Menor")
    else:
        print(f"Correcto! Has encontrado el número en {intentos} intentos")
        break
