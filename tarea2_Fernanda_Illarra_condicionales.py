#Ejercicio1

edad = int(input('Ingrese su edad: '))

if edad >= 18 : 
    print('Usted es mayor de edad')
else:
    print('Usted es menor de edad')


 #Ejercicio2
        
password = '010797fer'

newpass = input('Ingrese contraseña: ')

if password == newpass :
    print('Contraseña correcta')

else:
    print('ERROR: Contraseña incorrecta')    



#Ejercicio3

num1 = int(input('Ingrese un número: '))
num2 = int(input('Ingrese otro número: '))



if num2 == 0 : 
    print('ERROR : EL NÚMERO NO PUEDE SER CERO')
else:
    resultado = num1 // num2
    print(f'El resultado de la division entre los dos numeros es: {resultado}')   



#Ejercicio4

num_1 = int(input('Ingrese un número: '))

if num_1 % 2 == 0 : 
    print('El número ingresado es par')
else: 
    print('El número ingresado es impar')    


#Ejercicio5

name = input('Ingrese su nombre: ')
sexo = input('Ingrese su sexo F (femenino) o M (masculino) : ')

if (name < 'H' and sexo.upper() == 'F') or (name > 'M' and sexo.upper() == 'M'):
    print('Perteneces al grupo A')
else:
    print('Sos del grupo B')

     
#Ejercicio6

age = int(input('Ingrese su edad: '))

if age < 4 :
    print('Entras gratis')

elif age >= 4 and age < 18: 
    print('Debes pagar $400')

else:     
    print('Debes pagar $900')



#Ejercicio7

print('Bienvenido a la pizzeria Bella Napoli.')
tipo_pizza = (input('Tipos de Pizza:  \n 1 - Vegetariana. \n 2 - No vegetariana \n Ingrese la opcion deseada: '))
ingredientes =  ('Muzzarela, tomate')
ingrediente =''

if(tipo_pizza == '1'):
    tipo_pizza = ('Vegetariana')
    ingrediente = input('Elija un Extra para agregarle a la pizza: \n 1 - Pimiento \n 2 - Tofu \n')
    if(ingrediente == 1):
        ingrediente = ('Pimiento')
    elif(ingrediente == 2):
        ingrediente = ('Tofu')
    else:
        print('No ingreso una opcion valida. Error!')
elif(tipo_pizza =='2'):
    tipo_pizza = ('No Vegetariana')
    ingrediente = (input('Elija un Extra para agregarle a la pizza: \n 1 - Peperoni \n 2 - Jamón \n 3- Salmon \n'))
    if(ingrediente == 1):
        ingrediente = ('Peperoni')
    elif(ingrediente == 2):
        ingrediente = ('Jamón')
    elif(ingrediente == 3):
        ingrediente = ('Salmón')
    else:
        print('No ingreso una opcion valida. Error!')
print(f'Pizza {tipo_pizza} con {ingredientes} y {ingrediente}.')



#Ejercicio8

anio = int(input('Ingrese un año: '))

if (anio % 4 == 0 and anio % 100 != 0) or anio % 400 == 0:
    print('Es un año bisiesto.')
else:
    print('No es un año bisiesto')



#Ejercicio9

print('PIEDRA-PAPEL-TIJERA')
print('*'*20)
persona1 = int(input('Jugador 1\n1-Piedra\n2-Papel\n3-Tijera\nElija lo que quiera:'))
persona2 = int(input('Jugador 2\n1-Piedra\n2-Papel\n3-Tijera\nElija lo que quiera:'))

if persona1  == 1 and persona2 == 3:
    resultado = 'Gana Jugador 1: La piedra rompe la tijera'
elif persona1 == 2 and persona2 == 1:
    resultado = 'Gana Jugador 1: El papel envuelve a la piedra'
elif persona1  == 3 and persona2 == 2:
    resultado = 'Gana Jugador 1: La tijera corta al papel'
elif persona2 == 1 and persona1  == 3:
    resultado = 'Gana Jugador 2: La piedra rompe la tijera'
elif persona2 == 2 and persona1  == 1:
    resultado = 'Gana Jugador 2: El papel envuelve a la piedra'
elif persona2 == 3 and persona1  == 2:
    resultado = 'Gana Jugador 2: La tijera corta al papel'
else:
    resultado = 'Empate!' 
    
print(resultado)



#Ejercicio10

n1 = int(input('Ingrese un número: '))
n2 = int(input('Ingrese otro número: '))
n3 = int(input('Ingrese otro número: '))

prom = round(((n1 + n2 + n3) / 3),2)
maxi = max(n1,n2,n3)
mini = min(n1,n2,n3)
 
print(f'Max = {maxi}, Min = {mini}, Prom = {prom}')



#Ejercicio11

print('Ingrese los siguientes datos: ')
age1 = int(input('Ingrese su edad: '))
peso = int(input('Ingrese su peso: '))
pulso = int(input('Ingrese su pulso: '))
tension_baja = int(input('Ingrese su tensión baja: '))
tension_alta = int(input('Ingrese su tensión alta:'))
plaquetas = int(input('Ingrese su plaquetas: '))

if (age1 >= 18 and age1 <= 65) and (peso >= 50) and (pulso >= 60 and pulso <= 100) and (tension_baja >= 80) and (tension_alta <= 120) and (plaquetas >= 150000):
    print('Apto para donar sangre')
else:
    print('No puede donar')            