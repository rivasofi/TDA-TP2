import sys
from archivos_tp.parsers import *
from archivos_tp.algoritmo import *

def main():
    archivo_listado = sys.argv[1]
    archivo_mensajes = sys.stdin
    
    posibles_palabras = cargar_palabras(archivo_listado)
    mensajes_a_analizar = cargar_mensajes(archivo_mensajes)
    
    for linea in mensajes_a_analizar:
        linea_analizada = algoritmo(linea, posibles_palabras)
        
        if linea_analizada == []:
            print("No es un mensaje")
        
        else:
            for palabra in linea_analizada:
                print(palabra, end=" ")
            print()  # para el salto de línea
    
if __name__ == "__main__":
    main()