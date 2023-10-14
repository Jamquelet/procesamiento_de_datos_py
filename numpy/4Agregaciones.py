#Agregaciones
#NumPy tiene varias funciones de agregación incorporadas para trabajar con arreglos

""" 
---> Media (Promedio)= medida que se utiliza para representar el valor típico o central de un conjunto de datos
Media = (Suma de todos los valores) / (Cantidad de valores)
La media proporciona una idea de la tendencia central de los datos y es útil para resumir datos numéricos, puede verse afectada por valores extremos (valores atípicos) en el conjunto de datos.

---> Desviación Estándar: es una medida de dispersión que indica cuánto se alejan los valores individuales de la media en un conjunto de datos, mide la variabilidad o la propagación de los datos.Una desviación estándar más pequeña indica que los valores tienden a estar cerca de la media, mientras que una desviación estándar más grande indica que los valores están más dispersos.
 """
""" import numpy as np

# Supongamos que tienes un arreglo de datos
datos = np.array([1, 2, 3, 4, 5])

# Calcular la media 
media = np.mean(datos)

# Calcular la desviación estándar
desviacion_estandar = np.std(datos)

print("Media:", media)
print("Desviación estándar:", desviacion_estandar) """

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

#------------------------------------------------------------------------------------------------------------------

#Agregaciones multidimensionales: Un tipo común de operación de agregación es un agregado a lo largo de una fila o columna.

#Digamos que tienes algunos datos almacenados en un arreglo bidimensional:

M = np.random.random((3, 4))
print(M)
""" 
[[ 0.8967576   0.03783739  0.75952519  0.06682827]
 [ 0.8354065   0.99196818  0.19544769  0.43447084]
 [ 0.66859307  0.15038721  0.37911423  0.6687194 ]]
 """
#Por defecto, cada función de agregación de NumPy devolverá el agregado sobre todo el arreglo:
M.sum() #6.0850555667307118

#Las funciones de agregación toman un argumento adicional que especifica el eje a lo largo del cual se calcula el agregado. Por ejemplo, podemos encontrar el valor mínimo dentro de cada columna especificando axis=0:
M.min(axis=0)#array([ 0.66859307,  0.03783739,  0.19544769,  0.06682827])

#La función devuelve cuatro valores, correspondientes a las cuatro columnas de números.

#De manera similar, podemos encontrar el valor máximo dentro de cada fila:
M.max(axis=1)
#array([ 0.8967576 ,  0.99196818,  0.6687194 ])

#La palabra clave axis especifica la dimensión del arreglo que se colapsará, en lugar de la dimensión que se devolverá. Por lo tanto, especificar axis=0 significa que se colapsará el primer eje: para arreglos bidimensionales, esto significa que se agregarán los valores dentro de cada columna.

