#MODULO PARA IMPRIMIR MENUS
import os

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
		print('**** INFORMES ****\n 1) Clientes con mas Rappicreditos\n 2) Rappitenderos con mas propina\n 3) Restaurantes con mas ventas \n 4) Distancia recorrida por rappitenderos \n 5) Volver \n')

def imprimir_submenu_carga_manual():
	print('**** CARGA MANUAL ****\n 1) Restaurante \n 2) Cliente \n 3) Plato \n 4) Rappitendero \n 5) Volver \n')

