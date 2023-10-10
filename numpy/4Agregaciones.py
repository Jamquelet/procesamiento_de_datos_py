#Agregaciones
#NumPy tiene varias funciones de agregación incorporadas para trabajar con arreglos

#Suma de los valores en un arreglo: 
#consideremos calcular la suma de todos los valores en un arreglo. Python en sí mismo puede hacer esto utilizando la función sum incorporada:

import numpy as np
L = np.random.random(100)
sum(L)
#55.61209116604941

#La sintaxis es bastante similar a la función sum de NumPy, y el resultado es el mismo en el caso más simple:
np.sum(L)
#55.612091166049424

#Sin embargo, debido a que ejecuta la operación en código compilado, la versión de NumPy de la operación se calcula mucho más rapido:

big_array = np.random.rand(1000000)
"""
%timeit sum(big_array)
%timeit np.sum(big_array)
 """
#10 loops, best of 3: 104 ms per loop
# 1000 loops, best of 3: 442 µs per loop

#Sin embargo, ten cuidado: la función sum y la función np.sum no son idénticas, ¡lo que a veces puede generar confusión! En particular, sus argumentos opcionales tienen diferentes significados y np.sum puede manejar arreglos de múltiples dimensiones.

#------------------------------------------------------------------------------

#Mínimo y máximo
#Python tiene las funciones incorporadas min y max, que se utilizan para encontrar el valor mínimo y el valor máximo de cualquier arreglo dado:

min(big_array), max(big_array)
#(1.1717128136634614e-06, 0.9999976784968716)

#Las funciones correspondientes de NumPy tienen una sintaxis similar y, nuevamente, se ejecutan mucho más rápido:
np.min(big_array), np.max(big_array) #(1.1717128136634614e-06, 0.9999976784968716)
"""
 %timeit min(big_array)
%timeit np.min(big_array)

10 loops, best of 3: 82.3 ms per loop
1000 loops, best of 3: 497 µs per loop """

#Para min, max, sum y varios otros agregados de NumPy, hay una sintaxis más corta para usar los métodos del propio objeto de arreglo:
print(big_array.min(), big_array.max(), big_array.sum())
#1.17171281366e-06 0.999997678497 499911.628197


