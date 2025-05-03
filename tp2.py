import sys
from archivos_tp.parsers import *
from archivos_tp.algoritmo import *

def main():
    archivo_listado = sys.argv[1]
    archivo_mensajes = sys.stdin
    
    posibles_palabras = cargar_palabras(archivo_listado)
    mensajes_a_analizar = cargar_mensajes(archivo_mensajes)
    
    for linea in mensajes_a_analizar:
        opt, indices = algoritmo(linea, posibles_palabras)
        
        if not opt[len(linea)]:
            print("No es un mensaje")
        else:
            palabras = reconstruccion(linea, indices, len(linea))
            print(" ".join(palabras))
    
if __name__ == "__main__":
    main()