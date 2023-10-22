""" Agregaciones
Podemos aplicar funciones de summary similar a SQL. Estas funciones resumen los valores en una columna o en varias columnas y proporcionan información estadística útil sobre los datos.

Ejemplos de uso de estas funciones son:

Suma (sum()): Calcula la suma de los valores en una columna o en varias columnas. Por ejemplo: """

import pandas as pd

data = {'Nombre': ['Ana', 'Juan', 'Pedro'],
        'Edad': [25, 30, 35],
        'Puntuación': [80, 90, 85]}
df = pd.DataFrame(data)

suma_edades = df['Edad'].sum()
suma_puntuaciones = df['Puntuación'].sum()

print(suma_edades)
print(suma_puntuaciones)
""" Salida:

90
255 """

#Promedio (mean()): Calcula el promedio de los valores en una columna o en varias columnas. Por ejemplo:

promedio_edades = df['Edad'].mean()
promedio_puntuaciones = df['Puntuación'].mean()

print(promedio_edades)
print(promedio_puntuaciones)
""" Salida:

30.0
85.0 """

""" Mínimo (min()) y máximo (max()): Encuentra el valor mínimo y máximo en una columna o en varias columnas. Por ejemplo: """

min_edad = df['Edad'].min()
max_puntuacion = df['Puntuación'].max()

print(min_edad)
print(max_puntuacion)
""" Salida:

25
90 """

#Mediana (median()): Calcula la mediana de los valores en una columna o en varias columnas. Por ejemplo:

mediana_edades = df['Edad'].median()
mediana_puntuaciones = df['Puntuación'].median()

print(mediana_edades)
print(mediana_puntuaciones)
""" Salida:

30.0
85.0 """

#Conteo (count()): Cuenta el número de valores no nulos en una columna o en varias columnas. Por ejemplo:

conteo_edades = df['Edad'].count()
conteo_puntuaciones = df['Puntuación'].count()

print(conteo_edades)
print(conteo_puntuaciones)
""" Salida:

3
3 """

""" Se pueden combinar estas funciones con el agrupamiento para obtener estadísticas más detalladas:

Group By (groupby()): La función groupby() se utiliza para agrupar los datos en un DataFrame según una o varias columnas. Una vez que has agrupado los datos, puedes aplicar agregaciones en cada grupo. """

import pandas as pd

data = {'Ciudad': ['Madrid', 'Barcelona', 'Madrid', 'Valencia', 'Barcelona'],
        'Edad': [25, 30, 35, 25, 28],
        'Puntuación': [80, 90, 85, 95, 75]}
df = pd.DataFrame(data)

# Agrupar por ciudad y calcular el promedio de edad y puntuación en cada grupo
promedios_por_ciudad = df.groupby('Ciudad').mean()
print(promedios_por_ciudad)
""" Salida:

             Edad  Puntuación
Ciudad
Barcelona     29.0        82.5
Madrid        30.0        82.5
Valencia      25.0        95.0 """

#----------------------------------------------------------------

""" Creación de cubos de datos: Un cubo de datos es una forma de agrupar y resumir datos multidimensionales utilizando múltiples columnas de agrupación. Puedes utilizar la función groupby() con varias columnas para crear cubos de datos y aplicar agregaciones en cada combinación única de valores de esas colúmnas: """

# Agrupar por ciudad y edad, y calcular el promedio de puntuación en cada combinación de ciudad y edad
cubo_datos = df.groupby(['Ciudad', 'Edad']).mean()
print(cubo_datos)
""" Salida:

                 Puntuación
Ciudad    Edad
Barcelona 28           75.0
          30           90.0
Madrid    25           80.0
          35           85.0
Valencia  25           95.0 """