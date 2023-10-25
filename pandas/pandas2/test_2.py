import pandas as pd
""" 
Sea el siguiente CSV:

Nombre,Edad,Puntuacion
Estudiante1,20,85.5
Estudiante2,21,75.0
Estudiante3,19,92.5
Estudiante4,22,80.2
Estudiante5,20,88.9
Estudiante6,21,76.8
Estudiante7,19,94.2
Estudiante8,22,82.1
Estudiante9,20,87.3
Estudiante10,21,77.6

Calcula lo siguiente usando Pandas:

Cargar el dataframe
Obtener la puntuación promedio de los estudiantes mayores de 20 años.
Obtener el nombre de los estudiantes cuya puntuación sea mayor a 85 y la edad sea menor a 22.
Obtener la edad y la cantidad de estudiantes por cada edad. Ordena los resultados por edad de forma descendente. (Usa .reset_index(drop=True) al final de tu operación).
Obtener la edad promedio de los estudiantes que tienen una puntuación mayor a 80.
"""

def ej_1_cargar_csv() -> pd.DataFrame:
    df = pd.read_csv('datos.csv') 
    return df

def ej_2_puntuacion_promedio(df: pd.DataFrame) -> float:
    resultado = df[df['Edad'] > 20]['Puntuacion'].mean()
    return resultado
    pass 


def ej_3_nombre_estudiantes(df: pd.DataFrame) -> list[str]:
    r = df[(df['Puntuacion'] > 85) & (df['Edad'] < 22)]['Nombre']
    return r
    pass

def ej_4_edad_y_cantidad(df: pd.DataFrame) -> pd.DataFrame:
    if 'Edad' in df:
        result = df['Edad'].value_counts().reset_index()
        result.columns = ['Edad', 'Cantidad']
        result = result.sort_values(by='Edad', ascending=False).reset_index(drop=True)
        return result
    else:
        # Si la columna 'Edad' no existe en el DataFrame, puedes manejar esta situación apropiadamente.
        return pd.DataFrame()  # O cualquier otro valor por defecto o manejo de error que prefieras

""" def ej_4_edad_y_cantidad(df: pd.DataFrame) -> pd.DataFrame:
    edades_conteo = df['Edad'].value_counts().reset_index().rename(columns={'index': 'Edad','Edad': 'Cantidad'}).sort_values(by='Edad', ascending=False).reset_index(drop=True)
    return edades_conteo
 """
"""   # Obtener el conteo de estudiantes por edad
edades_conteo = df['Edad'].value_counts().reset_index()

# Renombrar las columnas para mayor claridad
edades_conteo.columns = ['Edad', 'Cantidad']

# Ordenar los resultados por edad de forma descendente
edades_conteo = edades_conteo.sort_values(by='Edad', ascending=False)

# Reiniciar el índice para tener un índice secuencial
edades_conteo = edades_conteo.reset_index(drop=True) """


def ej_5_edad_promedio(df: pd.DataFrame) -> float:
    r= df[df['Puntuacion']>80]['Edad'].mean()
    return r
