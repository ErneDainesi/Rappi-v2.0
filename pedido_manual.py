# INFORMACION DE HAVERSINE SACADA DE https://pypi.org/project/haversine/
import random
import math
from haversine import haversine
from imprimir_menus import limpiar_pantalla, ingresar_entero, mensaje_solicitud, mensaje_error, mensaje_info, ingresar_entre_rangos

def pedido_manual(clientes, restaurantes, rappitenderos):
	print('\n**** INICIO DE SESION ****\n')
	usuario = mensaje_solicitud('Ingrese su nombre de usuario: ')
	usuario = validar_inicio_de_sesion(usuario, clientes)
	mostrar_restaurantes(restaurantes, usuario, rappitenderos, clientes)

def validar_inicio_de_sesion(usuario, clientes):
	while usuario not in clientes:
		mensaje_error("El usuario no esta registrado.")
		usuario = mensaje_solicitud('Vuelva a intentar: ')
	contrasenia = mensaje_solicitud('Contrasenia: ')
	while contrasenia != clientes[usuario]['Contrasenia']:
		mensaje_error("Contrasenia incorrecta.")
		contrasenia = mensaje_solicitud('Vuelva a intentar: ')
	return usuario

def mostrar_restaurantes(restaurantes, usuario, rappitenderos, clientes):
	limpiar_pantalla()
	print('\nBienvenido {}'.format(usuario))
	print('\n**** RESTAURANTES ****\n')
	cliente = clientes[usuario]
	restaurantes_a_pedir = restaurantes_dentro_del_rango(restaurantes, cliente)
	indice = 0
	for restaurante in restaurantes_a_pedir:
		indice += 1
		print("{}) {}".format(indice, restaurante))
	elegir_restaurante(cliente, restaurantes, rappitenderos, restaurantes_a_pedir)

def restaurantes_dentro_del_rango(restaurantes, cliente):
	#Devuelve una lista con los restaurantes que hacen envios al domicilio del cliente.
	restaurantes_a_pedir = []
	coordenadas_cliente = cliente["Posicion"]
	for restaurante in restaurantes:
		coordenadas_restaurante = restaurantes[restaurante]["Posicion"]
		radio_de_entrega = restaurantes[restaurante]["Radio de Entrega"]
		distancia = haversine(coordenadas_cliente, coordenadas_restaurante)
		if distancia <= radio_de_entrega:
			restaurantes_a_pedir.append(restaurante)
	return restaurantes_a_pedir

def elegir_restaurante(cliente, restaurantes, rappitenderos, restaurantes_a_pedir):
	inicio = 1
	if 1 == len(list(restaurantes_a_pedir)):
		fin = 2
	else:
		fin = len(list(restaurantes_a_pedir))
	opcion_elegida = ingresar_entre_rangos(inicio, fin)
	nombre_restaurante = list(restaurantes_a_pedir)[opcion_elegida - 1]
	restaurante_elegido = restaurantes[nombre_restaurante]
	elegir_plato(cliente, restaurante_elegido, rappitenderos, nombre_restaurante)

def elegir_plato(cliente, restaurante_elegido, rappitenderos, nombre_restaurante):
	limpiar_pantalla()
	seguir = 's'
	total_a_pagar = 0
	pedido = {'Pedido': [], 'Destino': cliente['Direccion']}
	while seguir == 's':
		limpiar_pantalla()
		platos_restaurante_elegido, fin = mostrar_menu_restaurante(restaurante_elegido, nombre_restaurante)
		posicion_plato_elegido = ingresar_entre_rangos(1, fin)
		plato_elegido = list(platos_restaurante_elegido)[posicion_plato_elegido - 1]
		cantidad = pedir_numero_entero_positivo('Ingrese la cantidad a pedir: ')
		total_a_pagar = crear_pedido(plato_elegido, restaurante_elegido, cantidad, cliente, total_a_pagar, platos_restaurante_elegido, pedido)
		seguir = mensaje_solicitud("Ingrese 's' para elegir otro plato o presione otra tecla para finalizar el pedido: ")
	asignar_pedido_a_rappitendero(cliente, restaurante_elegido, rappitenderos, pedido, total_a_pagar, False)

def crear_pedido(plato_elegido, restaurante_elegido, cantidad, cliente, total_a_pagar, platos_restaurante_elegido, pedido):		
		posicion_del_plato = platos_restaurante_elegido.index(plato_elegido)
		total_a_pagar += (restaurante_elegido['Platos'][posicion_del_plato][1] * cantidad)
		posicion_del_plato_en_pedido = plato_ya_esta_en_pedido(plato_elegido, pedido)
		if posicion_del_plato_en_pedido == -1:
			pedido['Pedido'].append((cantidad, plato_elegido))
		else:
			cantidad_anterior = pedido['Pedido'][posicion_del_plato_en_pedido][0]
			del (pedido['Pedido'][posicion_del_plato_en_pedido])
			pedido['Pedido'].append((cantidad + cantidad_anterior, plato_elegido))
		return total_a_pagar	

