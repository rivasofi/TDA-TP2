def cargar_palabras(listado):
    palabras = set()
    with open(listado, 'r') as archivo_listado:
        for line in archivo_listado:
            palabra = line.strip()
            if palabra:
                palabras.add(palabra)
    return palabras

def cargar_mensajes(posibles_mensajes):
    #no necesito abrir el archivo al venir como stdin
    mensajes = []
    for line in posibles_mensajes:
        mensaje = line.strip()
        if mensaje:
            mensajes.append(mensaje)
    return mensajes