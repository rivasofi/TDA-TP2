import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from random import seed

from matplotlib import pyplot as plt
import seaborn as sns
import numpy as np
import scipy as sp

from util import time_algorithm

from script import *

from archivos_tp.algoritmo import algoritmo

from archivos_tp.parsers import *




def graficar_medicion_L_variable(results, x_2):
    ax: plt.Axes
    fig, ax = plt.subplots()
    ax.plot(x_2, [results[i] for i in x_2], label="Medición")
    ax.set_title('Tiempo de ejecución de comparar transacciones')
    ax.set_xlabel('Cantidad de transacciones')
    ax.set_ylabel('Tiempo de ejecución (s)')
    None

    # scipy nos pide una función que recibe primero x y luego los parámetros a ajustar:
    f = lambda x_2, c1, c2: c1 * x_2**2 + c2 

    c, pcov = sp.optimize.curve_fit(f, x_2, [results[n] for n in x_2])


    print(f"c_1 = {c[0]}, c_2 = {c[1]}")
    r = np.sum((c[0] * x_2 **2 + c[1] - [results[n] for n in x_2])**2)
    print(f"Error cuadrático total: {r}")
    ax.plot(x_2, [c[0] * n **2 + c[1] for n in x_2], 'r--', label="Ajuste")
    ax.legend()
    fig.savefig(f"ajuste-L_variable.png", dpi=300, bbox_inches='tight')
    graficar_error_L_variable(c, results, x_2)


def graficar_error_L_variable(c, results, x_2):
    ax: plt.Axes
    fig, ax = plt.subplots()
    errors = [np.abs(c[0] * n **2 + c[1] - results[n]) for n in x_2]
    ax.plot(x_2, errors)
    ax.set_title('Error de ajuste')
    ax.set_xlabel('Cantidad de transacciones')
    ax.set_ylabel('Error absoluto (s)')
    None
    fig.savefig(f"error-L_variable.png", dpi=300, bbox_inches='tight')



def graficar_medicion_n_variable(results, x):
    ax: plt.Axes
    fig, ax = plt.subplots()
    ax.plot(x, [results[i] for i in x], label="Medición")
    ax.set_title('Tiempo de ejecución de algoritmo') #CHEQUEAR NAME
    ax.set_xlabel('Largo cadena recibida')
    ax.set_ylabel('Tiempo de ejecución (s)')
    None

    # scipy nos pide una función que recibe primero x y luego los parámetros a ajustar:
    f = lambda x, c1, c2: c1 * x + c2 

    c, pcov = sp.optimize.curve_fit(f, x, [results[n] for n in x])


    print(f"c_1 = {c[0]}, c_2 = {c[1]}")
    r = np.sum((c[0] * x + c[1] - [results[n] for n in x])**2)
    print(f"Error cuadrático total: {r}")
    ax.plot(x, [c[0] * n + c[1] for n in x], 'r--', label="Ajuste")
    ax.legend()
    fig.savefig(f"ajuste-n_variable.png", dpi=300, bbox_inches='tight')
    graficar_error_n_variable(c, results, x)


def graficar_error_n_variable(c, results, x):
    ax: plt.Axes
    fig, ax = plt.subplots()
    errors = [np.abs(c[0] * n + c[1] - results[n]) for n in x]
    ax.plot(x, errors)
    ax.set_title('Error de ajuste')
    ax.set_xlabel('Largo cadena recibida')
    ax.set_ylabel('Error absoluto (s)')
    None
    fig.savefig(f"error-n_variable.png", dpi=300, bbox_inches='tight')


#Cantidad transacciones es la cantidad de transacciones a generar, es_la_rata es un bool que indica si el archivo va a devolver que es la rata o no, 
# error_maximo es el error maximo que se puede tener en la transaccion, distancia_maxima es la distancia maxima entre transacciones, 
# inicio es un bool que indica si la transaccion que no encaja estará al inicio (si es true) o al final (si es false) y 
# tipo_de_solapamiento es el tipo de solapamiento que se va a usar (sin solapamientos, solapamientos parciales o solapamiento total)
def crear_cadenas_y_medir_n(palabras_por_linea):
    
    archivo_diccionario = "../diccionario_local.txt"
    archivo_palabras = "palabras-30.txt"
    archivo_cadenas = f"{palabras_por_linea}_in.txt"

    n = 30
    l_min = 7  # modificar para cambiar L
    diccionario_local = obtener_diccionario_local(archivo_diccionario)
    if not os.path.exists(archivo_palabras):
        diccionario_artificial = generar_palabras(diccionario_local, n, l_min)
        escribir_archivo_palabras(diccionario_artificial, archivo_palabras)
    else:
        # Cargar desde el archivo único ya existente
        diccionario_artificial = cargar_palabras(archivo_palabras)

    # generar archivo con cadenas de texto
    

    n_lineas = 2
    num_invalidas = 0
    generar_cadenas(diccionario_local, diccionario_artificial, n_lineas, palabras_por_linea, num_invalidas, archivo_cadenas)
    
    posibles_palabras = cargar_palabras(archivo_palabras)
    mensajes_a_analizar = cargar_mensajes(archivo_cadenas)

    for linea in mensajes_a_analizar:
        algoritmo(linea, posibles_palabras)


def crear_cadenas_y_medir_L(palabra_mas_larga):
    
    archivo_diccionario = "../diccionario_local.txt"
    archivo_palabras = f"palabras-Lmin_{palabra_mas_larga}.txt"
    archivo_cadenas = f"16_in-Lmin_{palabra_mas_larga}.txt"

    
    n = 30
    l_min = palabra_mas_larga  # modificar para cambiar L
    diccionario_local = obtener_diccionario_local(archivo_diccionario)

    diccionario_artificial = generar_palabras(diccionario_local, n, l_min)
    escribir_archivo_palabras(diccionario_artificial, archivo_palabras)
    
    palabras_por_linea = 16
    n_lineas = 2
    num_invalidas = 0
    generar_cadenas(diccionario_local, diccionario_artificial, n_lineas, palabras_por_linea, num_invalidas, archivo_cadenas)
    
    posibles_palabras = cargar_palabras(archivo_palabras)
    mensajes_a_analizar = cargar_mensajes(archivo_cadenas)

    for linea in mensajes_a_analizar:
        algoritmo(linea, posibles_palabras)


def funcion_a_medir_n_variable(palabras_por_linea):
    return crear_cadenas_y_medir_n(palabras_por_linea)


def funcion_a_medir_L_variable(palabra_mas_larga):
    return crear_cadenas_y_medir_L(palabra_mas_larga)

# def medir_tiempo():
#     if tipo_solapamiento == "sin_solapamientos" and es_la_rata:
#         results = time_algorithm(funcion_a_medir, x, lambda cantidad_transacciones: [cantidad_transacciones])
#         return results
    
def obtener_volumenes(minimo, maximo, cantidad):
    return np.linspace(minimo, maximo, cantidad).astype(int)


if __name__ == '__main__':
    seed (12345)
    np.random.seed(12345)
    sns.set_theme()

    x = obtener_volumenes(5001, 50000, 10)

    x_2 = obtener_volumenes(25, 70, 10)


    


    # results_x = time_algorithm(funcion_a_medir_n_variable, x, lambda palabras_por_linea: [palabras_por_linea])

    # graficar_medicion_n_variable(results_x, x)
    #Medir con varios valores en un n variable (variar )

    results_x_2 = time_algorithm(funcion_a_medir_L_variable, x_2, lambda palabra_mas_larga: [palabra_mas_larga])

    graficar_medicion_L_variable(results_x_2, x_2)
    


    

