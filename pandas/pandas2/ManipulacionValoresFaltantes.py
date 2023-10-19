""" Manipulación de valores faltantes

La manipulación de valores faltantes, como NaN (Not a Number) u otros valores nulos, es una parte importante del procesamiento de datos. Pandas proporciona varias herramientas para detectar y manipular valores faltantes en un DataFrame.

Sea el siguiente dataframe: """

import pandas as pd
import numpy as np

data = {
    'A': [1, 2, np.nan, 4, 5],
    'B': [np.nan, 2, 3, np.nan, 6],
    'C': [7, 8, 9, 10, np.nan]
}

df = pd.DataFrame(data)
print(df)
""" salida:
     A    B     C
0  1.0  NaN   7.0
1  2.0  2.0   8.0
2  NaN  3.0   9.0
3  4.0  NaN  10.0
4  5.0  6.0   NaN
 """

""" 1.Detectar valores faltantes: isna() y isnull(): Estos métodos se utilizan para detectar valores faltantes en un DataFrame. Devuelven una máscara booleana con True en las posiciones donde existen valores faltantes y False en las posiciones no faltantes. Por ejemplo: """

# Detectar valores faltantes en todo el DataFrame
print(df.isna())
""" salida
    A      B      C
0  False   True  False
1  False  False  False
2   True  False  False
3  False   True  False
4  False  False   True
 """
# Detectar valores faltantes en una columna específica
print(df['B'].isnull())
""" salida:
0     True
1    False
2    False
3     True
4    False
Name: B, dtype: bool """

#----------------------------------------------------------------

""" 2.Sustituir valores faltantes:

a.fillna(): Este método se utiliza para reemplazar los valores faltantes con un valor específico. Puedes proporcionar un valor único para reemplazar todos los valores faltantes o utilizar métodos como 'bfill' (backward fill) o 'ffill' (forward fill) para propagar los valores no faltantes hacia atrás o hacia adelante, respectivamente. Por ejemplo:
 """
# Reemplazar todos los valores faltantes con cero
df.fillna(0)

# Reemplazar los valores faltantes con los valores no faltantes más cercanos
df.fillna(method='bfill')  # backward fill
df.fillna(method='ffill')  # forward fill

df_filled = df.fillna(0)
print(df_filled)  
""" salida:
     A    B     C
0  1.0  0.0   7.0
1  2.0  2.0   8.0
2  0.0  3.0   9.0
3  4.0  0.0  10.0
4  5.0  6.0   0.0
 """

df_bfill = df.fillna(method='bfill')
print(df_bfill)
""" salida:
     A    B     C
0  1.0  2.0   7.0
1  2.0  2.0   8.0
2  4.0  3.0   9.0
3  4.0  6.0  10.0
4  5.0  6.0   NaN  

 """

df_ffill = df.fillna(method='ffill')
print(df_ffill)
""" salida: 
     A    B     C
0  1.0  NaN   7.0
1  2.0  2.0   8.0
2  2.0  3.0   9.0
3  4.0  3.0  10.0
4  5.0  6.0  10.0  
 """

""" b.dropna(): Este método se utiliza para eliminar filas o columnas que contengan valores faltantes. Puedes especificar el eje (axis) en el que deseas realizar el filtrado. Por ejemplo:
 """
# Eliminar todas las filas que contienen al menos un valor faltante
df.dropna()

# Eliminar todas las columnas que contienen al menos un valor faltante
df.dropna(axis=1)

df_dropped = df.dropna()
print(df_dropped)  
""" salida:
     A    B    C
1  2.0  2.0  8.0    
 """