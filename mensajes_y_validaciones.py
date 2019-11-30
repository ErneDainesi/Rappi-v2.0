def mensaje_info(mensaje):
    print("[INFO]", mensaje)

def mensaje_solicitud(mensaje):
    return input("[SOLICITUD]" + " " + mensaje)

def mensaje_error(mensaje):
    print("[ERROR]", mensaje)
    
def ingresar_entre_rangos(inicio, fin):
    #Recibe el inicio y el fin de un rango que se desea ingresar un numero entre
    opcion_elegida = ingresar_entero_o_flotante('Ingrese una opcion entre {} y {}: '.format(inicio, fin), int)
    while opcion_elegida > fin or opcion_elegida < inicio:
        mensaje_error("La opcion esta fuera del rango pedido.")
        opcion_elegida = ingresar_entero_o_flotante('Debe ingresar una opcion entre {} y {}: '.format(inicio, fin), int)
    return opcion_elegida

def ingresar_entero_o_flotante(mensaje, tipo_de_dato):
    #Pide el ingreso de un dato tipo entero o flotante, si lo ingresado es distinto al tipo de dato esperado se lo
    # vuelve a pedir hasta que ingrese el tipo de dato correspondiente.
    entrada = ''
    while type(entrada) != tipo_de_dato:
        entrada = mensaje_solicitud(mensaje)
        try:
            entrada = int(entrada)
            return entrada
        except ValueError:
            if tipo_de_dato == int:
                mensaje_error("Debe ingresar un numero entero.")
            elif tipo_de_dato == float:
                mensaje_error("Debe ingresar un numero flotante.")

def pedir_numero_entero_positivo(mensaje):
    numero = ingresar_entero_o_flotante(mensaje, int)
    while numero < 1:
        mensaje_error("La cantidad debe ser mayor a cero.")
        numero = ingresar_entero_o_flotante('Vuelva a intentarlo: ', int)
    return numero
