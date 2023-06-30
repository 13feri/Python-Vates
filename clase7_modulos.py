import random
import math


#EJERCICIO1
def tirar_dados():
    dado1 = random.randint(1, 6)
    dado2 = random.randint(1, 6)
    return dado1,dado2


while True:
    print("SIMULADOR DE TIRADA DE DADOS")
    print("=" * 28)

    print("1 - Tirar dados")

    print("2 - Salir")

    opcion = input('Seleccione una opción (1-2): ')

    if opcion == '2':
        print('¡Hasta pronto!')
        break



    if opcion != '1':
        print('Opción inválida! Por favor, seleccione una opción válida.')
        continue


    dado1,dado2 = tirar_dados()
    print(f'Tirada -> {dado1} - {dado2}')

    print()

#Ejercicio 2

hip = float(input('Ingrese la hipotenusa:'))
ang = math.radians(float(input('Ingrese el angulo: ')))

cate_ad =  hip * math.cos(ang)
cate_op = hip * math.sin(ang)

print(f'El cateto adyacente es : {cate_ad: .2f} y el cateto opuesto es : {cate_op: .2f}')