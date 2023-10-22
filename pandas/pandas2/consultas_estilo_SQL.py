""" Consultas estilo SQL
Se pueden realizar consultas similares a SQL utilizando el método query() en un DataFrame.
Sea:
  Nombre  Edad     Ciudad
0    Ana    25     Madrid
1   Juan    30  Barcelona
2  Pedro    35     Madrid
3    Ana    25   Valencia
4  María    28  Barcelona 

Podemos realizar consultas como:

1.Consulta básica: Para seleccionar las filas donde la edad sea mayor que 25, puedes escribir lo siguiente: """

import pandas as pd
df = pd.DataFrame()

resultado = df.query('Edad > 25')
print(resultado)
""" Salida:

Nombre  Edad     Ciudad
1   Juan    30  Barcelona
2  Pedro    35     Madrid
4  María    28  Barcelona """

#2.Consulta con operadores lógicos: Para seleccionar las filas donde la edad sea mayor que 25 y la ciudad sea 'Madrid', puedes utilizar operadores lógicos:

resultado = df.query('Edad > 25 and Ciudad == "Madrid"')
print(resultado)
""" Salida:

Nombre  Edad  Ciudad
2  Pedro    35  Madrid """

#3.Consulta con uso de variables: Puedes utilizar variables para realizar consultas más complejas. Por ejemplo, vamos a definir una variable ciudad_busqueda y seleccionar las filas que coincidan con la ciudad almacenada en esa variable:

ciudad_busqueda = 'Barcelona'
resultado = df.query('Ciudad == @ciudad_busqueda')
print(resultado)
""" Salida:

Nombre  Edad     Ciudad
1   Juan    30  Barcelona
4  María    28  Barcelona """