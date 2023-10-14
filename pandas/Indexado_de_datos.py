""" Indexado de datos
Podemos indexar los datos por fila y por colúmna

1. Indexación de columnas:

Acceso por nombre de columna: Puedes acceder a una columna específica utilizando la notación de corchetes [] y el nombre de la columna como índice. Por ejemplo, df['nombre_columna'] devuelve una Serie con los datos de la columna llamada 'nombre_columna'.

Acceso por atributo: Si el nombre de la columna es un identificador de Python válido, también puedes acceder a la columna utilizando la notación de punto ., es decir, df.nombre_columna. Esta forma de acceso es conveniente si el nombre de la columna no contiene espacios ni caracteres especiales.

2. Indexación de filas:

Acceso por índice numérico: Pandas asigna automáticamente un índice numérico a las filas del DataFrame. Puedes acceder a una fila específica utilizando la notación de corchetes [] y el número de índice de la fila. Por ejemplo, df.iloc[0] devuelve una Serie con los datos de la primera fila.

Acceso por etiqueta de índice: Si has asignado etiquetas personalizadas a las filas, puedes acceder a una fila utilizando la función .loc[] y la etiqueta de índice correspondiente. Por ejemplo, df.loc['etiqueta_fila'] devuelve una Serie con los datos de la fila que tiene la etiqueta 'etiqueta_fila'.

3. Indexación combinada:

Acceso por nombre de columna y etiqueta de fila: Puedes combinar la indexación de columnas y filas para acceder a un elemento específico del DataFrame. Por ejemplo, df.loc['etiqueta_fila', 'nombre_columna'] devuelve el valor ubicado en la intersección de la fila con la etiqueta 'etiqueta_fila' y la columna con el nombre 'nombre_columna'.
Es importante tener en cuenta que el indexado en pandas es inclusivo en el extremo inicial y exclusivo en el extremo final. Por ejemplo, al usar .iloc[0:3], se obtendrán las filas con índices 0, 1 y 2, pero no se incluirá la fila con índice 3. """

#----------------------------------------------------------------

""" Ejemplo con índice numérico
Supongamos que tienes el siguiente DataFrame: """

import pandas as pd

data = {'Nombre': ['Juan', 'María', 'Pedro'],
        'Edad': [25, 30, 27],
        'Ciudad': ['Madrid', 'Barcelona', 'Sevilla']}

df = pd.DataFrame(data)

""" El DataFrame se verá así:

  Nombre  Edad     Ciudad
0   Juan    25     Madrid
1  María    30  Barcelona
2  Pedro    27    Sevilla """

#----------------------------------------------------------------

#1. Acceso a una columna específica:

columna_edad = df['Edad']
print(columna_edad)
""" Salida:

0    25
1    30
2    27
Name: Edad, dtype: int64 
En este ejemplo, accedemos a la columna 'Edad' utilizando la notación de corchetes []. Esto devuelve una Serie que contiene los valores de la columna 'Edad'."""

#----------------------------------------------------------------

#2. Acceso a una fila específica:

fila_1 = df.iloc[1]
print(fila_1)

""" Salida:

Nombre        María
Edad             30
Ciudad    Barcelona
Name: 1, dtype: object
En este caso, utilizamos la función iloc[] para acceder a la segunda fila (índice 1) del DataFrame. Se devuelve una Serie que contiene los valores de la fila correspondiente. """

#----------------------------------------------------------------

#3. Acceso a un elemento específico:

elemento = df.loc[0, 'Ciudad']
print(elemento)
#Salida:Madrid

#----------------------------------------------------------------

""" Ejemplo con índice custom
Como se explicó arriba, es posible especificar un índice no numérico al crear el DataFrame o al modificarlo posteriormente.

Sea el dataframe anterior, podemos especificarle un índice propio, no numérico: """

import pandas as pd

data = {'Nombre': ['Juan', 'María', 'Pedro'],
        'Edad': [25, 30, 27],
        'Ciudad': ['Madrid', 'Barcelona', 'Sevilla']}

# Especificar un índice no numérico
index = ['a', 'b', 'c']

df = pd.DataFrame(data, index=index)

""" El DataFrame se verá así:

  Nombre  Edad     Ciudad
a   Juan    25     Madrid
b  María    30  Barcelona
c  Pedro    27    Sevilla 

En este ejemplo, se proporciona una lista de etiquetas (index) al crear el DataFrame. Cada etiqueta se asigna a una fila correspondiente en el DataFrame. Ahora, las filas están etiquetadas con las letras 'a', 'b' y 'c' en lugar de los índices numéricos predeterminados."""

#Luego, puedes acceder a las filas utilizando estas etiquetas no numéricas mediante el uso de la función .loc[]. Por ejemplo:
fila_b = df.loc['b']
print(fila_b)

""" Salida:

Nombre        María
Edad             30
Ciudad    Barcelona
Name: b, dtype: object

También se pueden asignar etiquetas personalizadas a las filas en cualquier momento después de la creación del DataFrame utilizando el atributo index. Por ejemplo:

df.index = ['x', 'y', 'z']
Esto cambiará el índice del DataFrame para que las filas estén etiquetadas como 'x', 'y' y 'z'. Luego puedes utilizar estas etiquetas personalizadas en las operaciones de indexación. """