def mostrar_menu_restaurante(restaurante_elegido, nombre_restaurante):
	print('\n**** MENU {} ****\n'.format(nombre_restaurante))
	platos_restaurante_elegido = []
	opcion_menu = 0
	for plato in restaurante_elegido['Platos']:
		opcion_menu += 1
		platos_restaurante_elegido.append(plato[0])
		print('{}) {} - ${}'.format(opcion_menu, plato[0], plato[1]))
	if 1 == len(platos_restaurante_elegido):
		fin = 2
	else:
		fin = len(platos_restaurante_elegido)
	return platos_restaurante_elegido, fin

def plato_ya_esta_en_pedido(plato, pedido):
	#Funcion para verificar si el plato elegido ya habia sido elegido con anterioridad en el mismo pedido
    #En caso de que si devuelvo su posicion, sino -1
	for i in range(len(pedido['Pedido'])):
		if plato in pedido['Pedido'][i]:
			return i
	return -1

def pedir_numero_entero_positivo(mensaje):
	numero = ingresar_entero(mensaje)
	while numero < 1:
		mensaje_error("La cantidad debe ser mayor a cero.")
		numero = ingresar_entero('Vuelva a intentarlo: ')
	return numero

def asignar_pedido_a_rappitendero(cliente, restaurante_elegido, rappitenderos, pedido, total_a_pagar, simulacion):
	rappitendero_asignado, distancia_al_restaurante = calcular_rappitendero_mas_cercano(restaurante_elegido, rappitenderos)
	rappitenderos[rappitendero_asignado]['Pedido actual'] = pedido
	rappitenderos[rappitendero_asignado]['Posicion actual'] = restaurante_elegido['Posicion']
	rappitenderos[rappitendero_asignado]['Distancia recorrida'] += distancia_al_restaurante
	rappitendero_asignado = rappitenderos[rappitendero_asignado]
	calcular_demora(cliente, rappitendero_asignado, total_a_pagar, restaurante_elegido, simulacion)

def calcular_rappitendero_mas_cercano(restaurante, rappitenderos):
	#Devuelve al rappitendero mas cercano al restaurante y la distancia a la cual se encuentra del mismo
	rappitendero_mas_cercano = ''
	distancia_anterior = 9999
	coordenadas_restaurante = restaurante["Posicion"]
	for rappitendero in rappitenderos:
		coordenadas_rappitendero = rappitenderos[rappitendero]["Posicion actual"]
		distancia = haversine(coordenadas_restaurante, coordenadas_rappitendero)
		if distancia < distancia_anterior:
			rappitendero_mas_cercano = rappitendero
			distancia_anterior = distancia
	return rappitendero_mas_cercano, distancia_anterior

def	calcular_demora(cliente, rappitendero_asignado, total_a_pagar, restaurante_elegido, simulacion):
	posicion_rappitendero = rappitendero_asignado['Posicion actual']
	velocidad_rappitendero = 15
	destino = cliente['Posicion']
	distancia = haversine(posicion_rappitendero, destino)
	rappitendero_asignado['Distancia recorrida'] += distancia
	tiempo_estimado = round((distancia / velocidad_rappitendero) * 60)
	entregar_pedido(cliente, rappitendero_asignado, total_a_pagar, restaurante_elegido, tiempo_estimado, simulacion)

def entregar_pedido(cliente, rappitendero_asignado, total_a_pagar, restaurante_elegido, tiempo_estimado, simulacion):
	rappitendero_asignado['Posicion actual'] = cliente['Posicion']
	rappicreditos_ganados = calcular_rappicreditos_ganados(total_a_pagar)
	cliente['Rappicreditos'] += rappicreditos_ganados
	restaurante_elegido['Total de ventas'] += (total_a_pagar * 0.95)
	rappitendero_asignado['Propina acumulada'] += (total_a_pagar * 0.05)
	rappitendero_asignado['Pedido actual'] = {'Pedido': [], 'Destino': ''}
	informar_sobre_pedido(simulacion, tiempo_estimado, total_a_pagar, rappicreditos_ganados)

def calcular_rappicreditos_ganados(total_a_pagar):
	rappicreditos_ganados = 0
	if total_a_pagar < 200:
		rappicreditos_ganados = (total_a_pagar * 0.05)
	elif (total_a_pagar >= 200) and (total_a_pagar < 500):
		rappicreditos_ganados = (total_a_pagar * 0.1)
	else:
		rappicreditos_ganados = (total_a_pagar * 0.15)
	return rappicreditos_ganados

def informar_sobre_pedido(simulacion, tiempo_estimado, total_a_pagar, rappicreditos_ganados):
	if not simulacion:
		limpiar_pantalla()
		mensaje_info('Su pedido tardara {} minutos en llegar y el monto a pagar es ${}.'.format(tiempo_estimado, total_a_pagar))
		mensaje_info('Por su pedido gano {} rappicreditos que seran acreditados a su cuenta de forma inmediata.'.format(rappicreditos_ganados))
		print('\nMuchas gracias por usar Rappi')
		mensaje_info('Su sesion a sido cerrada.')
