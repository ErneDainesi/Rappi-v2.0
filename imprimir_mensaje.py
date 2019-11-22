def mensaje_info(mensaje):
    print("[INFO]", mensaje)

def mensaje_solicitud(mensaje):
    return input("[SOLICITUD]" + " " + mensaje)

def mensaje_error(mensaje):
    print("[ERROR]", mensaje)