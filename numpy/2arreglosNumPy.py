#Conceptos básicos de arreglos de NumPy

#ATRIBUTOS DE UN ARRAY

#1.Tamaño de los arreglos: Puedes obtener el tamaño de un arreglo utilizando el atributo size. Este atributo devuelve el número total de elementos en el arreglo.

import numpy as np

arr = np.array([1, 2, 3, 4, 5])
print("Tamaño del arreglo:", arr.size)
#salida: Tamaño del arreglo: 5

#----------------------------------------------------------------

#2. Forma de los arreglos: El atributo shape te permite conocer la estructura del arreglo, es decir, el número de elementos en cada dimensión. Si tienes un arreglo unidimensional, el atributo shape devolverá una tupla con un solo valor que representa el tamaño del arreglo. Si tienes un arreglo multidimensional, shape devolverá una tupla con el tamaño en cada dimensión.

arr = np.array([[1, 2, 3], [4, 5, 6]])
print("Forma del arreglo:", arr.shape)
#salida: Forma del arreglo: (2, 3)

#----------------------------------------------------------------

#3. Consumo de memoria de los arreglos: El atributo nbytes te permite saber cuánta memoria está ocupando el arreglo en bytes. Es útil para evaluar la eficiencia del uso de memoria de tu código.

arr = np.array([1, 2, 3, 4, 5])
print("Consumo de memoria:", arr.nbytes, "bytes")
#salida: Consumo de memoria: 20 bytes

#----------------------------------------------------------------

#4.Tipos de datos de los arreglos: Puedes utilizar el atributo dtype para obtener el tipo de datos de los elementos en el arreglo. NumPy ofrece varios tipos de datos, como int, float, bool, string, entre otros.

arr = np.array([1, 2, 3, 4, 5])
print("Tipo de datos del arreglo:", arr.dtype)
#salida: Tipo de datos del arreglo: int64

#------------------------------------------------------------------------------------------------------------------------

#INDEXADO: El indexado en NumPy se realiza utilizando corchetes [] y puede ser de una o varias dimensiones, dependiendo de la forma del arreglo.

#1. Indexado unidimensional: Si tienes un arreglo unidimensional, puedes acceder a los elementos individuales utilizando un índice entre corchetes. El índice comienza en cero para el primer elemento y va incrementando de uno en uno.

import numpy as np

arr = np.array([1, 2, 3, 4, 5])
print("Elemento en la posición 2:", arr[2])
#salida: Elemento en la posición 2: 3

#----------------------------------------------------------------

#2. Indexado multidimensional: Si tienes un arreglo multidimensional, el indexado se realiza especificando el índice en cada dimensión separado por comas. Puedes acceder a elementos individuales o a subarreglos utilizando esta notación.

arr = np.array([[1, 2, 3], [4, 5, 6]])
print("Elemento en la posición (1, 2):", arr[1, 2])
#salida: Elemento en la posición (1, 2): 6

#----------------------------------------------------------------

#3. Establecer el valor de un elemento: Además de obtener valores, también puedes establecer nuevos valores en un arreglo.

arr = np.array([1, 2, 3, 4, 5])
arr[2] = 10
print("Arreglo modificado:", arr)
#salida: Arreglo modificado: [ 1  2 10  4  5]

#----------------------------------------------------------------

#4. Indexado con rangos: Puedes utilizar rangos para acceder a subarreglos dentro de un arreglo. Los rangos se especifican utilizando la notación start:end:step, donde start es el índice de inicio (incluido), end es el índice final (excluido) y step es el incremento entre los elementos.

arr = np.array([1, 2, 3, 4, 5])
print("Subarreglo:", arr[1:4])
#salida: Subarreglo: [2 3 4]

#------------------------------------------------------------------------------------------------------------------------

#SLICING: El "slicing" o rebanado es una técnica muy útil para acceder a subarreglos dentro de un arreglo multidimensional. Permite seleccionar porciones específicas del arreglo en una o varias dimensiones, lo que facilita la manipulación y extracción de datos.El rebanado en NumPy se realiza especificando rangos en cada dimensión, separados por comas dentro de los corchetes []. Puedes utilizar los rangos para especificar el inicio (start), fin (stop) y el paso (step) del rebanado.

import numpy as np

arr = np.array([[1, 2, 3, 4], 
                [5, 6, 7, 8], 
                [9, 10, 11, 12]])

# Obtener una porción del arreglo
sub_arr = arr[0:2, 1:3]
print(sub_arr)
#salida: [[2 3][6 7]]
#En este ejemplo, hemos seleccionado una porción del arreglo original arr que incluye las filas de índice 0 y 1, y las columnas de índice 1 y 2. El resultado es un nuevo subarreglo [2 3; 6 7].

#Además de especificar rangos, también puedes omitir valores para seleccionar todas las filas o columnas en una dimensión determinada. Por ejemplo:

# Obtener todas las filas de la tercera columna
column = arr[:, 2]
print(column)
#salida: [ 3  7 11]
#Aquí hemos seleccionado todas las filas (:) y la tercera columna (2) del arreglo arr. El resultado es un nuevo arreglo unidimensional [3 7 11] que contiene los elementos de la tercera columna.

#También puedes utilizar valores negativos en el rebanado para contar desde el final del arreglo. Por ejemplo:

# Obtener las últimas dos filas y las últimas dos columnas
sub_arr = arr[-2:, -2:]
print(sub_arr)
#salida: [[ 7  8] [11 12]]
#En este caso, hemos seleccionado las últimas dos filas (-2:) y las últimas dos columnas (-2:) del arreglo arr, obteniendo un nuevo subarreglo [[7 8]; [11 12]].

