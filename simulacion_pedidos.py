#Simulacion de pedidos

import random
from pedido_manual import crear_pedido, asignar_pedido_a_rappitendero, calcular_rappicreditos_ganados, restaurantes_dentro_del_rango
from imprimir_menus import limpiar_pantalla
from mensajes_y_validaciones import mensaje_error, ingresar_entero_o_flotante

def simulacion_de_pedidos(clientes, restaurantes, rappitenderos):
	limpiar_pantalla()
	print("\n **** SIMULACION DE PEDIDOS ****\n")
	cantidad_simulaciones =  ingresar_entero_o_flotante("Puede simular entre 1 y 100 pedidos. Ingrese la cantidad: ", int)
	while cantidad_simulaciones < 1 or cantidad_simulaciones > 100:
		mensaje_error("La cantidad ingresada es invalida.")
		cantidad_simulaciones =  ingresar_entero_o_flotante("Puede simular entre 1 y 100 pedidos. Ingrese la cantidad: ", int)
	max_porciones = ingresar_entero_o_flotante("Ingrese una cantidad maxima de porciones por plato: ", int)
	limpiar_pantalla()
	generar_simulaciones(cantidad_simulaciones, max_porciones, clientes, restaurantes, rappitenderos)
		
def generar_simulaciones(cantidad_simulaciones, max_porciones, clientes, restaurantes, rappitenderos):
	print("\n **** PEDIDOS SIMULADOS ****\n")
	for simulacion in range(1, cantidad_simulaciones + 1):		
		cliente = random.choice(list(clientes))
		restaurantes_a_pedir = restaurantes_dentro_del_rango(restaurantes, clientes[cliente])
		if len(restaurantes_a_pedir) > 0:
			restaurante = random.choice(list(restaurantes_a_pedir))
			platos_restaurante = lista_platos(restaurantes[restaurante]["Platos"])
			total_a_pagar = 0
			pedido = {'Pedido': [], 'Destino': clientes[cliente]['Direccion']}
			crear_pedido_simulado(pedido, total_a_pagar, platos_restaurante, restaurante, restaurantes, cliente, clientes, rappitenderos, max_porciones)

def lista_platos(menu):
	platos = []
	for plato in menu:
		platos.append(plato[0])
	return platos
	
def crear_pedido_simulado(pedido, total_a_pagar, platos_restaurante, restaurante, restaurantes, cliente, clientes, rappitenderos, max_porciones):
	rango_platos_por_pedido = range(1, len(platos_restaurante) + 1)
	for x in rango_platos_por_pedido:
		plato = random.choice(platos_restaurante)
		cantidad_de_porciones = random.choice(range(1, max_porciones + 1))
		total_a_pagar = crear_pedido(plato, restaurantes[restaurante], cantidad_de_porciones, clientes[cliente], total_a_pagar, platos_restaurante, pedido)
	asignar_pedido_a_rappitendero(clientes[cliente], restaurantes[restaurante], rappitenderos, pedido, total_a_pagar, True)
	rappicreditos_ganados = calcular_rappicreditos_ganados(total_a_pagar)
	print("[SIMULACION] {} pidio en {}. Pago ${} y obtuvo {} rappicreditos.".format(cliente, restaurante, total_a_pagar, rappicreditos_ganados))
