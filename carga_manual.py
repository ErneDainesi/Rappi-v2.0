from random import randint
from imprimir_menus import limpiar_pantalla, mensaje_error, mensaje_info, mensaje_solicitud, ingresar_entre_rangos


def cargar_restaurante(restaurantes):
    limpiar_pantalla()
    print("\n **** CARGA RESTAURANTE **** \n")
    nombre = ingresar_nombre(restaurantes)
    direccion = ingresar_direccion("restaurante")
    telefono = ingresar_telefono("restaurante")
    latitud, longitud = ingresar_coordenadas("restaurante")
    radio_de_entrega = ingresar_flotante("Ingrese el radio de entrega del restaurante: ")
    total_ventas = ingresar_flotante("Ingrese el total de ventas del restaurante: ")
    platos = cargar_plato()

    restaurantes[nombre] = {'Direccion': direccion, 'Telefono': telefono, 'Posicion': (latitud, longitud),
                            'Radio de Entrega': radio_de_entrega, 'Platos': platos, 'Total de ventas': total_ventas}
    mensaje_info("Su restaurante se ha cargado correctamente.")
    return restaurantes

def ingresar_flotante(indicacion):
    entrada = ''
    while type(entrada) != float:
        entrada = mensaje_solicitud(indicacion)
        try:
            entrada = float(entrada)
            return entrada
        except ValueError:
            mensaje_error("Debe ingresar un numero flotante.")

def ingresar_coordenadas(entidad):
    latitud = ingresar_flotante("Ingrese la latitud del " + entidad + ": ")
    longitud = ingresar_flotante("Ingrese la longitud del " + entidad + ": ")
    return latitud, longitud

def ingresar_telefono(entidad):
    telefono = mensaje_solicitud("Ingrese el telefono del " + entidad + ": ")
    while not validar_numero_telefono(telefono) or not parentesis_balanceados(telefono):
        mensaje_error("El telefono ingresado tiene un formato incorrecto")
        telefono = mensaje_solicitud("Ingrese el telefono del " + entidad + ": ")
    return telefono

def parentesis_balanceados(telefono):
    pos_parentesis_que_abre = 0
    pos_parentesis_que_cierra = 0
    parentesis_que_abren = []
    parentesis_que_cierran = []
    for caracter in telefono:
        if caracter == '(':
            parentesis_que_abren.append(caracter)
            pos_parentesis_que_abre = telefono.index(caracter)
        elif caracter == ')':
            parentesis_que_cierran.append(caracter)
            pos_parentesis_que_cierra = telefono.index(caracter)
    if len(parentesis_que_abren) == len(
            parentesis_que_cierran) and pos_parentesis_que_cierra >= pos_parentesis_que_abre:
        return True
    else:
        return False


def validar_numero_telefono(telefono):
    es_valido = True
    for caracter in telefono:
        if caracter not in "0123456789-()+ ":
            es_valido = False
    return es_valido


def ingresar_direccion(entidad):
    direccion = mensaje_solicitud("Ingrese la direccion del " + entidad + ": ")
    while direccion == '':
        mensaje_error("Debe ingresar una direccion\n")
        direccion = mensaje_solicitud("Ingrese la direccion del " + entidad + ": ")
    return direccion


def ingresar_nombre(restaurantes):
    nombre = mensaje_solicitud("Ingrese el nombre del restaurante: ")
    while len(nombre) > 25 or len(nombre) < 5:
        mensaje_error("Debe ingresar un nombre que posea entre 5 y 25 caracteres\n")
        nombre = mensaje_solicitud("Ingrese nuevamente el nombre del restaurante: ")
    while nombre in restaurantes:
        mensaje_error("Ya existe un restaurante con ese nombre\n")
        nombre = mensaje_solicitud("Ingrese nuevamente el nombre del restaurante: ")
    return nombre


def cargar_cliente(clientes):
    limpiar_pantalla()
    print("\n **** CARGA CLIENTE **** \n")
    nombre_usuario = ingresar_nombre_usuario(clientes)
    contrasenia = ingresar_contrasenia()
    confirmar_contrasenia(contrasenia)
    telefono = ingresar_telefono("cliente")
    direccion = ingresar_direccion("cliente")
    coordenadas = ingresar_coordenadas("cliente")
    rappicreditos = ingresar_rappicreditos()
    clientes[nombre_usuario] = {'Contrasenia': contrasenia, 'Telefono': telefono, 'Direccion': direccion,
                                'Posicion': coordenadas, 'Rappicreditos': rappicreditos}
    limpiar_pantalla()
    mensaje_info("\nEl cliente se ha cargado correctamente.")
    return clientes


def ingresar_nombre_usuario(clientes):
    nombre_usuario = mensaje_solicitud("Ingrese el nombre de usuario: ")
    while len(nombre_usuario) < 3 or len(nombre_usuario) > 12:
        mensaje_error("Debe ingresar un nombre que posea entre 3 y 12 caracteres\n")
        nombre_usuario = mensaje_solicitud("Ingrese nuevamente el nombre de usuario: ")
    while nombre_usuario in clientes.keys():
        mensaje_error("Ya existe un usuario con ese nombre\n")
        nombre_usuario = mensaje_solicitud("Ingrese nuevamente el nombre de usuario: ")
    return nombre_usuario


