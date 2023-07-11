import math

# Ejercicio 1


class Estudiante:
    def __init__(self, nombre) -> None:
        self.nombre = nombre

    def get_nombre(self):
        impresion = print(f"Hola {self.nombre} como estas")
        return impresion


fer = Estudiante("Fer")

fer.get_nombre()

# Ejercicio 2


class Rectangulo:
    def __init__(self, largo, ancho) -> None:
        self.largo = largo
        self.ancho = ancho

    def area(self):
        area = self.largo * self.ancho
        return area


rect1 = Rectangulo(5, 10)
area = rect1.area()
print(f"El area del rectangulo es: {area}")


# Ejercicio 3


class Circulo:
    def __init__(self) -> None:
        pass

    def set_radio(self):
        radio = int(input("Ingrese el radio del circulo: "))
        self.radio = radio

    def get_area(self):
        area = math.pi * self.radio**2
        return area


cir1 = Circulo()

cir1.set_radio()
area = cir1.get_area()
print(f"El area del circulo es: {area}")


# Ejercicio 4


class Compras:
    lista = list()

    def __init__(self) -> None:
        pass

    def add_item(self, item):
        self.lista.append(item)

    def del_item(self, item):
        if item in self.lista:
            self.lista.remove(item)
        else:
            print(f"El elemento: {item} no existe.")

    def get_lista(self):
        return self.lista


shop = Compras()

while True:
    print("*" * 40)
    print("*** BIENVENIDA A LA LISTA DE COMPRAS ***")
    print("*" * 40)
    print("1 - Agregar Item a la lista de compras.")
    print("2 - Eliminar Item de la lista de compras.")
    print("3 - Imprimir lista de compras.")
    print("4 - Salir.")

    opcion = str(input("Ingrese una opción: "))

    if opcion == "4":
        print("Gracias por utilizar Lista de Compras. Vuelvan pronto")
        break

    if opcion == "1":
        item = input("Ingrese el item que desea agregar: ")
        shop.add_item(item)
        print(f"El item: {item}  se agrego correctamente.")

    elif opcion == "2":
        item = input("Ingrese el item que desea eliminar: ")
        shop.del_item(item)
        print(f"El item: {item} se agrego correctamente.")

    elif opcion == "3":
        lista = shop.get_lista()
        print("La lista contiene los siguientes items: ")
        for item in lista:
            print(f"- {item}")
    else:
        print("Ingrese una opcion valida.")
        continue


# Ejercicio 5
class Stock:
    def __init__(self) -> None:
        self.stock = {}

    def añadir_item(self, clave: str, cantidad: int):
        self.stock[clave] = cantidad

    def borrar_item(self, clave):
        if clave in self.stock.keys():
            del self.stock[clave]
        else:
            print(f"No se encontró clave con el nombre de: {clave} ")

    def devolver_stock(self):
        return self.stock


stock5 = Stock()

while True:
    print("*" * 20)
    print("** LISTA DE STOCK **")
    print("*" * 20)
    print("1 - Agregar Item a la lista de stock.")
    print("2 - Eliminar Item de la lista de stock.")
    print("3 - Devolver stock.")
    print("4 - Salir.")

    opcion = str(input("Ingrese una opción: "))

    if opcion == "4":
        print("Gracias por utilizar Lista de Compras. Vuelvan pronto")
        break

    if opcion == "1":
        item = input("Ingrese el item que desea agregar: ")
        cantidad = int(input("Ingrese la cantidad del item: "))
        stock5.añadir_item(item, cantidad)
        print(f"El item: {item}  se agrego correctamente.")

    elif opcion == "2":
        item = input("Ingrese el item que desea eliminar: ")
        stock5.borrar_item(item)
        print(f"El item: {item} se agrego correctamente.")

    elif opcion == "3":
        diccionario = stock5.devolver_stock()
        print("La lista contiene los siguientes items: ")
        for item, valor in diccionario.items():
            print(f"- {item}: {valor} unidades.")
    else:
        print("Ingrese una opcion valida.")
        continue

# Ejercicio 6


class Automovil:
    marca = str
    modelo = str
    year = int
    odometro = float(0)

    def __init__(self, marca, modelo, year) -> None:
        self.marca = marca
        self.modelo = modelo
        self.year = year

    def add_kms(self, kms):
        self.odometro += kms


auto1 = Automovil("Ford", "EcoSport", 2022)
auto2 = Automovil("volkswagen", "Gol Trend", 2020)


for i in range(1, 11):
    auto1.add_kms(10)
    auto2.add_kms(20)


print(f"Odometro del Auto {auto1.modelo}: {auto1.odometro} km/h")
print(f"Odometro del Auto {auto2.modelo} {auto2.odometro} km/h")


# Ejercicio 7


class Billetera:
    saldo = float
    movimientos = []

    def __init__(self) -> None:
        self.saldo = 0

    def add_mov_entrada(self, monto):
        self.saldo += monto
        self.movimientos.append(monto)

    def add_mov_salida(self, monto):
        self.saldo -= monto
        self.movimientos.append(-monto)

    def get_movimientos(self):
        return self.movimientos


billetera_virtual = Billetera()

