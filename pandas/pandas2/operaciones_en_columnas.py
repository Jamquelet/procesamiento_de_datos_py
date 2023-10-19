""" Operaciones en columnas

Similar al paradigma establecido con NumPy, Pandas provee funciones a nivel de colúmna que permiten vectorizar ciertas operaciones. Algunas de estas funciones son:

apply(): El método apply() se utiliza para aplicar una función a lo largo de una columna o fila en un DataFrame. Puedes pasar una función predefinida, una función anónima (lambda) o incluso una función personalizada. Por ejemplo, puedes aplicar la función sum() para obtener la suma de una columna específica:
# Aplicar la función sum a la columna 'Columna1'
resultado = df['Columna1'].apply(sum)

.str: El atributo .str se utiliza para acceder a métodos y atributos de cadenas de texto en una columna, permitiendo realizar operaciones dentro de esta. Por ejemplo, puedes utilizar .str.lower() para convertir todos los elementos de una columna de texto en minúsculas:
# Convertir todos los elementos de la columna 'Nombre' a minúsculas
df['Nombre'] = df['Nombre'].str.lower()

map(): El método map() se utiliza para mapear valores de una columna a nuevos valores. Puedes proporcionar un diccionario o una función para realizar la asignación. Por ejemplo, puedes asignar nuevos valores a una columna basándote en un diccionario de mapeo:
# Mapear valores de la columna 'Categoría' a nuevos valores
mapeo = {'A': 'Alto', 'B': 'Medio', 'C': 'Bajo'}
df['Categoría'] = df['Categoría'].map(mapeo)

fillna(): El método fillna() se utiliza para reemplazar valores faltantes (NaN) en una columna con un valor específico. Puedes proporcionar un valor único o utilizar métodos como 'bfill' (backward fill) o 'ffill' (forward fill) para propagar valores de forma hacia atrás o hacia adelante. Por ejemplo, puedes reemplazar los valores faltantes en una columna con ceros:
# Reemplazar los valores faltantes en la columna 'Cantidad' con ceros
df['Cantidad'] = df['Cantidad'].fillna(0)
 """