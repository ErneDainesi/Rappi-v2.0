#MODULO PARA LOS INFORMES
from imprimir_mensaje import mensaje_info

def crear_informe(diccionario, tipo_de_informe):
	#tipo_de_informe es un parametro para saber que informe mostrar
	#diccionario puede ser restaurantes, clientes o rappitenderos
	top_diez_rappicreditos = {}
	mayor_propina = {}
	mas_ventas_restaurantes = {}
	for clave in diccionario:
		#Clave puede ser: Nombre del cliente, del rappitendero o del restaurante.
		#Depende el tipo de informe que se pida
		if tipo_de_informe == 'Rappicreditos':
			top_diez_rappicreditos[clave] = diccionario[clave]['Rappicreditos']
		elif tipo_de_informe == 'Rappitenderos':
			mayor_propina[clave] = diccionario[clave]['Propina acumulada']
		elif tipo_de_informe == 'Restaurantes':
			mas_ventas_restaurantes[clave] = diccionario[clave]['Total de ventas']
	mostrar_informe_pedido(tipo_de_informe, top_diez_rappicreditos, mayor_propina, mas_ventas_restaurantes)

def mostrar_informe_pedido(tipo_de_informe, top_diez_rappicreditos, mayor_propina, mas_ventas_restaurantes):
	if tipo_de_informe == 'Rappicreditos':
		print('\n **** CLIENTES CON MAS RAPPICREDITOS ****\n')
		mostrar_listado(top_diez_rappicreditos)
	elif tipo_de_informe == 'Rappitenderos':
		print('\n **** RAPPITENDEROS CON MAYOR PROPINA ****\n')
		mostrar_listado(mayor_propina)
	elif tipo_de_informe == 'Restaurantes':
		print('\n **** RESTAURANTES CON MAS VENTAS ****\n')
		mostrar_listado(mas_ventas_restaurantes)

def mostrar_listado(diccionario):
	#Asumo que todos los informes son top 10
	ranking_ordenado = sorted(diccionario.items(), key = lambda x : x[1], reverse = True)
	puesto = 0
	for cliente in ranking_ordenado[:10]:
		puesto += 1
		print('{} - {} - ${}'.format(puesto, cliente[0], cliente[1]))

def crear_archivo_rappitenderos(rappitenderos):
	print('\n **** DISTANCIAS RECORRIDAS ****\n')
	with open("recorridos_rappitenderos.csv", 'w') as archivo:
		archivo.write("Nombre, Distancia recorrida(km)\n")
		for rappitendero in rappitenderos:
			archivo.write("{}, {}\n".format(rappitendero, round(rappitenderos[rappitendero]["Distancia recorrida"], 1)))
			print("{}, {}km".format(rappitendero, round(rappitenderos[rappitendero]["Distancia recorrida"], 1)))
	mensaje_info("Se ha creado un archivo .csv con los datos del informe")
