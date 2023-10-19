""" Filtrado Avanzado

Podemos utilizar todas las funciones a nivel de colúmnas aprendidas hasta ahora para filtrar datos con mayor granularidad.

1.Filtrado con múltiples condiciones: Puedes utilizar operadores lógicos como & (and), | (or) y ~ (not) para combinar múltiples condiciones en una expresión de filtrado. Por ejemplo, para filtrar filas donde el valor de la columna "A" sea mayor que 5 y el valor de la columna "B" sea menor que 10, puedes utilizar:

df_filtrado = df[(df['A'] > 5) & (df['B'] < 10)]

2.Filtrado basado en condiciones complejas: Puedes utilizar funciones lógicas y de comparación más complejas utilizando los métodos isin(), between(), .str.startswith(), .str.endswith(), .str.contains() y otros. Estos métodos te permiten especificar condiciones más específicas para filtrar los datos. Por ejemplo, para filtrar filas donde el valor de la columna "C" comienza con la letra "A" y la columna "D" contiene la cadena "XYZ", puedes utilizar:

df_filtrado = df[df['C'].str.startswith('A') & df['D'].str.contains('XYZ')]

3.Filtrado utilizando una función personalizada: Puedes utilizar una función personalizada en combinación con el método apply() para aplicar una lógica de filtrado más compleja a tus datos. La función debe devolver True o False para cada fila del DataFrame, y luego puedes usar esta función en el filtro. Por ejemplo, si tienes una función mi_funcion() que define una lógica personalizada de filtrado, puedes aplicarla de la siguiente manera:

df_filtrado = df[df["col"].apply(mi_funcion)]
 """