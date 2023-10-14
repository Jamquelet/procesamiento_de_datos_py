""" Filtrado de datos
Pandas proporciona varias formas de filtrar basado en condiciones, esto permite seleccionar subconjuntos de datos que cumplen ciertas condiciones específicas. Esta funcionalidad es útil cuando deseas extraer filas del DataFrame que satisfacen ciertos criterios o combinaciones de criterios, similar a una sentencia WHERE de SQL. """

#----------------------------------------------------------------

""" 1. Operadores de comparación: Puedes utilizar operadores de comparación, como igualdad (==), desigualdad (!=), mayor que (>), menor que (<), mayor o igual que (>=), y menor o igual que (<=), para realizar filtrados basados en condiciones. 

Ejemplo:"""

import pandas as pd

data = {'Nombre': ['Juan', 'María', 'Pedro'],
        'Edad': [25, 30, 27],
        'Ciudad': ['Madrid', 'Barcelona', 'Sevilla']}

df = pd.DataFrame(data)

# Filtrar las filas donde la edad sea mayor que 25
filtro = df['Edad'] > 25
resultados = df[filtro]

print(resultados)
""" Salida:

  Nombre  Edad     Ciudad
1  María    30  Barcelona
2  Pedro    27    Sevilla """

#----------------------------------------------------------------

""" 2. Métodos query() y eval(): Pandas también proporciona los métodos query() y eval() para realizar filtrados avanzados. Estos métodos permiten escribir expresiones más complejas y realizar cálculos en el proceso de filtrado. Aquí tienes un ejemplo: """
import pandas as pd

data = {'Nombre': ['Juan', 'María', 'Pedro'],
        'Edad': [25, 30, 27],
        'Ciudad': ['Madrid', 'Barcelona', 'Sevilla']}

df = pd.DataFrame(data)

# Utilizar el método query() para filtrar las filas donde la edad sea mayor que 25
resultados = df.query('Edad > 25')

print(resultados)
""" Salida:

  Nombre  Edad     Ciudad
1  María    30  Barcelona
2  Pedro    27    Sevilla """

#----------------------------------------------------------------

#3. Combinación de condiciones: Puedes combinar múltiples condiciones utilizando los operadores lógicos & (AND) y | (OR). Por ejemplo:
import pandas as pd

data = {'Nombre': ['Juan', 'María', 'Pedro'],
        'Edad': [25, 30, 27],
        'Ciudad': ['Madrid', 'Barcelona', 'Sevilla']}

df = pd.DataFrame(data)

# Filtrar las filas donde la edad es mayor que 25 y la ciudad es 'Madrid'
filtro = (df['Edad'] > 25) & (df['Ciudad'] == 'Madrid')
resultados = df[filtro]

print(resultados)
""" Salida:

  Nombre  Edad  Ciudad
0   Juan    25  Madrid """
