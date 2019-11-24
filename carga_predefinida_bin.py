#MODULO CARGA PREDEFINIDA

from imprimir_menus import limpiar_pantalla
from imprimir_mensaje import *
from info_predefinida import crear_archivos_binarios
from carga_archivos import grabar_en_csv, vaciar_archivo
import pickle

def carga_predefinida(restaurantes, clientes, rappitenderos):
	limpiar_pantalla()
	mensaje_info("Si realiza una carga predefinida los datos anteriores se perderan.")
	realizar_carga = mensaje_solicitud("Desea continuar? (s/n): ")
	if realizar_carga == "s":
		limpiar_pantalla()
		vaciar_archivos_existentes()
		crear_archivos_binarios() #En info_predefinida
		leer_archivos_binarios(restaurantes, clientes, rappitenderos)
		sobreescribir_con_info_predefinida(restaurantes, clientes, rappitenderos)
		mensaje_info('Se ha realizado una carga predefinida.\n')
		return restaurantes, clientes, rappitenderos
	print(mensaje_info("Volviendo al menu anterior..."))

def vaciar_archivos_existentes():
	vaciar_archivo("restaurantes.csv")
	vaciar_archivo("clientes.csv")
	vaciar_archivo("rappitenderos.csv")

def leer_archivos_binarios(restaurantes, clientes, rappitenderos):
	leer_binario("restaurantes_predefinido.bin", restaurantes)
	leer_binario("clientes_predefinido.bin", clientes)
	leer_binario("rappitenderos_predefinido.bin", rappitenderos)

def sobreescribir_con_info_predefinida(restaurantes, clientes, rappitenderos):
	grabar_en_csv(restaurantes, "restaurantes.csv")
	grabar_en_csv(clientes, "clientes.csv")
	grabar_en_csv(rappitenderos, "rappitenderos.csv")

def leer_binario(nombre_archivo, diccionario_a_cargar):
	with open(nombre_archivo, "rb") as arch:
		seguir_leyendo = True
		while seguir_leyendo:
			try:
				dato = pickle.load(arch)
				print(dato)
				cargar_diccionario(nombre_archivo, dato, diccionario_a_cargar)
			except EOFError:
				seguir_leyendo = False
	return diccionario_a_cargar

def cargar_diccionario(nombre_archivo, dato, diccionario):
	if nombre_archivo == "restaurantes_predefinido.bin":
		for nombre, direccion, telefono, posicion, radio_de_entrega, platos, total_de_ventas in zip(dato[0], dato[1], dato[2], dato[3], dato[4], dato[5], dato[6]):
			diccionario[nombre] = {'Direccion' : direccion, 'Telefono' : telefono, 'Posicion': posicion, 'Radio de Entrega': radio_de_entrega, 'Platos': platos, 'Total de ventas' : total_de_ventas}
	elif nombre_archivo == "clientes_predefinido.bin":
		for nombre, contrasenia, telefono, direccion, posicion, rappicreditos in zip(dato[0], dato[1], dato[2], dato[3], dato[4], dato[5]):
			diccionario[nombre] = {'Contrasenia' : contrasenia, 'Telefono' : telefono, 'Direccion' : direccion, 'Posicion' : posicion, 'Rappicreditos' : rappicreditos}
	elif nombre_archivo == "rappitenderos_predefinido.bin":
		for nombre, propina_acumulada, posicion_actual, pedido_actual, distancia_recorrida in zip(dato[0], dato[1], dato[2], dato[3], dato[4]):
			diccionario[nombre] = {'Propina acumulada' : propina_acumulada, 'Posicion actual' : posicion_actual, 'Pedido actual' : pedido_actual, 'Distancia recorrida' : distancia_recorrida}
