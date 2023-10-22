""" Manejo de duplicados
La manipulación de duplicados es una parte importante del procesamiento de datos. Pandas proporciona herramientas para detectar y manejar duplicados en un DataFrame.

Considere el siguiente DataFrame de ejemplo: """

import pandas as pd

data = {
    'Nombre': ['Ana', 'Juan', 'Pedro', 'Ana', 'María'],
    'Edad': [25, 30, 35, 25, 28],
    'Ciudad': ['Madrid', 'Barcelona', 'Madrid', 'Valencia', 'Barcelona']
}

df = pd.DataFrame(data)
print(df)
""" Salida: """
"""  """
"""   Nombre  Edad     Ciudad """
""" 0    Ana    25     Madrid """
""" 1   Juan    30  Barcelona """
""" 2  Pedro    35     Madrid """
""" 3    Ana    25   Valencia """
""" 4  María    28  Barcelona """

#----------------------------------------------------------------

""" 1.Detectar duplicados:

duplicated(): Este método se utiliza para detectar filas duplicadas en un DataFrame. Devuelve una máscara booleana con True en las posiciones donde existen duplicados y False en las posiciones no duplicadas. Por ejemplo: """

# Detectar filas duplicadas en todo el DataFrame
print(df.duplicated())
""" Salida:

0    False
1    False
2    False
3    True
4    False
dtype: bool """

""" -drop_duplicates(): Este método se utiliza para eliminar filas duplicadas de un DataFrame. Por defecto, mantiene la primera aparición de cada conjunto de duplicados y elimina las siguientes. Por ejemplo:
 """
# Eliminar filas duplicadas en todo el DataFrame
df_sin_duplicados = df.drop_duplicates()
print(df_sin_duplicados)
""" Salida:

Nombre  Edad     Ciudad
0    Ana    25     Madrid
1   Juan    30  Barcelona
2  Pedro    35     Madrid
3    Ana    25   Valencia
4  María    28  Barcelona """

#----------------------------------------------------------------
""" 
2.Manipulación de duplicados:

keep en drop_duplicates(): Puedes utilizar el argumento keep en el método drop_duplicates() para especificar qué duplicados mantener. Los valores posibles son:

keep='first' (predeterminado): Mantiene la primera aparición de cada conjunto de duplicados y elimina las siguientes.
keep='last': Mantiene la última aparición de cada conjunto de duplicados y elimina las anteriores.
keep=False: Elimina todas las filas que contienen duplicados. """

# Mantener la última aparición de cada conjunto de duplicados
df_ultima_aparicion = df.drop_duplicates(keep='last')
print(df_ultima_aparicion)
""" Salida:

Nombre  Edad     Ciudad
1   Juan    30  Barcelona
2  Pedro    35     Madrid
3    Ana    25   Valencia
4  María    28  Barcelona """

# Eliminar todas las filas que contienen duplicados
df_sin_duplicados = df.drop_duplicates(keep=False)
print(df_sin_duplicados)
""" Salida:

Nombre  Edad     Ciudad
1   Juan    30  Barcelona
2  Pedro    35     Madrid
4  María    28  Barcelona """

#----------------------------------------------------------------
""" 
3.Conteo de valores

value_counts(): Proporciona un recuento de la frecuencia de cada valor único en la columna especificada. """

ciudad_counts = df['Ciudad'].value_counts()
print(ciudad_counts)
""" Barcelona    2
Madrid       2
Valencia     1
Name: Ciudad, dtype: int64 """

""" El método value_counts() también puede aceptar algunos argumentos opcionales, como normalize y sort. Por ejemplo, si deseas obtener los conteos normalizados (porcentajes), puedes establecer normalize=True """

ciudad_counts_normalized = df['Ciudad'].value_counts(normalize=True)
print(ciudad_counts_normalized)    
""" Barcelona    0.4
Madrid       0.4
Valencia     0.2
Name: Ciudad, dtype: float64
En este caso, el resultado muestra las proporciones de cada valor único en la columna "Ciudad". """