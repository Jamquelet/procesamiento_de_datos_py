#ejemplo 1
""" Supongamos que trabajas en una empresa minorista y tienes datos de ventas almacenados en un arreglo de NumPy. Cada fila del arreglo representa una transacción de venta y las columnas contienen información como el ID del producto, la cantidad vendida, el precio unitario, etc.

Tu objetivo es analizar los datos y extraer información estadística relevante. Utilizando las funciones de agregación de NumPy, puedes realizar diferentes cálculos sobre los datos de ventas. """

import numpy as np

# Datos de ventas (ejemplo simplificado)
ventas = np.array([
    [1, 10, 5.99],
    [2, 5, 3.49],
    [3, 8, 4.99],
    [4, 12, 2.99],
])

total_ventas = np.sum(ventas[:, 1])  # Suma de la cantidad vendida
promedio_precio = np.mean(ventas[:, 2])  # Promedio del precio unitario
max_cantidad = np.max(ventas[:, 1])  # Cantidad máxima vendida
min_precio = np.min(ventas[:, 2])  # Precio mínimo unitario

print("Total de ventas:", total_ventas) #35.0
print("Precio promedio:", promedio_precio) #4.365
print("Cantidad máxima vendida:", max_cantidad)# 12.0
print("Precio mínimo unitario:", min_precio)#2.99

#----------------------------------------------------------------

#ejemplo 2

""" Supongamos que tienes un conjunto de datos que representa las temperaturas máximas diarias registradas en diferentes ciudades durante una semana. Los datos están almacenados en un arreglo bidimensional llamado temperaturas con la forma (7, 3), donde las filas representan los días de la semana y las columnas representan las diferentes ciudades. También tienes un arreglo unidimensional llamado ajuste de dimensión (3), que contiene los ajustes de temperatura que deseas aplicar a cada ciudad. """

import numpy as np

temperaturas = np.array([[25, 28, 30],
                         [27, 29, 31],
                         [26, 27, 29],
                         [23, 25, 28],
                         [24, 26, 29],
                         [26, 28, 30],
                         [28, 30, 32]])

ajuste = np.array([2, 1, 3])

#Ahora, supongamos que deseas aplicar el ajuste de temperatura a cada ciudad de manera eficiente utilizando broadcasting. Simplemente puedes realizar la operación de suma entre temperaturas y ajuste, y NumPy aplicará automáticamente el broadcasting para que las dimensiones coincidan correctamente:

temperaturas_ajustadas = temperaturas + ajuste
print(temperaturas_ajustadas)

#El resultado será un nuevo arreglo temperaturas_ajustadas con la misma forma que temperaturas (7, 3), donde cada valor de temperatura se ha ajustado según el valor correspondiente en el arreglo ajuste.
""" 
[[27 29 33]
 [29 30 34]
 [28 28 32]
 [25 26 31]
 [26 27 32]
 [28 29 33]
 [30 31 35]] """