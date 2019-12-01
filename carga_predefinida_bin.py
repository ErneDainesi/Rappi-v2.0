from imprimir_menus import limpiar_pantalla
from mensajes_y_validaciones import mensaje_info, mensaje_solicitud
from info_predefinida import crear_archivos_binarios
from carga_archivos import grabar_en_csv, leer_binario, platos_csv

def carga_predefinida(restaurantes, clientes, rappitenderos):
	limpiar_pantalla()
	mensaje_info("Si realiza una carga predefinida los datos anteriores se perderan.")
	realizar_carga = mensaje_solicitud("Desea continuar? (s/n): ")
	if realizar_carga == "s":
		limpiar_pantalla()
		vaciar_diccionarios(restaurantes, rappitenderos, clientes)
		crear_archivos_binarios() #En info_predefinida
		leer_archivos_binarios(restaurantes, clientes, rappitenderos)
		sobreescribir_con_info_predefinida(restaurantes, clientes, rappitenderos)
		platos_csv(restaurantes)
		mensaje_info('Se ha realizado una carga predefinida.\n')
		return restaurantes, clientes, rappitenderos
	print(mensaje_info("Volviendo al menu anterior..."))

def leer_archivos_binarios(restaurantes, clientes, rappitenderos):
	leer_binario("restaurantes_predefinido.bin", restaurantes)
	leer_binario("clientes_predefinido.bin", clientes)
	leer_binario("rappitenderos_predefinido.bin", rappitenderos)

def sobreescribir_con_info_predefinida(restaurantes, clientes, rappitenderos):
	grabar_en_csv(restaurantes, "restaurantes.csv")
	grabar_en_csv(clientes, "clientes.csv")
	grabar_en_csv(rappitenderos, "rappitenderos.csv")

def vaciar_diccionarios(restaurantes, rappitenderos, clientes):
	restaurantes.clear()
	rappitenderos.clear()
	clientes.clear()
