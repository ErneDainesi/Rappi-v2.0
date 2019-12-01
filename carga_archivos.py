import os.path
import pickle
from mensajes_y_validaciones import mensaje_info

def cargar_archivos():
    restaurantes, clientes, rappitenderos = dict(), dict(), dict()
    cargar_datos_csv("restaurantes.csv", restaurantes)
    cargar_menus_csv(restaurantes)
    cargar_datos_csv("clientes.csv", clientes)
    cargar_datos_csv("rappitenderos.csv", rappitenderos)
    return restaurantes, clientes, rappitenderos

def guardar_datos_antes_de_salir(restaurantes, clientes, rappitenderos):
    #Guarda todos los datos de los diccionarios hasta el momento de uso con la info más actual
    vaciar_archivo("restaurantes.csv")
    vaciar_archivo("clientes.csv")
    vaciar_archivo("rappitenderos.csv")
    grabar_en_csv(restaurantes, "restaurantes.csv")
    platos_csv(restaurantes)
    grabar_en_csv(clientes, "clientes.csv")
    grabar_en_csv(rappitenderos, "rappitenderos.csv")

def cargar_datos_csv(nombre_csv, diccionario):
    if os.path.exists(nombre_csv):
        corte = []
        with open(nombre_csv) as archivo:
            next(archivo) #saltea el encabezado
            linea = leer_csv(archivo, corte)
            while linea != corte:
                cargar_diccionario_csv(linea, diccionario, nombre_csv)
                linea = leer_csv(archivo, corte)

def leer_csv(archivo, corte):
    linea = archivo.readline()
    lista = linea.rstrip().split(',')
    return lista if linea else corte

def grabar_en_csv(diccionario, nombre_del_archivo):
    #Guarda los datos del diccionario pasado por parámetro en un archivo .csv
    with open(nombre_del_archivo, "a") as arch:
        escribir_encabezado(arch, nombre_del_archivo)
        for clave in diccionario:
            escribir_en_archivo(clave, diccionario, nombre_del_archivo, arch)

def cargar_diccionario_csv(linea, diccionario, nombre_csv):
    if nombre_csv == "restaurantes.csv":
        diccionario[linea[0]] = {'Direccion' : linea[1], 'Telefono' : linea[2], 'Posicion': (float(linea[3]), float(linea[4])), 'Radio de Entrega': float(linea[5]), 'Total de ventas' : float(linea[6])}
    elif nombre_csv == "clientes.csv":
        diccionario[linea[0]] = {'Contrasenia' : linea[1], 'Telefono' : linea[2], 'Direccion' : linea[3], 'Posicion' : (float(linea[4]), float(linea[5])), 'Rappicreditos' : float(linea[6])}
    elif nombre_csv == "rappitenderos.csv":
        diccionario[linea[0]] = {'Propina acumulada' : float(linea[1]), 'Posicion actual' : (float(linea[2]), float(linea[3])), 'Pedido actual' : linea[4], 'Distancia recorrida' : float(linea[5])}

def escribir_encabezado(archivo, nombre_del_archivo):
    if nombre_del_archivo == "clientes.csv":
        archivo.write("Nombre,Contrasenia,Telefono,Direccion,Latitud,Longitud,Rappicreditos\n")
    elif nombre_del_archivo == "restaurantes.csv":
        archivo.write("Nombre,Direccion,Telefono,Latitud,Longitud,Radio de entrega,Total de ventas\n")
    elif nombre_del_archivo == "rappitenderos.csv":
        archivo.write("Nombre,Propina acumulada,Latitud,Longitud,Pedido actual,Distancia recorrida\n")
    elif nombre_del_archivo == "menu_restaurantes.csv":
        archivo.write("Restaurante,Plato,Precio\n")

def escribir_en_archivo(clave, diccionario, nombre_del_archivo, arch):
    if nombre_del_archivo == "clientes.csv":
        arch.write("{},{},{},{},{},{},{}\n".format(clave, diccionario[clave]["Contrasenia"], diccionario[clave]["Telefono"], diccionario[clave]["Direccion"], diccionario[clave]["Posicion"][0], diccionario[clave]["Posicion"][1], diccionario[clave]["Rappicreditos"]))
    elif nombre_del_archivo == "restaurantes.csv":
        arch.write("{},{},{},{},{},{},{}\n".format(clave, diccionario[clave]["Direccion"], diccionario[clave]["Telefono"], diccionario[clave]["Posicion"][0], diccionario[clave]["Posicion"][1], diccionario[clave]["Radio de Entrega"], diccionario[clave]["Total de ventas"]))
    elif nombre_del_archivo == "rappitenderos.csv":
        arch.write("{},{},{},{},{},{}\n".format(clave, diccionario[clave]["Propina acumulada"], diccionario[clave]["Posicion actual"][0], diccionario[clave]["Posicion actual"][1], diccionario[clave]["Pedido actual"], diccionario[clave]["Distancia recorrida"]))