while True:
    print("*" * 40)
    print("*** BIENVENIDA A LA BILLETERA VIRTUAL***")
    print("*" * 40)
    print("1 - Añadir plata a la billetera")
    print("2 - Sacar plata de la billetera")
    print("3 - Mostrar los movimientos")
    print("4 - Salir.")

    opcion = str(input("Ingrese una opción: "))

    if opcion == "4":
        print("Gracias por utilizar Billetera Virtual. Vuelvan pronto")
        break

    if opcion == "1":
        item = int(input("Ingrese el monto a añadir: "))

        billetera_virtual.add_mov_entrada(item)
        print(f"Se agrego ${item}  en la billetera.")

    elif opcion == "2":
        item = int(input("Ingrese el monto a retirar: "))
        billetera_virtual.add_mov_salida(item)
        print(f"Se retiro ${item} de la billetera.")

    elif opcion == "3":
        mov = billetera_virtual.get_movimientos()
        print("Los movimientos de la billetera virtual son: ")
        for item in mov:
            print(f"** {item}")
        print("-" * 30)
        print(f"El saldo total es de: ${billetera_virtual.saldo}")
        print("-" * 30)
    else:
        print("Ingrese una opcion valida.")
        continue

    print()

# Ejercicio8


class Persona:
    nombre = str
    apellido = str
    billetera = Billetera()

    def _init_(self, nombre: str, apellido: str) -> None:
        self.nombre = nombre
        self.apellido = apellido

    def inc_saldo(self, saldo: float):
        self.billetera.add_mov_entrada(saldo)

    def dec_saldo(self, saldo: float):
        self.billetera.add_mov_salida(saldo)

    def get_saldo(self):
        return self.billetera.saldo


personita = Persona("Fernanda", "Illarra")

personita.inc_saldo(10)
personita.inc_saldo(20)
personita.inc_saldo(30)
personita.dec_saldo(15)
personita.inc_saldo(5)

saldo = personita.get_saldo()
print(f"El saldo de la persona: {personita.nombre} {personita.apellido} es ${saldo}")


# Ejercicio9


class Libreta:
    def __init__(self, nombre, curso):
        self.nombre = nombre
        self.curso = curso
        self.notas = {"Matemática": 0, "Lengua": 0, "Física": 0}

    def set_nota(self, materia, nota):
        if materia in self.notas:
            self.notas[materia] = nota
        else:
            print(f'La materia "{materia}" no existe en la libreta.')

    def get_promedio(self):
        total = sum(self.notas.values())
        cantidad = len(self.notas)
        promedio = total / cantidad
        return promedio


libreta1 = Libreta("Fernanda", "6to Año")

while True:
    print("*" * 32)
    print("** LIBRETA DE CALIFICACIONES **")
    print("*" * 32)
    print("1 - Agregar materias y notas.")
    print("2 - Visualizar promedio.")
    print("4 - Salir.")

    opcion = str(input("Ingrese una opción: "))

    if opcion == "4":
        print("A salido de la Libreta de Calificaciones")
        break

    if opcion == "1":
        materia = input(
            "Ingrese el nombre de la materia (Matemática, Lengua o Fisica): "
        )
        nota = int(input(f"Ingrese la nota de {materia}: "))
        libreta1.set_nota(materia, nota)
        print(f"La materia {materia} con {nota}  se agrego correctamente.")

    elif opcion == "2":
        promedio = libreta1.get_promedio()
        print(f"El promedio total de las materias es : {promedio}")


class Persona:
    def __init__(self, nombre, telefono, email):
        self.nombre = nombre
        self.telefono = telefono
        self.email = email


class Agenda:
    def __init__(self):
        self.contactos = []

    def añadir_contacto(self, nombre, telefono, email):
        for contacto in self.contactos:
            if contacto.nombre == nombre:
                print("Error!! El contacto ya existe.")
                return

        nuevo_contacto = Persona(nombre, telefono, email)
        self.contactos.append(nuevo_contacto)
        print("Contacto añadido correctamente.")

    def lista_contactos(self):
        print("Lista de contactos:")
        for contacto in self.contactos:
            print(f"Nombre: {contacto.nombre}")
            print(f"Teléfono: {contacto.telefono}")
            print(f"Email: {contacto.email}")
            print()

    def buscar_contacto(self, nombre):
        for contacto in self.contactos:
            if contacto.nombre == nombre:
                print("Datos del contacto:")
                print(f"Nombre: {contacto.nombre}")
                print(f"Teléfono: {contacto.telefono}")
                print(f"Email: {contacto.email}")
                return

        print("No se encontró ningún contacto con ese nombre.")

    def editar_contacto(self, nombre):
        for contacto in self.contactos:
            if contacto.nombre == nombre:
                nuevo_nombre = input("Ingrese el nuevo nombre: ")
                nuevo_telefono = input("Ingrese el nuevo teléfono: ")
                nuevo_email = input("Ingrese el nuevo email: ")

                contacto.nombre = nuevo_nombre
                contacto.telefono = nuevo_telefono
                contacto.email = nuevo_email

                print("Contacto editado con éxito.")
                return

        print("No se encontró ningún contacto con ese nombre.")


def mostrar_menu():
    print("*" * 13)
    print("** AGENDA **")
    print("*" * 13)
    print("1 - Añadir contacto")
    print("2 - Lista de contactos")
    print("3 - Buscar contacto")
    print("4 - Editar contacto")
    print("5 - Salir")
    opcion = input("Ingrese una opción: ")
    return opcion


agenda = Agenda()

while True:
    opcion = mostrar_menu()

    if opcion == "1":
        nombre = input("Ingrese el nombre del contacto: ")
        telefono = input("Ingrese el teléfono del contacto: ")
        email = input("Ingrese el email del contacto: ")
        agenda.añadir_contacto(nombre, telefono, email)
    elif opcion == "2":
        agenda.lista_contactos()
    elif opcion == "3":
        nombre = input("Ingrese el nombre del contacto a buscar: ")
        agenda.buscar_contacto(nombre)
    elif opcion == "4":
        nombre = input("Ingrese el nombre del contacto a editar: ")
        agenda.editar_contacto(nombre)
    elif opcion == "5":
        print("Saliendo de la agenda...")
        break
    else:
        print("Opción inválida. Por favor intente nuevamente.")
