import sys
from archivos_tp.parsers import *

def main():
    archivo_listado = sys.argv[1]
    archivo_mensajes = sys.stdin
    
    posibles_palabras = cargar_palabras(archivo_listado)
    mensajes_a_analizar = cargar_mensajes(archivo_mensajes)
    
if __name__ == "__main__":
    main()