def ingresar_contrasenia():
    cant_mayusculas = 0
    cant_minusculas = 0
    cant_digitos = 0
    cant_no_simbolos = 0
    mensaje_info("\nContrasenia debera tener minimo 8 caracteres, una mayuscula, una minuscula, un digito y un simbolo.")
    contrasenia = mensaje_solicitud("Ingrese la contrasenia del cliente: ")
    while len(contrasenia) < 8:
        mensaje_error("Debe ingresar una contrasenia de 8 caracteres como minimo.")
        contrasenia = mensaje_solicitud("Ingrese nuevamente la contrasenia: ")
    for caracter in contrasenia:
        if caracter.isupper():
            cant_mayusculas += 1
        elif caracter.islower():
            cant_minusculas += 1
        elif caracter.isdigit():
            cant_digitos += 1
        elif not caracter.isalnum():
            cant_no_simbolos += 1
    while cant_mayusculas <= 1 and cant_minusculas <= 1 and cant_digitos <= 1 and cant_no_simbolos <= 1:
        mensaje_error("La contrasenia no cumple con los requisitos.")
        contrasenia = mensaje_solicitud("Ingrese nuevamente la contrasenia: ")
    return contrasenia


def confirmar_contrasenia(contrasenia):
    contrasenia_repetida = mensaje_solicitud("Confirme la contrasenia: ")
    while contrasenia != contrasenia_repetida:
        mensaje_error("Las contrasenias no coinciden")
        contrasenia_repetida = mensaje_solicitud("Confirme nuevamente la contrasenia: ")
    return contrasenia_repetida


def ingresar_rappicreditos():
    rappicreditos = ingresar_flotante("Ingrese los rappicreditos del cliente: ")
    return rappicreditos


def cargar_plato():
    limpiar_pantalla()
    print("\n **** CARGA PLATO **** \n")
    platos_nuevos = []
    cargar_plato = "s"
    while cargar_plato == "s":        
        nombre_plato = mensaje_solicitud("\nIngrese el nombre del plato para el restaurante: ")
        while len(nombre_plato) > 25 or len(nombre_plato) < 5:
            mensaje_error("Debe ingresar un nombre que posea entre 5 y 25 caracteres\n")
            nombre_plato = mensaje_solicitud("\nIngrese nuevamente el nombre del plato: ")
        precio_plato = ingresar_flotante("Ingrese el precio del plato: ")
        while precio_plato <= 0:
            mensaje_error("La cantidad a ingresar debe ser mayor a cero.")
            precio_plato = ingresar_flotante('Ingrese el precio del plato: ')
        platos_nuevos.append((nombre_plato, precio_plato))
        mensaje_info("\nSu plato se ha cargado correctamente.")
        cargar_plato = mensaje_solicitud("\nIngrese 's' para cargar otro plato o presione otra tecla para finalizar la carga: ")
        limpiar_pantalla()
        print("\n **** CARGA PLATO **** \n")
    limpiar_pantalla()
    return platos_nuevos

def cargar_plato_restaurante_ya_existente(restaurantes):
    limpiar_pantalla()
    imprimir_menu_lista_restaurantes(restaurantes)
    restaurante_elegido = seleccionar_restaurante(restaurantes)
    platos_nuevos = cargar_plato()
    restaurantes[restaurante_elegido]['Platos'] += platos_nuevos

def imprimir_menu_lista_restaurantes(restaurantes):
    print('**** LISTA DE RESTAURANTES ****\n')
    indice = 0
    for restaurante in restaurantes:
        indice += 1
        print("{}) {}".format(indice, restaurante))


def seleccionar_restaurante(restaurantes):
    inicio = 1
    if 1 == len(list(restaurantes)):
        fin = 2
    else:
        fin = len(list(restaurantes))
    opcion_elegida = ingresar_entre_rangos(inicio, fin)
    restaurante_elegido = list(restaurantes)[opcion_elegida - 1]
    return restaurante_elegido


def cargar_rappitendero(rappitenderos, restaurantes):
    limpiar_pantalla()
    print("\n **** CARGA RAPPITENDERO **** \n")
    nombre_rappitendero = mensaje_solicitud("Ingrese el nombre del rappitendero: ")
    propina_acumulada = ingresar_flotante("Ingrese la propina acumulada: ")
    coordenadas = restaurantes[elegir_restaurante_al_azar(restaurantes)]['Posicion']
    pedido_actual = None
    rappitenderos[nombre_rappitendero] = {'Propina acumulada': propina_acumulada, 'Posicion actual': coordenadas,
                                          'Pedido actual': pedido_actual}
    limpiar_pantalla()
    mensaje_info("\nRappitendero cargado con exito.")
    return rappitenderos


def elegir_restaurante_al_azar(restaurantes):
    lista_de_restaurantes = list(restaurantes)
    numero_random = randint(0, len(lista_de_restaurantes) - 1)
    restaurante_al_azar = lista_de_restaurantes[numero_random]
    return restaurante_al_azar
