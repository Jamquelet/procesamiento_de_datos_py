#pytest -k <nombre-test> -rPx : Comando para ejecutar un solo test y mostrar la salida de los prints dentro

""" Se te dará una función a implementar para cada uno de los siguientes ejercicios en el archivo solucion.py, una vez almacenas los resultados en las variables descritas en cada ejercicio, retorna sus valores para poder realizar la validación de tu solución, por ejemplo, para el ejercicio 1:
 """
def ej_1_get_array() -> np.ndarray:
    temperaturas = []# Crea el arreglo aquí
    return temperaturas

""" Crea un arreglo de NumPy llamado temperaturas que contenga las siguientes temperaturas en grados Celsius: 25, 30, 27, 22, 29, 31, 26, 28.

Calcula la media y la desviación estándar de las temperaturas utilizando las funciones de agregación de NumPy. Almacena los resultados en variables llamadas media y desviacion.

Convierte las temperaturas de grados Celsius a grados Fahrenheit utilizando la fórmula F = C * 9/5 + 32, donde F representa los grados Fahrenheit y C representa los grados Celsius. Almacena los resultados en un nuevo arreglo NumPy llamado temperaturas_fahrenheit.

Encuentra la temperatura máxima y mínima en el arreglo temperaturas_fahrenheit utilizando las funciones de agregación de NumPy. Almacena los resultados en variables llamadas temp_max y temp_min.

Crea un arreglo NumPy llamado diferencias que contenga las diferencias entre cada temperatura en el arreglo temperaturas y la temperatura media calculada anteriormente.

Calcula el cuadrado de cada diferencia en el arreglo diferencias utilizando la función de NumPy para operaciones matemáticas element-wise. Almacena los resultados en un nuevo arreglo NumPy llamado diferencias_cuadrado.

Calcula la suma de todos los elementos en el arreglo diferencias_cuadrado utilizando la función de agregación de NumPy. Almacena el resultado en una variable llamada suma_cuadrados.

Calcula la raíz cuadrada de la suma de cuadrados utilizando la función de NumPy para operaciones matemáticas element-wise. Almacena el resultado en una variable llamada raiz_suma_cuadrados. """


import numpy as np
from typing import Tuple


def ej_1_get_array() -> np.ndarray:
    # TODO: retornar el array del ejercicio 1
    pass


def ej_2_media_std(array: np.ndarray) -> Tuple[np.ndarray, np.ndarray]:
    # TODO: Retorna (media, std) en ese orden
    pass


def ej_3_temperaturas(array: np.ndarray) -> np.ndarray:
    pass


def ej_4_min_max(
    temperaturas_fahrenheit: np.ndarray
) -> Tuple[np.ndarray, np.ndarray]:
    # TODO: Retorna (temp_min, temp_max) en ese orden
    pass


def ej_5_diferencias(temperaturas: np.ndarray, media: float) -> np.ndarray:
    pass


def ej_6_cuadrado(diferencias: np.ndarray) -> np.ndarray:
    pass


def ej_7_suma(diferencias_cuadrado: np.ndarray) -> float:
    pass


def ej_8_raiz(suma_cuadrados: float) -> float:
    pass
