import sys
from archivos_tp.parsers import *
from archivos_tp.algoritmo import *

def main():
    archivo_listado = sys.argv[1]
    archivo_mensajes = sys.stdin
    
    posibles_palabras = cargar_palabras(archivo_listado)
    mensajes_a_analizar = cargar_mensajes(archivo_mensajes)

    cant_lineas_invalidas = 0
    lineas_invalidas = []
    contador_lineas = 1

    for linea in mensajes_a_analizar:
        opt, indices = algoritmo(linea, posibles_palabras)
        
        if not opt[len(linea)]:
            print("\033[31mNo es un mensaje\033[0m")
            cant_lineas_invalidas += 1
            lineas_invalidas.append(contador_lineas)

        else:
            palabras = reconstruccion(linea, indices, len(linea))
            for palabra in palabras:
                print(palabra, end=" ")
            print()  # para el salto de línea

        contador_lineas += 1

    print(f"\nCantidad de líneas del archivo: {contador_lineas - 1}")
    print(f"Cantidad de líneas inválidas del archivo: {cant_lineas_invalidas}")
    print(f"Líneas inválidas: {lineas_invalidas}")
    
if __name__ == "__main__":
    main()