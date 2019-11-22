#MODULO CARGA PREDEFINIDA

#Todas estas funciones reciben los diccionarios vacios
#Devuelven los diccionarios con la informacion 'hardcodeada'

from imprimir_menus import limpiar_pantalla, mensaje_info, mensaje_solicitud
from info_predefinida import crear_archivos
import pickle

def carga_predefinida(restaurantes, clientes, rappitenderos):
	limpiar_pantalla()
	mensaje_info("Si realiza una carga predefinida los datos anteriores se perderan.")
	realizar_carga = mensaje_solicitud("Desea continuar? (s/n): ")
	if realizar_carga == "s":
		crear_archivos()
		leer_binario("restaurantes.bin", restaurantes)
		leer_binario("clientes.bin", clientes)
		leer_binario("rappitenderos.bin", rappitenderos)
		limpiar_pantalla()
		mensaje_info('Se ha realizado una carga predefinida.\n')
		return restaurantes, clientes, rappitenderos
	print(mensaje_info("Volviendo al menu anterior..."))

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
	if nombre_archivo == "restaurantes.bin":
		for nombre, direccion, telefono, posicion, radio_de_entrega, platos, total_de_ventas in zip(dato[0], dato[1], dato[2], dato[3], dato[4], dato[5], dato[6]):
			diccionario[nombre] = {'Direccion' : direccion, 'Telefono' : telefono, 'Posicion': posicion, 'Radio de Entrega': radio_de_entrega, 'Platos': platos, 'Total de ventas' : total_de_ventas}
	elif nombre_archivo == "clientes.bin":
		for nombre, contrasenia, telefono, direccion, posicion, rappicreditos in zip(dato[0], dato[1], dato[2], dato[3], dato[4], dato[5]):
			diccionario[nombre] = {'Contrasenia' : contrasenia, 'Telefono' : telefono, 'Direccion' : direccion, 'Posicion' : posicion, 'Rappicreditos' : rappicreditos}
	elif nombre_archivo == "rappitenderos.bin":
		for nombre, propina_acumulada, posicion_actual, pedido_actual, distancia_recorrida in zip(dato[0], dato[1], dato[2], dato[3], dato[4]):
			diccionario[nombre] = {'Propina acumulada' : propina_acumulada, 'Posicion actual' : posicion_actual, 'Pedido actual' : pedido_actual, 'Distancia recorrida' : distancia_recorrida}