#------------------------------------------------------------------------------------------------------------------------

#RESCHAPE: La modificación de la forma de los arreglos en NumPy se refiere a cambiar la estructura o dimensión de un arreglo existente sin modificar sus elementos. Esto se logra utilizando el método reshape() de NumPy.

import numpy as np

# Crear un arreglo unidimensional
arr = np.array([1, 2, 3, 4, 5, 6])

# Cambiar la forma del arreglo a una matriz de 2 filas y 3 columnas
reshaped_arr = arr.reshape(2, 3)
print(reshaped_arr)
#salida: 
# [[1 2 3] 
# [4 5 6]]
# hemos creado un arreglo unidimensional arr con 6 elementos. Luego utilizamos el método reshape() para cambiar su forma a una matriz de 2 filas y 3 columnas. El resultado es el arreglo reshaped_arr, que tiene la forma [[1 2 3]; [4 5 6]].
#La modificación de la forma de un arreglo no altera los elementos en sí, simplemente los reorganiza en una nueva estructura. Es importante tener en cuenta que la cantidad total de elementos en el arreglo original debe ser igual a la cantidad total de elementos en la forma deseada.

# Otro ejemplo con un arreglo bidimensional:

# Crear un arreglo bidimensional de 3x4
arr = np.array([[1, 2, 3, 4],
                [5, 6, 7, 8],
                [9, 10, 11, 12]])

# Cambiar la forma del arreglo a una matriz de 2 filas y 6 columnas
reshaped_arr = arr.reshape(2, 6)
print(reshaped_arr)
#salida: 
# [[ 1  2  3  4  5  6] 
# [ 7  8  9 10 11 12]]
#En este caso, hemos creado un arreglo bidimensional arr de 3 filas y 4 columnas. Luego, utilizamos reshape() para cambiar su forma a una matriz de 2 filas y 6 columnas. El resultado es el arreglo reshaped_arr, que tiene la forma [[1 2 3 4 5 6]; [7 8 9 10 11 12]].

#También es posible utilizar el valor -1 en una dimensión al utilizar reshape(), lo que indica que NumPy debe inferir automáticamente el tamaño adecuado en esa dimensión. Veamos un ejemplo:

# Crear un arreglo unidimensional de 12 elementos
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])

# Cambiar la forma del arreglo a una matriz de 3 filas y tamaño de columna automático
reshaped_arr = arr.reshape(3, -1)
print(reshaped_arr)
#salida: 
# [[ 1  2  3  4]
# [ 5  6  7  8]
# [ 9 10 11 12]]
#En este ejemplo, hemos utilizado reshape() para cambiar la forma del arreglo arr a una matriz de 3 filas y un tamaño de columna automático. NumPy infiere que el tamaño de columna adecuado es 4, lo que resulta en el arreglo reshaped_arr mostrado arriba.

#-----------------------------------------------------------------------------------------------------------------------

#COMBINACIONES DE ARRAYS: NumPy ofrece varias funciones para combinar múltiples arreglos en uno solo. Algunas de las funciones comunes son concatenate(), vstack() y hstack().

import numpy as np

# Crear dos arreglos
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])

# Unir los arreglos utilizando concatenate()
result = np.concatenate((arr1, arr2))
print(result)
#salida: [1 2 3 4 5 6], utilizamos la función concatenate() para unir los arreglos arr1 y arr2 en uno solo. El resultado es un nuevo arreglo [1 2 3 4 5 6].

#También puedes utilizar vstack() para unir arreglos verticalmente (a lo largo del eje 0) o hstack() para unir arreglos horizontalmente (a lo largo del eje 1). Veamos un ejemplo de cada uno:

# Unir arreglos verticalmente utilizando vstack()
result = np.vstack((arr1, arr2))
print(result)
#salida: 
# [[1 2 3]
# [4 5 6]]

# Unir arreglos horizontalmente utilizando hstack()
result = np.hstack((arr1, arr2))
print(result)
#salida: [1 2 3 4 5 6]

#--------------------------------------------------------------------------------------------------------------------

#DIVISIÓN DE ARRAYS: NumPy también ofrece funciones para dividir un arreglo en múltiples arreglos más pequeños. Algunas de las funciones comunes son split(), vsplit() y hsplit().

# Crear un arreglo
arr = np.array([1, 2, 3, 4, 5, 6])

# Dividir el arreglo en tres partes utilizando split()
result = np.split(arr, 3)
print(result)
#SALIDA: [array([1, 2]), array([3, 4]), array([5, 6])], utilizamos la función split() para dividir el arreglo arr en tres partes. El resultado es una lista con tres arreglos más pequeños array([1, 2]), array([3, 4]) y array([5, 6]).

#utilizar vsplit() para dividir un arreglo verticalmente o hsplit() para dividir un arreglo horizontalmente. Veamos un ejemplo de cada uno:

# Dividir el arreglo verticalmente utilizando vsplit()
arr = np.array([[1, 2, 3],
                [4, 5, 6]])

result = np.vsplit(arr, 2)
print(result)
#salida: [array([[1, 2, 3]]), array([[4, 5, 6]])]

# Dividir el arreglo horizontalmente utilizando hsplit()
arr = np.array([[1, 2, 3],
                [4, 5, 6]])

result = np.hsplit(arr, 3)

print(result)
#salida: 
""" [array([[1],
    [4]]),
array([[2],
       [5]]),
array([[3],
       [6]])] """



