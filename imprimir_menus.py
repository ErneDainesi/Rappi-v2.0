#MODULO PARA IMPRIMIR MENUS
import os

def ingresar_entre_rangos(inicio, fin):
	#Recibe el inicio y el fin de un rango que se desea ingresar un numero entre
	opcion_elegida = ingresar_entero('Ingrese una opcion entre {} y {}: '.format(inicio, fin))
	while opcion_elegida > fin or opcion_elegida < inicio:
		mensaje_error("La opcion esta fuera del rango pedido.")
		opcion_elegida = ingresar_entero('Debe ingresar una opcion entre {} y {}: '.format(inicio, fin))
	return opcion_elegida

def mensaje_info(mensaje):
	print("[INFO]", mensaje)

def mensaje_solicitud(mensaje):
	return input("[SOLICITUD]" + " " + mensaje)

def mensaje_error(mensaje):
	print("[ERROR]", mensaje)

def ingresar_entero(mensaje):
	entrada = ''
	while type(entrada) != int:
		entrada = mensaje_solicitud(mensaje)
		try:
			entrada = int(entrada)
			return entrada
		except ValueError:
			mensaje_error("Debe ingresar un numero entero.")

def limpiar_pantalla():
	if os.name == "nt":
		return os.system("cls")
	else:
		return os.system("clear")

def imprimir_logo():
	print('\n*********************')
	print('**** RAPPI v2.0 *****')
	print('*********************\n')

def imprimir_menu_principal():
	print('**** MENU PRINCIPAL ****')
	print('1) Carga de datos')
	print('2) Pedidos')
	print('3) Informes')
	print('4) Salir \n')

def imprimir_submenu(opcion_elegida):
	if opcion_elegida == 1:
		print('**** CARGA DE DATOS ****\n 1) Carga manual \n 2) Carga predefinida \n 3) Volver \n')
	elif opcion_elegida == 2:
		print('**** PEDIDOS **** \n 1) Pedido manual \n 2) Simulacion de pedidos \n 3) Volver \n')
	elif opcion_elegida == 3:
		print('**** INFORMES ****\n 1) Clientes con mas Rappicreditos\n 2) Rappitenderos con mas propina\n 3) Restaurantes con mas ventas \n 4) Generar archivo con formato csv de los rappitenderos y su distancia recorrida \n 5) Volver \n')

def imprimir_submenu_carga_manual():
	print('**** CARGA MANUAL ****\n 1) Restaurante \n 2) Cliente \n 3) Plato \n 4) Rappitendero \n 5) Volver \n')

