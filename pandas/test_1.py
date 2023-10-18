""" Dado el siguiente CSV:

Fecha,Producto,Cantidad,Precio
2023-01-02,Producto A,10,15.99
2023-01-03,Producto B,5,10.99
2023-01-04,Producto A,8,12.99
2023-01-05,Producto C,3,8.99
2023-01-06,Producto B,6,9.99 """

import pandas as pd

# Cargar el archivo CSV en un DataFrame
data = pd.read_csv("data.csv")

# Convierte la columna "Fecha" al tipo datetime
data['Fecha'] = pd.to_datetime(data['Fecha'])

# Convierte la columna "Cantidad" al tipo entero inplace
data['Cantidad'] = data['Cantidad'].astype(int)

# Establece la columna "Fecha" como índice inplace
data.set_index('Fecha', inplace=True)

# Filtrar el DataFrame para mostrar ventas a partir del 2023-01-04
ventas_desde_2023_01_04 = data['2023-01-04':]

# Guardar el resultado en un archivo CSV llamado "resultado_1.csv"
ventas_desde_2023_01_04.to_csv("resultado_1.csv")

# Filtrar el DataFrame para mostrar las ventas del "Producto A"
ventas_producto_a = data[data['Producto'] == 'Producto A']

# Guardar el resultado en un archivo CSV llamado "resultado_2.csv"
ventas_producto_a.to_csv("resultado_2.csv")

# Verifica el tipo de datos de la columna "Fecha" después de la conversión
print(data.dtypes)

# Verifica el nuevo índice
print(data)

#------------------------------------------------------------------------

#pytest

import pandas as pd

def ej_1_cargar_csv() -> pd.DataFrame:
    df = pd.read_csv("datos.csv")
    return df

def ej_2_convertir_fecha(df: pd.DataFrame) -> None:
    df['Fecha'] = pd.to_datetime(df['Fecha'])

def ej_3_convertir_cantidad(df: pd.DataFrame) -> None:
    df['Cantidad'] = df['Cantidad'].astype(int)

def ej_4_fecha_como_indice(df: pd.DataFrame) -> None:
    df['Fecha'] = pd.to_datetime(df['Fecha'])
    df.set_index('Fecha', inplace=True)

def ej_5_filtrar_por_fecha(df: pd.DataFrame) -> pd.DataFrame:
    df = df[df.index >= '2023-01-04']
    df.to_csv("resultado_1.csv")
    return df

def ej_6_filtrar_por_producto(df: pd.DataFrame) -> pd.DataFrame:
    df = df[df['Producto'] == 'Producto A']
    df.to_csv("resultado_2.csv")
    return df



