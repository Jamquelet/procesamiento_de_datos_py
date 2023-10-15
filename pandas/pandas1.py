""" Pandas
Pandas es una librería open source ampliamente utilizada en el análisis y manipulación de datos en Python. Está construida sobre NumPym, proporciona DataFrames y Series, que permiten trabajar de manera eficiente con datos tabulares y de series de tiempo.

Puede realizar operaciones como la selección de columnas y filas, filtrado, agregación, ordenación y eliminación de datos duplicados. También proporciona métodos para manejar y eliminar datos faltantes, lo que facilita el tratamiento de valores nulos o NaN en los conjuntos de datos.

Los DataFrames y las Series pueden tener índices personalizados, lo que permite un acceso rápido y flexible a los datos utilizando etiquetas en lugar de solo índices numéricos. Esto facilita el procesamiento y la manipulación de datos basados en etiquetas de columna y fila.

Al igual que NumPy, pandas aprovecha las operaciones vectorizadas para realizar cálculos eficientes en grandes conjuntos de datos. Esto significa que puedes realizar operaciones matemáticas y lógicas en columnas enteras o en filas enteras sin la necesidad de iterar explícitamente sobre los elementos. Esto mejora significativamente el rendimiento y la eficiencia computacional.

Proporciona métodos para leer y escribir datos en una variedad de formatos, como CSV, Excel, SQL, JSON y HDF5. Esto facilita la carga de datos desde diferentes fuentes y la exportación de los resultados del análisis en varios formatos. """

""" Ejemplo
Primero instalamos Pandas ejecutando el comando: pip install pandas

Supongamos que tienes un archivo CSV llamado "datos.csv" que contiene los siguientes datos:

nombre,edad,ciudad
Juan,25,Madrid
María,30,Barcelona
Pedro,27,Sevilla
 """
#Podemos leer este archivo de la siguiente forma
#import pandas as pd

# Leer el archivo CSV en un DataFrame
df = pd.read_csv("datos.csv")

# Mostrar el DataFrame
print(df)
""" Salida esperada:

  nombre  edad     ciudad
0   Juan    25     Madrid
1  María    30  Barcelona
2  Pedro    27    Sevilla
 """

#----------------------------------------------------------------

#Conversión de tipos de datos de colúmnas: Se pueden realizar conversiones de tipos de datos en las columnas de un DataFrame.

""" 1. Conversión de tipos de datos durante la creación del DataFrame: Cuando creas un DataFrame, puedes especificar los tipos de datos de las columnas utilizando el argumento dtype dentro del diccionario de datos.

Por ejemplo: """
import pandas as pd

data = {'Nombre': ['Juan', 'María', 'Pedro'],
        'Edad': [25, 30, 27],
        'Ciudad': ['Madrid', 'Barcelona', 'Sevilla']}

df = pd.DataFrame(data, dtype={'Edad': float})

print(df.dtypes)
""" Salida:

Nombre    object
Edad     float64
Ciudad    object
dtype: object """

#----------------------------------------------------------------

#2. Conversión de tipos de datos después de la creación del DataFrame: Puedes realizar conversiones de tipos de datos después de crear el DataFrame utilizando el método astype(). Por ejemplo:
import pandas as pd

data = {'Nombre': ['Juan', 'María', 'Pedro'],
        'Edad': ['25', '30', '27'],
        'Ciudad': ['Madrid', 'Barcelona', 'Sevilla']}

df = pd.DataFrame(data)

# Convertir la columna 'Edad' de str a int
df['Edad'] = df['Edad'].astype(int)

print(df.dtypes)
""" Salida:

Nombre    object
Edad       int32
Ciudad    object
dtype: object """

#----------------------------------------------------------------

#3. Conversión de tipos de datos utilizando funciones de conversión: Pandas también proporciona varias funciones de conversión específicas para transformar los tipos de datos de las columnas. Algunas de estas funciones incluyen to_numeric(), to_datetime(), to_timedelta(), entre otras. Aquí tienes un ejemplo de uso de to_numeric():

import pandas as pd

data = {'Nombre': ['Juan', 'María', 'Pedro'],
        'Edad': ['25', '30', '27'],
        'Ciudad': ['Madrid', 'Barcelona', 'Sevilla']}

df = pd.DataFrame(data)

# Convertir la columna 'Edad' de str a int utilizando to_numeric()
df['Edad'] = pd.to_numeric(df['Edad'])

print(df.dtypes)
""" Salida:

Nombre    object
Edad       int64
Ciudad    object
dtype: object """

#----------------------------------------------------------------

#quiz
#¿Qué es un DataFrame en pandas? 
#Una estructura de datos bidimensional con filas y columnas

#¿Cuál es la función de la función head() en pandas?
#muestra las primeras filas de un dataframe

#¿Cómo se filtran datos en pandas basándose en condiciones?
#utilizando operadores de comparación y condiciones booleanas

#¿Cuál es el método utilizado para convertir el tipo de datos de una columna en pandas?
#astype()

#¿Cuál es la diferencia entre un DataFrame y una Serie en pandas?
#un dataframe puede contener múltiples columnas, mientras que una serie  representa solo una columnas

#¿Cuál es la función de la función info() en pandas?
#Muestra los tipos de datps y la información sobre las columnas de dataframe

#¿Cómo se accede a una columna específica en un DataFrame?
#Utilizando la notación de corchetes [  ] con el nombre de la columna

#¿Cuál es el método utilizado para leer un archivo CSV en pandas? read_csv()