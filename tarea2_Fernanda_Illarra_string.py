#Ejercicio1 

nombre = input('Ingrese su nombre: ')
num = int(input('Ingrese un número: '))

res = (nombre + '\n') * num
print(res)


#Ejercicio2

name = input('Ingrese su nombre: ')
surname = input('Ingrese su Apellido: ')

print(f"{surname}, {name} ")


#Ejercicio3

ruta = input('Ingrese su ruta samba: ')

ruta1 = ruta[2:]
indexx = ruta1.index('/')

host = ruta1[:indexx]
path = ruta1[indexx:]

print(f'host = {host}; path = {path}')




#Ejercicio4


correo = input('Ingrese su mail: ')

partes = correo.split('@')
name = partes[0]
dominio = partes[1]

correo2 = name + '@educ.ar'

print(f'Nuevo correo electronico: {correo2}')


#Ejercicio5

nif = input('Ingrese 8 digitos de su NIF: ')

validar = len(nif) == 8 
letras_nif = 'TRWAGMYFPDXBNJZSQVHLCKE'
posicion = int(nif) % 23
digito_control = letras_nif[posicion] * validar

nif_completo = nif + digito_control
print(f'El NIF completo es: {nif_completo}')




#Ejercicio6

num1 = int(input('Ingrese un número: '))

num2 = int(str(num1) + str(num1))
num3 = int(str(num2) + str(num1))

res_ = num1 + num2 + num3

print(f'El resultado es : {res_}')



#Ejercicio7

fecha_nacimiento = input('Ingrese su fecha de nacimiento en formato dd/mm/aaaa:')

dia, mes, anio = fecha_nacimiento.split('/')

dia = dia.zfill(2)
mes = mes.zfill(2)

print(f'Día: {dia}')
print(f'Mes: {mes}')
print(f'Año: {anio}')



#Ejercicio8

nombre_produc = input('Ingrese el nombre del producto: ')
cantidad = int(input('Ingrese el número de unidades: '))
precio = float(input('Ingrese el precio del producto: '))
 
coste_total = precio * cantidad

cadena = f'Nombre del producto: {nombre_produc}\n'
cadena += f'Precio del producto: {precio}\n'
cadena += f'Número de unidades: {cantidad}\n'
cadena += f'Costo total: {coste_total:8.2f}'

print(cadena)



#Ejercicio9

productos = input("Ingrese los productos de la compra (cantidad:producto, separados por comas): ")

print('\n'.join(map(str.strip, productos.replace(':', ' ').split(','))))



#Ejercicio10

palabra = input('Ingrese una palabra: ')

vocales = palabra.count('a') + palabra.count('e') + palabra.count('i') + palabra.count('o') + palabra.count('u')

res2 = len(palabra) * vocales

print(res2)
