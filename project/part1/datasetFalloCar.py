#convertir la lista de edades a un arreglo de NumPy y calcular el promedio de edad de las personas participantes en el estudio.
import numpy as np
from datasets import load_dataset

dataset = load_dataset("mstz/heart_failure")#estructura similar a un diccionario con particiones de datos y características

data = dataset["train"] #accedemos a todos los registos indexando por esa partición

age_list  = np.array([data['age']])
print(age_list)

age_avg = np.mean(age_list) 
print(age_avg)

""" 

# Suponiendo que ya tienes cargados los datos en 'data'

# Obtén la lista de edades
edades = data["age"]

# Convierte la lista de edades en un arreglo de NumPy
edades_np = np.array(edades)

# Calcula el promedio de edades
promedio_edades = np.mean(edades_np)

# Imprime el resultado
print("El promedio de edad de las personas participantes en el estudio es:", promedio_edades)
 """