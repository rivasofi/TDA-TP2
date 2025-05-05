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




def graficar_medicion_L_variable(results, L_min):
    ax: plt.Axes
    fig, ax = plt.subplots()
    ax.plot(x, [results[i] for i in x], label="Medición")
    ax.set_title('Tiempo de ejecución de comparar transacciones')
    ax.set_xlabel('Cantidad de transacciones')
    ax.set_ylabel('Tiempo de ejecución (s)')
    None

    # scipy nos pide una función que recibe primero x y luego los parámetros a ajustar:
    f = lambda x, c1, c2: c1 * x * np.log2(x) + c2 

    c, pcov = sp.optimize.curve_fit(f, x, [results[n] for n in x])


    print(f"c_1 = {c[0]}, c_2 = {c[1]}")
    r = np.sum((c[0] * x **2 + c[1] - [results[n] for n in x])**2)
    print(f"Error cuadrático total: {r}")
    ax.plot(x, [c[0] * n **2 + c[1] for n in x], 'r--', label="Ajuste")
    ax.legend()
    fig.savefig(f"ajuste--.png", dpi=300, bbox_inches='tight')
    graficar_error_L_variable(c, results, L_min)


def graficar_error_L_variable(c, results, L_min):
    ax: plt.Axes
    fig, ax = plt.subplots()
    errors = [np.abs(c[0] * n **2 + c[1] - results[n]) for n in x]
    ax.plot(x, errors)
    ax.set_title('Error de ajuste')
    ax.set_xlabel('Cantidad de transacciones')
    ax.set_ylabel('Error absoluto (s)')
    None
    fig.savefig(f"error--.png", dpi=300, bbox_inches='tight')



def graficar_medicion_n_variable(results, largo_cadena):
    ax: plt.Axes
    fig, ax = plt.subplots()
    ax.plot(x, [results[i] for i in x], label="Medición")
    ax.set_title('Tiempo de ejecución de algoritmo') #CHEQUEAR NAME
    ax.set_xlabel('Largo cadena recibida')
    ax.set_ylabel('Tiempo de ejecución (s)')
    None

    # scipy nos pide una función que recibe primero x y luego los parámetros a ajustar:
    f = lambda x, c1, c2: c1 * x**2 + c2 

    c, pcov = sp.optimize.curve_fit(f, x, [results[n] for n in x])


    print(f"c_1 = {c[0]}, c_2 = {c[1]}")
    r = np.sum((c[0] * x + c[1] - [results[n] for n in x])**2)
    print(f"Error cuadrático total: {r}")
    ax.plot(x, [c[0] * n + c[1] for n in x], 'r--', label="Ajuste")
    ax.legend()
    fig.savefig(f"ajuste--.png", dpi=300, bbox_inches='tight')
    graficar_error_n_variable(c, results, largo_cadena)


def graficar_error_n_variable(c, results, largo_cadena):
    ax: plt.Axes
    fig, ax = plt.subplots()
    errors = [np.abs(c[0] * n + c[1] - results[n]) for n in x]
    ax.plot(x, errors)
    ax.set_title('Error de ajuste')
    ax.set_xlabel('Largo cadena recibida')
    ax.set_ylabel('Error absoluto (s)')
    None
    fig.savefig(f"error--.png", dpi=300, bbox_inches='tight')


#Cantidad transacciones es la cantidad de transacciones a generar, es_la_rata es un bool que indica si el archivo va a devolver que es la rata o no, 
# error_maximo es el error maximo que se puede tener en la transaccion, distancia_maxima es la distancia maxima entre transacciones, 
# inicio es un bool que indica si la transaccion que no encaja estará al inicio (si es true) o al final (si es false) y 
# tipo_de_solapamiento es el tipo de solapamiento que se va a usar (sin solapamientos, solapamientos parciales o solapamiento total)
def crear_cadenas_y_medir(cantidad_transacciones, es_la_rata, error_maximo, distancia_maxima, inicio, tipo_de_solapamiento):
    if es_la_rata:
        nombre_archivo = f"{cantidad_transacciones}-es.txt"
    else:
        nombre_archivo = f"{cantidad_transacciones}-no-es.txt"
    if tipo_de_solapamiento == "sin_solapamientos":
        sin_solapamientos(cantidad_transacciones, nombre_archivo, error_maximo, distancia_maxima, es_la_rata, inicio)
    ruta_completa = f"../archivos_test/{nombre_archivo}"

    transacc_sospechosas = obtener_transacciones_aproximadas(ruta_completa)
    transacc_sospechoso = obtener_transacciones_sospechoso(ruta_completa)
    cant = obtener_cantidad_transacciones(ruta_completa)

    comparar_transacciones(transacc_sospechosas, transacc_sospechoso, cant)


def funcion_a_medir(cantidad_transacciones):
    return crear_cadenas_y_medir(cantidad_transacciones, True, 20, 10, False, "sin_solapamientos")


def medir_tiempo_para_solapamiento(tipo_solapamiento, es_la_rata):
    if tipo_solapamiento == "sin_solapamientos" and es_la_rata:
        results = time_algorithm(funcion_a_medir, x, lambda cantidad_transacciones: [cantidad_transacciones])
        return results
    
def obtener_volumenes_n(minimo_transacciones, maximo_transacciones, cantidad_archivos):
    return np.linspace(minimo_transacciones, maximo_transacciones, cantidad_archivos).astype(int)

if __name__ == '__main__':
    seed (12345)
    np.random.seed(12345)
    sns.set_theme()

    x = obtener_volumenes_n(5001, 100000, 20)


    #Medir con varios valores en un n variable (variar )
    results_sin_solapamientos = medir_tiempo_para_solapamiento("sin_solapamientos", True)
    graficar_medicion(results_sin_solapamientos, "sin_solapamientos", 100000)   




    

