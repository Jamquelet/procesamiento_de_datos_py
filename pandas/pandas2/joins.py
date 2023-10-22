""" Joins
Existen dos formas de combinar dataframes, usando las funciones merge() y concat().

merge(): La función merge() se utiliza para combinar dos DataFrames en función de una o más columnas comunes, similar a la operación JOIN en SQL.
La sintaxis es
 """
import pandas as pd
left_df = pd.DataFrame()
right_df = pd.DataFrame()

merged_df = pd.merge(left_df, right_df, on='columna_comun')
""" Donde:

left_df y right_df son los DataFrames que deseas combinar.
'columna_comun' es el nombre de la columna en la que se realizará la unión.
Además de on, también puedes especificar otros parámetros opcionales como how, left_on, right_on, etc., para controlar el tipo de unión y las columnas de unión cuando los nombres no son iguales en ambos DataFrames.

Ejemplo:
 """
import pandas as pd

# DataFrames de ejemplo
df1 = pd.DataFrame({'id': [1, 2, 3], 'nombre': ['Juan', 'María', 'Carlos']})
df2 = pd.DataFrame({'id': [1, 2, 3], 'edad': [25, 30, 35]})

# Combinar los DataFrames en función de la columna 'id'
merged_df = pd.merge(df1, df2, on='id')

print(merged_df)
""" Salida:

   id  nombre  edad
0   1    Juan    25
1   2   María    30
2   3  Carlos    35 """

#concat(): El método concat() se utiliza para concatenar DataFrames a lo largo de un eje específico (ya sea a lo largo de las filas o a lo largo de las columnas). Puedes concatenar varios DataFrames en función de tus necesidades.

import pandas as pd

# DataFrame 1
data1 = {'ID': [1, 2, 3],
         'Nombre': ['Ana', 'Juan', 'Pedro']}
df1 = pd.DataFrame(data1)

# DataFrame 2
data2 = {'ID': [4, 5, 6],
         'Nombre': ['María', 'Luis', 'Sofía']}
df2 = pd.DataFrame(data2)

# Concatenar los DataFrames a lo largo de las filas
df_concat = pd.concat([df1, df2], axis=0)
print(df_concat)
""" Salida:

   ID Nombre
0   1    Ana
1   2   Juan
2   3  Pedro
0   4  María
1   5   Luis
2   6  Sofía
En este ejemplo, los DataFrames df1 y df2 se concatenan a lo largo de las filas utilizando axis=0, lo que resulta en un DataFrame combinado con todas las filas de ambos DataFrames.
 """
