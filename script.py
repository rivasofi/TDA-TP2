import random

# recibe la ruta al archivo con todas las palabras
# devuelve una lista con todas sus palabras que usaremos para armar el set de datos (debe ser lista para hacer random.choice)
def obtener_diccionario_local(archivo_diccionario):
    with open(archivo_diccionario, "r") as archivo:
        palabras = archivo.read().splitlines()
    
    return palabras  # lista con las miles de palabras (debe ser lista, para hacer random.choice)

# recibe la lista con palabras del diccionario local, y una cantidad n de palabras a seleccionar del mismo
# devuelve un set con las palabras que seleccionó para el archivo de palabras
def generar_diccionario_artificial(diccionario_local, n):
    palabras_seleccionadas = random.sample(diccionario_local, n)
    
    return set(palabras_seleccionadas)

# recibe el set con palabras seleccionadas y las escribe en un archivo
def escribir_diccionario_artificial_en_archivo(diccionario_artificial, archivo_palabras):
    with open(archivo_palabras, "w") as archivo:
        for palabra in diccionario_artificial:
            archivo.write(palabra + "\n")

# genera las líneas (cadenas) válidas e inválidas y las escribe en el archivo de cadenas
# recibe:
    # el diccionario local (para generar cadenas inválidas)
    # el diccionario que creamos a partir del local, para crear cadenas válidas
    # cantidad de líneas (cadenas) a generar para el archivo
    # cantidad de palabras que tendrá cada línea
    # de las líneas totales, la cantidad que queramos que sean cadenas inválidas
def generar_cadenas_encriptadas(diccionario_local, diccionario_artificial, cant_lineas, palabras_por_linea, cant_invalidas, archivo_cadenas):
    lineas = []
    
    if cant_invalidas > cant_lineas:
        cant_invalidas = cant_lineas
    
    # generamos posiciones aleatorias para las líneas inválidas
    posiciones_invalidas = random.sample(range(cant_lineas), cant_invalidas)
    cant_invalidas_generadas = 0

    # generar cadenas válidas e inválidas
    for i in range(cant_lineas):
        es_valida = i not in posiciones_invalidas
        cant_palabras = 0
        palabras_linea = []
        
        while cant_palabras < palabras_por_linea:
            if es_valida:
                palabra = random.choice(list(diccionario_artificial))  # sólo agarra palabras válidas

                palabras_linea.append(palabra)
                linea = "".join(palabras_linea)
                cant_palabras += 1
            
            else:
                palabra = random.choice(diccionario_local)

                if palabra not in diccionario_artificial:  # sólo agarra palabras inválidas
                    palabras_linea.append(palabra)
                    linea = "".join(palabras_linea)
                    cant_palabras += 1
                    cant_invalidas_generadas += 1

        lineas.append(linea)
    
    with open(archivo_cadenas, "w") as archivo:
        for linea in lineas:
            archivo.write(linea + "\n")


if __name__ == "__main__":
    archivo_diccionario = "diccionario_local.txt"
    archivo_palabras = "palabras.txt"
    archivo_cadenas = "mensaje.txt"
    
    # generar archivo con palabras
    n = 10
    diccionario_local = obtener_diccionario_local(archivo_diccionario)
    diccionario_artificial = generar_diccionario_artificial(diccionario_local, n)
    escribir_diccionario_artificial_en_archivo(diccionario_artificial, archivo_palabras)

    # generar archivo con cadenas de texto
    n_lineas = 5
    palabras_por_linea = 20
    num_invalidas = 3 
    generar_cadenas_encriptadas(diccionario_local, diccionario_artificial, n_lineas, palabras_por_linea, num_invalidas, archivo_cadenas)