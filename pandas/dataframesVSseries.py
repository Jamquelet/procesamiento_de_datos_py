""" Dataframe vs Series
Vamos a clarificar la diferencia entre un DataFrame y una Serie de Python.

Un DataFrame es una estructura de datos bidimensional que consta de filas y columnas, similar a una tabla o una hoja de cálculo. Puede contener múltiples columnas, donde cada columna puede ser de un tipo de dato diferente. Se utiliza para representar y manipular conjuntos de datos estructurados.

Por otro lado, una Serie es una estructura de datos unidimensional etiquetada que puede contener datos de cualquier tipo. Una Serie se puede considerar como una columna de un DataFrame o un conjunto de datos unidimensional con una etiqueta de índice (ya sea numérico o no). """

#DataFrame:
import pandas as pd

data = {'Nombre': ['Juan', 'María', 'Pedro'],
        'Edad': [25, 30, 27],
        'Ciudad': ['Madrid', 'Barcelona', 'Sevilla']}

df = pd.DataFrame(data)
print(df)
""" Salida:

  Nombre  Edad     Ciudad
0   Juan    25     Madrid
1  María    30  Barcelona
2  Pedro    27    Sevilla """

#----------------------------------------------------------------

#Serie:
import pandas as pd

nombres = pd.Series(['Juan', 'María', 'Pedro'])
print(nombres)
""" Salida:

0     Juan
1    María
2    Pedro
dtype: object """