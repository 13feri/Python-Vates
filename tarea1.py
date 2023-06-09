#Tarea 1 
#Ejercicio 1



nombre = str(input("Introduzca su nombre")) 
edad = int(input("Introduzca su edad"))
print(f"Hola, {nombre}. Tienes {edad} años.")

#Ejercicio 2 

num1 = int(input("Introduzca un numero "))
print(f"El numero es:{num1} y es de tipo:{type(num1)}" )
num2 = int(input("Introduzca otro numero "))
print(f"El numero es:{num2} y es de tipo:{type(num2)}" )



#Ejercicio3 

nume1 = (input("Introduzca un numero "))
nume1 = float(nume1)
print(f"El numero es: {nume1} y es de tipo: {type(nume1)}" )


#Ejercicio4
numero1 = int(input("Introduzca un numero "))
numero2 = int(input("Introduzca un numero "))
suma = numero1 + numero2
resta = numero1 - numero2
multipli = numero1 * numero2
division = numero1 / numero2
diviE = numero1 // numero2
modu = numero1 % numero2
pote = numero1 ** numero2

print(f"El resultado entre los numeros es suma: {suma}, la resta: {resta}, multiplicacion: {multipli}, division: {division}, division entera {diviE}, modulo: {modu} y potencia {pote}  ")



#Ejercicio5

numero_ = int(input("Introduzca un numero "))
raiz = numero_ ** 0.5
print(f"La raiz cuadrada de {numero_} es: {raiz}")



#Ejercicio6

numeroaca_ = int(input("Introduzca un numero "))
mod_ = numeroaca_ % 2 
print("Si el modulo es 0 el numero es par y si es uno es impar")
print(f"El modulo de {numeroaca_} es {mod_}")



#Ejercicio7
peso = float(input("Introduzca su peso en kg "))
altura = float(input("Introduzca su altura en metro "))
imc = peso / (altura ** 2)
print(f"Su indice de masa corporal es: {imc}")



#Ejercicio8
base = float(input("Introduzca la medida de base de un triangulo: "))
alturat = float(input("Introduzca la medida de altura de un triangulo: "))
superficie = (base * alturat)/2
print(f"La superficie del triangulo es: {superficie}")


#Ejercicio9

cant_inver = float(input("Ingrese el numero a invertir: "))
inte_anual = float(input("Ingrese el interes anual: "))
cant_año = int(input("Ingrese los años que desea invertir: "))

cap_obt = cant_inver * (1 + (inte_anual/100) ) ** cant_año
print(f"El capital obtenido es: ${cap_obt}")



#Ejercicio 10
pesopayaso = 250
pesomunieca = 120
cant_munieca = int(input("Ingrese cantidad de muñecas vendidas: ")) 
cant_payasos = int(input("Ingrese cantidad de payasos vendidas: "))

pesototal = (((pesopayaso * cant_payasos) + (pesomunieca * cant_munieca)))/1000

print(f"El peso total del paquete es: {pesototal}kg")



#Ejercicio 11 
a = float(input("Ingrese el valor de a: "))
b = float(input("ingrese el valor de b: "))
c = float(input("ingrese el valor de c: "))

x1 = (-b + (((b**2)-(4*a*c))**(1/2)))/(2*a)
x2 = (-b - (((b**2)-(4*a*c))**(1/2)))/(2*a)

print(f"Las raices son x1 = {x1} y x2 = {x2}")



#Ejercicio12

resultado1 = a * x1**2 + b * x1 + c
print(f" El resultado con la primera raiz es:{resultado1}")
resultado2 = a * x2**2 + b * x2 + c
print(f" El resultado con la segunda raiz es:{resultado2}")

print("Si los resultados son cero entonces las raices son correctas")


#Ejercicio13

entero = int(input("Ingrese un numero entero: "))
float = float(input("Ingrese un numero flotante: "))
booleano = bool(input("Ingrese true o flase: "))
print(f"El valor es: {entero}, su tipo es {type(entero)} y su identificacion en memoria es {id(entero)}")
print(f"El valor es: {float}, su tipo es {type(float)} y su identificacion en memoria es {id(float)}")
print(f"El valor es: {booleano}, su tipo es {type(booleano)} y su identificacion en memoria es {id(booleano)}")


#Ejercicio14

valor1 = int(4.5)
print(f"El valor es: {valor1}, su tipo es {type(valor1)}")

valor2 = bool(4.5)
print(f"El valor es: {valor2}, su tipo es {type(valor2)}")

valor3 = int(True)
print(f"El valor es: {valor3}, su tipo es {type(valor3)}")

valor4 = float(True)
print(f"El valor es: {valor4}, su tipo es {type(valor4)}")

valor5 = float(6)
print(f"El valor es: {valor5}, su tipo es {type(valor5)}")

valor7 = bool(6)
print(f"El valor es: {valor7}, su tipo es {type(valor7)}")