def platos_csv(restaurantes):
    menus_csv = open("menu_restaurantes.csv", "w")
    escribir_encabezado(menus_csv, "menu_restaurantes.csv")
    escribir_menu(restaurantes, menus_csv)
    menus_csv.close()

def escribir_menu(restaurantes, menus_csv):
    for restaurante in restaurantes:
        for plato in restaurantes[restaurante]["Platos"]:
            menus_csv.write("{},{},{}\n".format(restaurante, plato[0], plato[1]))

def cargar_menus_csv(restaurantes):
    if os.path.exists("menu_restaurantes.csv"):
        corte = ['','',999999999999]
        platos = []
        with open("menu_restaurantes.csv") as menus_csv:
            next(menus_csv)
            linea = leer_csv(menus_csv, corte)
            corte_de_control_menus(platos, linea, corte, restaurantes, menus_csv)

def corte_de_control_menus(platos, linea, corte, restaurantes, menus_csv):
    while linea != corte:
        restaurante = linea[0]
        restaurantes[restaurante]["Platos"] = cargar_plato_a_restaurante(linea, platos)
        linea = leer_csv(menus_csv, corte)
        while restaurante == linea[0]: #Mientras siga siendo el mismo restaurante, carga los platos al diccionario
            restaurantes[restaurante]["Platos"] = cargar_plato_a_restaurante(linea, platos)
            linea = leer_csv(menus_csv, corte)
        platos = [] #Si no es el mismo dic, vacio la lista para volver a llenarla con los platos del proximo restaurante

def cargar_plato_a_restaurante(linea, platos):
    plato = (linea[1], float(linea[2]))
    platos.append(plato)
    return platos

def vaciar_archivo(nombre_del_archivo):
    if os.path.exists(nombre_del_archivo):
        arch = open(nombre_del_archivo, "w")
        arch.close()
    else:
        mensaje_info("El archivo {} no existe, entonces no se sobreescribio informacion.".format(nombre_del_archivo))

def leer_binario(nombre_archivo, diccionario_a_cargar):
    with open(nombre_archivo, "rb") as arch:
        seguir_leyendo = True
        while seguir_leyendo:
            try:
                dato = pickle.load(arch)
                cargar_diccionario_info_predefinida(nombre_archivo, dato, diccionario_a_cargar)
            except EOFError:
                seguir_leyendo = False
    return diccionario_a_cargar

def cargar_diccionario_info_predefinida(nombre_archivo, dato, diccionario):
    if nombre_archivo == "restaurantes_predefinido.bin":
        for nombre, direccion, telefono, posicion, radio_de_entrega, platos, total_de_ventas in zip(dato[0], dato[1], dato[2], dato[3], dato[4], dato[5], dato[6]):
            diccionario[nombre] = {'Direccion' : direccion, 'Telefono' : telefono, 'Posicion': posicion, 'Radio de Entrega': radio_de_entrega, 'Platos': platos, 'Total de ventas' : total_de_ventas}
    elif nombre_archivo == "clientes_predefinido.bin":
        for nombre, contrasenia, telefono, direccion, posicion, rappicreditos in zip(dato[0], dato[1], dato[2], dato[3], dato[4], dato[5]):
            diccionario[nombre] = {'Contrasenia' : contrasenia, 'Telefono' : telefono, 'Direccion' : direccion, 'Posicion' : posicion, 'Rappicreditos' : rappicreditos}
    elif nombre_archivo == "rappitenderos_predefinido.bin":
        for nombre, propina_acumulada, posicion_actual, pedido_actual, distancia_recorrida in zip(dato[0], dato[1], dato[2], dato[3], dato[4]):
            diccionario[nombre] = {'Propina acumulada' : propina_acumulada, 'Posicion actual' : posicion_actual, 'Pedido actual' : pedido_actual, 'Distancia recorrida' : distancia_recorrida}
