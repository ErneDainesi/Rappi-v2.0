import pickle

def crear_archivos_binarios():
    info_clientes()
    info_rappitenderos()
    info_restaurantes()

def info_restaurantes():
	nombre = ['La Guitarrita', 'La Farola Express', 'Wunderbar', 'La Juvenil', 'Kansas']
	direccion = ['Cuba 3300', 'Amenabar 1602', 'Av. Cramer 2830', 'Av. Cabildo 1833', 'Av. del Libertador 4625']
	telefono = ['011 4704-0756', '011 4780-3526', '011 2133-7805', '011 4786-3894', '011 4776-4100']
	posicion = [(-34.5504, -58.4643), (-34.5674, -58.4549), (-34.5585, -58.4668), (-34.5644, -58.4543), (-34.5712, -58.4232)]
	radio_de_entrega = [24.00, 30.00, 5.00, 23.00, 50.00]
	platos = [[('Muzzarela', 500.00), ('Coca-Cola', 130.00), ('Fugazzeta Rellena', 550.00)],
				[('Milanesa Napolitana', 650.00), ('Isenbeck', 180.00), ('Empanada', 40.00)], 
				[('Kill Bill', 420.00), ('Papas Cheddar', 250.00), ('Porron Imperial', 140.00)],
				[('Sorrentinos', 250.00), ('Ravioles', 230.00), ('Nioquis de papa', 200.00)],
				[('Ribs con BBQ', 650.00), ('Ojo de bife', 700.00), ('Pepsi', 200.00)]]
	total_de_ventas = (12500.30, 9537.62, 10530.27, 8763.50, 13621.69)
	datos_restaurantes = [nombre, direccion, telefono, posicion, radio_de_entrega, platos, total_de_ventas]
	generar_archivo_binario(datos_restaurantes, "restaurantes_predefinido.bin")

def info_clientes():
	nombre = ['Erne Dainesi', 'Lucas Bilo', 'Naza DS', 'Gallardo', 'Ricky Fort']
	contrasenia = ['ErneDai_123', 'LucasBilo_123', 'Nazarena_123', 'Pity_91218', 'Miame_123']
	telefono = ['+54 (011) 30036100', '+54 (011) 548965', '+54 (011) 85695745', '+54 (011) 51238445', '+54 (011) 6050019']
	direccion = ['Campos Salles 1857', 'Plaza de Mayo', 'Retiro', 'Obelisco', 'Casa Rosada']
	posicion = [(-34.5489, -58.4595), (-34.6082, -58.3709), (-34.5916, -58.3743), (-34.6037, -58.3814), (-34.6156, -58.4351)]
	rappicreditos = [30.25, 100.50, 150.45, 200.10, 500.05]
	datos_clientes = [nombre, contrasenia, telefono, direccion, posicion, rappicreditos]
	generar_archivo_binario(datos_clientes, "clientes_predefinido.bin")

def info_rappitenderos():
	nombre = ['Roberto', 'Juan', 'Carlos', 'Alberto', 'Javier']
	propina_acumulada = [52.50, 143.25, 345.00, 283.25, 150.00]
	posicion_actual = [(-34.5504, -58.4643), (-34.5674, -58.4549), (-34.5585, -58.4668), (-34.5644, -58.4543), (-34.5712, -58.4232)]
	pedido_actual = [None, None, None, None, None]
	distancia_recorrida = [0.0, 0.0, 0.0, 0.0, 0.0]
	datos_rappitenderos = [nombre, propina_acumulada, posicion_actual, pedido_actual, distancia_recorrida]
	generar_archivo_binario(datos_rappitenderos, "rappitenderos_predefinido.bin")

def generar_archivo_binario(diccionario, nombre_del_archivo):
	with open(nombre_del_archivo, "wb") as arch:
		pkl = pickle.Pickler(arch)
		pkl.dump(diccionario)
