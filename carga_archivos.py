import os.path

def grabar_en_csv(diccionario, nombre_del_archivo):
    #Guarda los datos del diccionario pasado por parámetro en un archivo .csv
    with open(nombre_del_archivo, "a") as arch:
        escribir_encabezado(arch, nombre_del_archivo)
        for clave in diccionario:
            escribir_en_archivo(clave, diccionario, nombre_del_archivo, arch)

def actualizar_csv(diccionario, clave, nombre_del_archivo):
    if not os.path.exists(nombre_del_archivo): #Si no existe el archivo, escribe el encabezado.
        archivo = open(nombre_del_archivo, "a")
        escribir_encabezado(archivo, nombre_del_archivo)
        escribir_en_archivo(clave, diccionario, nombre_del_archivo, archivo)
        archivo.close()
    else:
        archivo = open(nombre_del_archivo, "a")
        escribir_en_archivo(clave, diccionario, nombre_del_archivo, archivo)
        archivo.close()

def escribir_en_archivo(clave, diccionario, nombre_del_archivo, arch):
    if nombre_del_archivo == "clientes.csv":
        arch.write("{}, {}, {}, {}, {}, {}\n".format(clave, diccionario[clave]["Contrasenia"], diccionario[clave]["Telefono"], diccionario[clave]["Direccion"], diccionario[clave]["Posicion"], diccionario[clave]["Rappicreditos"]))
    elif nombre_del_archivo == "restaurantes.csv":
        arch.write("{}, {}, {}, {}, {}, {}, {}\n".format(clave, diccionario[clave]["Direccion"], diccionario[clave]["Telefono"], diccionario[clave]["Posicion"], diccionario[clave]["Radio de Entrega"], diccionario[clave]["Platos"], diccionario[clave]["Total de ventas"]))
    elif nombre_del_archivo == "rappitenderos.csv":
        arch.write("{}, {}, {}, {}, {}\n".format(clave, diccionario[clave]["Propina acumulada"], diccionario[clave]["Posicion actual"], diccionario[clave]["Pedido actual"], diccionario[clave]["Distancia recorrida"]))

def escribir_encabezado(archivo, nombre_del_archivo):
    if nombre_del_archivo == "clientes.csv":
        archivo.write("Nombre, Contrasenia, Telefono, Direccion, Posicion, Rappicreditos\n")
    elif nombre_del_archivo == "restaurantes.csv":
        archivo.write("Nombre, Direccion, Telefono, Posicion, Radio de entrega, Platos, Total de ventas\n")
    elif nombre_del_archivo == "rappitenderos.csv":
        archivo.write("Nombre, Propina acumulada, Posicion actual, Pedido actual, Distancia recorrida\n")

def vaciar_archivo(nombre_del_archivo):
    if not os.path.exists(nombre_del_archivo):
        arch = open(nombre_del_archivo, "w")
        arch.close()
    else:
        if nombre_del_archivo == "clientes.csv":
            mensaje_info("No existe el archivo clientes, entonces no se sobreescribio informacion anterior.")
        elif nombre_del_archivo == "restaurantes.csv":
            mensaje_info("No existe el archivo restaurantes, entonces no se sobreescribio informacion anterior.")
        elif nombre_del_archivo == "rappitenderos.csv":
            mensaje_info("No existe el archivo rappitenderos, entonces no se sobreescribio informacion anterior.")
