# Diccionario

# Ejercicio 1


def calcular_precio_fruta():
    precios_frutas = {"Banana": 1.35, "Manzana": 0.80, "Pera": 0.85, "Naranja": 0.70}

    fruta = input("Ingrese el nombre de la fruta: ")
    kilos = float(input("Ingrese la cantidad de kilos: "))

    # Verificar si la fruta existe en el diccionario
    if fruta in precios_frutas:
        precio_por_kilo = precios_frutas[fruta]
        precio_total = precio_por_kilo * kilos
        print(f"El precio de {kilos} kilos de {fruta} es: {precio_total}")
    else:
        print(f"La fruta {fruta} no está en el diccionario de precios.")


calcular_precio_fruta()

# Ejercicio 2


def imprimir_datos_personas(personas):
    print("{:<15} {:<15} {:<10} {:<20}".format("Nombre", "Apellido", "Edad", "Email"))
    print("-" * 60)
    for persona in personas:
        nombre = persona["Nombre"]
        apellido = persona["Apellido"]
        edad = persona["Edad"]
        email = persona["Email"]
        print("{:<15} {:<15} {:<10} {:<20}".format(nombre, apellido, edad, email))
    print("-" * 60)


# Crear el diccionario con los datos de las dos personas iniciales
personas = [
    {
        "Nombre": "Emilia",
        "Apellido": "Cabrera",
        "Edad": 23,
        "Email": "ecabrera@curso.com",
    },
    {
        "Nombre": "Gustavo Andrés",
        "Apellido": "Peralta",
        "Edad": 26,
        "Email": "gperalta@curso.com",
    },
]

# Solicitar al usuario los datos de la persona nueva
nombre = input("Ingrese el nombre de la persona: ")
apellido = input("Ingrese el apellido de la persona: ")
edad = int(input("Ingrese la edad de la persona: "))
email = input("Ingrese el email de la persona: ")

# Crear un diccionario con los datos de la persona nueva
persona_nueva = {"Nombre": nombre, "Apellido": apellido, "Edad": edad, "Email": email}

# Agregar la persona nueva al diccionario de personas
personas.append(persona_nueva)

# Imprimir los datos de las personas
imprimir_datos_personas(personas)


# Ejercicio3


def generar_diccionario_directorio(directorio):
    lineas = directorio.split("\n")
    campos = lineas[0].split(";")
    diccionario = {}

    for linea in lineas[1:]:
        datos = linea.split(";")
        cliente = {}

        for i in range(len(campos)):
            campo = campos[i]
            valor = datos[i]
            cliente[campo] = valor

        dni = cliente["dni"]
        diccionario[dni] = cliente

    return diccionario


directorio = "dni;nombre;email;teléfono;descuento\n01234567L;Luis González;luisgonzalez@mail.com;656343576;12.5\n71476342J;Macarena Ramírez;macarena@mail.com;692839321;8\n63823376M;Juan José Martínez;juanjo@mail.com;664888233;5.2\n98376547F;Carmen Sánchez;carmen@mail.com;667677855;15.7"

diccionario_directorio = generar_diccionario_directorio(directorio)

# Imprimir el diccionario de clientes
for dni, cliente in diccionario_directorio.items():
    print(f"{dni}: {cliente}")
