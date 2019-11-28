import os.path
import pickle
from imprimir_mensaje import *

def cargar_archivos():
    restaurantes, clientes, rappitenderos = dict(), dict(), dict()
    cargar_datos_csv("restaurantes.csv", restaurantes)
    cargar_datos_csv("clientes.csv", clientes)
    cargar_datos_csv("rappitenderos.csv", rappitenderos)
    return restaurantes, clientes, rappitenderos

def cargar_datos_csv(nombre_csv, diccionario):
    try:
        corte = []
        with open(nombre_csv) as archivo:
            next(archivo) #saltea el encabezado
            linea = leer_csv(archivo, corte)
            while linea != corte:
                cargar_diccionario_csv(linea, archivo, diccionario, nombre_csv)
                linea = leer_csv(archivo, corte)
        return diccionario
    except FileNotFoundError:
        return diccionario

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

def cargar_diccionario_csv(linea, archivo, diccionario, nombre_csv):
    if nombre_csv == "restaurantes_predefinido.bin":
        diccionario[linea[0]] = {'Direccion' : linea[1], 'Telefono' : linea[2], 'Posicion': (float(linea[3]), float(linea[4])), 'Radio de Entrega': float(linea[5]), 'Platos': linea[6], 'Total de ventas' : float(linea[7])}
    elif nombre_csv == "clientes_predefinido.bin":
        diccionario[linea[0]] = {'Contrasenia' : linea[1], 'Telefono' : linea[2], 'Direccion' : linea[3], 'Posicion' : (float(linea[4]), float(linea[5])), 'Rappicreditos' : float(linea[6])}
    elif nombre_csv == "rappitenderos_predefinido.bin":
        diccionario[linea[0]] = {'Propina acumulada' : float(linea[1]), 'Posicion actual' : (float(linea[2]), float(linea[3])), 'Pedido actual' : linea[4], 'Distancia recorrida' : float(linea[5])}


def actualizar_csv(diccionario, clave, nombre_del_archivo):
    if not os.path.exists(nombre_del_archivo): #Si no existe el archivo, escribe el encabezado.
        archivo = open(nombre_del_archivo, "a")
        escribir_encabezado(archivo, nombre_del_archivo)
    else:
        archivo = open(nombre_del_archivo, "a")
    escribir_en_archivo(clave, diccionario, nombre_del_archivo, archivo)
    archivo.close()

def escribir_encabezado(archivo, nombre_del_archivo):
    if nombre_del_archivo == "clientes.csv":
        archivo.write("Nombre,Contrasenia,Telefono,Direccion,Latitud,Longitud,Rappicreditos\n")
    elif nombre_del_archivo == "restaurantes.csv":
        archivo.write("Nombre,Direccion,Telefono,Latitud,Longitud,Radio de entrega,Platos,Total de ventas\n")
    elif nombre_del_archivo == "rappitenderos.csv":
        archivo.write("Nombre,Propina acumulada,Latitud,Longitud,Pedido actual,Distancia recorrida\n")

def escribir_en_archivo(clave, diccionario, nombre_del_archivo, arch):
    if nombre_del_archivo == "clientes.csv":
        arch.write("{},{},{},{},{},{},{}\n".format(clave, diccionario[clave]["Contrasenia"], diccionario[clave]["Telefono"], diccionario[clave]["Direccion"], diccionario[clave]["Posicion"][0], diccionario[clave]["Posicion"][1], diccionario[clave]["Rappicreditos"]))
    elif nombre_del_archivo == "restaurantes.csv":
        arch.write("{},{},{},{},{},{},{},{}\n".format(clave, diccionario[clave]["Direccion"], diccionario[clave]["Telefono"], diccionario[clave]["Posicion"][0], diccionario[clave]["Posicion"][1], diccionario[clave]["Radio de Entrega"], diccionario[clave]["Platos"], diccionario[clave]["Total de ventas"]))
    elif nombre_del_archivo == "rappitenderos.csv":
        arch.write("{},{},{},{},{},{}\n".format(clave, diccionario[clave]["Propina acumulada"], diccionario[clave]["Posicion actual"][0], diccionario[clave]["Posicion actual"][1], diccionario[clave]["Pedido actual"], diccionario[clave]["Distancia recorrida"]))

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
