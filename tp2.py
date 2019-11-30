#MODULO PRINCIPAL DEL TP

# Nombre del grupo: None
# Miembros: Nazarena Dos Santos (padron: 105492), Lucas Bilo (padron: 103252), Ernesto Dainesi (padron: 104346)

from imprimir_menus import *
from carga_predefinida_bin import carga_predefinida
from informes import *
from carga_manual import *
from pedido_manual import pedido_manual
from simulacion_pedidos import simulacion_de_pedidos
from carga_archivos import cargar_archivos, guardar_datos_antes_de_salir
from mensajes_y_validaciones import ingresar_entre_rangos

OPCION_MENU_CARGA = 1
OPCION_MENU_PEDIDOS = 2
OPCION_MENU_INFORMES = 3

def main():
	restaurantes, clientes, rappitenderos = cargar_archivos()
	menu_principal(restaurantes, clientes, rappitenderos)
	guardar_datos_antes_de_salir(restaurantes, clientes, rappitenderos)

def menu_principal(restaurantes, clientes, rappitenderos):
	opcion_elegida = 0
	while opcion_elegida != 4:
		limpiar_pantalla()
		imprimir_logo()		
		imprimir_menu_principal()
		opcion_elegida = ingresar_entre_rangos(1, 4)
		invocar_submenu_elegido(opcion_elegida, restaurantes, clientes, rappitenderos)
	limpiar_pantalla()	
	print('\nGracias por usar Rappi.')

def invocar_submenu_elegido(opcion_elegida, restaurantes, clientes, rappitenderos):
	limpiar_pantalla()
	if opcion_elegida != 4:
		opcion_submenu = 0
		rango_submenu = calcular_rango_submenu(opcion_elegida)
		while opcion_submenu != rango_submenu:			
			imprimir_logo()
			imprimir_submenu(opcion_elegida)
			opcion_submenu = ingresar_entre_rangos(1, rango_submenu)
			invocar_opcion_submenu(opcion_submenu, opcion_elegida, restaurantes, clientes, rappitenderos)

def calcular_rango_submenu(opcion_elegida):
	if opcion_elegida == OPCION_MENU_CARGA or opcion_elegida == OPCION_MENU_PEDIDOS:
		rango_submenu = 3
	elif opcion_elegida == OPCION_MENU_INFORMES:
		rango_submenu = 5
	return rango_submenu
	
def invocar_opcion_submenu(opcion_submenu, opcion_elegida, restaurantes, clientes, rappitenderos):
	#Aca van los llamados a las funciones del submenu que se eligio
	#Cada funcion se encuentra dentro de su respectivo modulo
	if opcion_elegida == OPCION_MENU_CARGA and opcion_submenu == 1:
		carga_manual(restaurantes, clientes, rappitenderos)
		limpiar_pantalla()
	elif opcion_elegida == OPCION_MENU_CARGA and opcion_submenu == 2:
		carga_predefinida(restaurantes, clientes, rappitenderos)
	elif opcion_elegida == OPCION_MENU_PEDIDOS and opcion_submenu == 1:
		limpiar_pantalla()
		pedido_manual(clientes, restaurantes, rappitenderos)
	elif opcion_elegida == OPCION_MENU_PEDIDOS and opcion_submenu == 2:
		simulacion_de_pedidos(clientes, restaurantes, rappitenderos)
	elif opcion_elegida == OPCION_MENU_INFORMES and opcion_submenu == 1:
		limpiar_pantalla()
		crear_informe(clientes, 'Rappicreditos')
	elif opcion_elegida == OPCION_MENU_INFORMES and opcion_submenu == 2:
		limpiar_pantalla()
		crear_informe(rappitenderos, 'Rappitenderos')
	elif opcion_elegida == OPCION_MENU_INFORMES and opcion_submenu == 3:
		limpiar_pantalla()
		crear_informe(restaurantes, 'Restaurantes')
	elif opcion_elegida == OPCION_MENU_INFORMES and opcion_submenu == 4:
		limpiar_pantalla()
		recorridos_rappitenderos(rappitenderos)

#----------------------
#------- CARGA --------
#----------------------

def carga_manual(restaurantes, clientes, rappitenderos):
	limpiar_pantalla()
	opcion_carga_manual = 0
	while opcion_carga_manual != 5:
		imprimir_logo()
		imprimir_submenu_carga_manual()
		opcion_carga_manual = ingresar_entre_rangos(1, 5)
		invocar_opcion_carga_manual(opcion_carga_manual, restaurantes, clientes, rappitenderos)

def invocar_opcion_carga_manual(opcion_carga_manual, restaurantes, clientes, rappitenderos):
	if opcion_carga_manual == 1:
		cargar_restaurante(restaurantes)
	elif opcion_carga_manual == 2:
		cargar_cliente(clientes)
	elif opcion_carga_manual == 3:
		cargar_plato_restaurante_ya_existente(restaurantes)
	elif opcion_carga_manual == 4:
		cargar_rappitendero(rappitenderos, restaurantes)

main()
