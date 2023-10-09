#Operaciones Vectorizadas

""" La lentitud de los bucles: 

La implementación predeterminada de Python (conocida como CPython) realiza algunas operaciones de manera muy lenta. Esto se debe en parte a la naturaleza dinámica e interpretada del lenguaje: el hecho de que los tipos sean flexibles, lo que impide que las secuencias de operaciones se compilen en un código de máquina eficiente como en lenguajes como C y Fortran. Recientemente ha habido varios intentos de abordar esta debilidad: ejemplos conocidos son el proyecto PyPy, una implementación de Python compilada en tiempo real (JIT); el proyecto Cython, que convierte el código Python en código C compilable; y el proyecto Numba, que convierte fragmentos de código Python en un bytecode rápido de LLVM. Cada uno de estos enfoques tiene sus fortalezas y debilidades, pero es seguro decir que ninguno de los tres ha superado hasta ahora el alcance y la popularidad del motor CPython estándar. 

#La relativa lentitud de Python generalmente se manifiesta en situaciones donde se repiten muchas operaciones pequeñas, por ejemplo, recorrer arreglos para operar en cada elemento. Por ejemplo, imaginemos que tenemos un arreglo de valores y queremos calcular el recíproco de cada uno. Un enfoque directo podría ser el siguiente: """

import numpy as np
np.random.seed(0)

def compute_reciprocals(values):
    output = np.empty(len(values))
    for i in range(len(values)):
        output[i] = 1.0 / values[i]
    return output
        
values = np.random.randint(1, 10, size=5)
compute_reciprocals(values)

#array([ 0.16666667,  1.        ,  0.25      ,  0.25      ,  0.125     ])

#Esta implementación probablemente se sienta bastante natural para alguien con experiencia en C o Java. Pero si medimos el tiempo de ejecución de este código para una entrada grande, veremos que esta operación es muy lenta, ¡quizás sorprendentemente lenta! Lo mediremos con la magia %timeit de IPython (que se discute en Perfilado y cronometraje de código):

#big_array = np.random.randint(1, 100, size=1000000)%timeit compute_reciprocals(big_array)
#1 loop, best of 3: 2.91 s per loop

""" ¡Toma varios segundos realizar estas millones de operaciones y almacenar el resultado! Cuando incluso los teléfonos celulares tienen velocidades de procesamiento medidas en Giga-FLOPS (es decir, miles de millones de operaciones numéricas por segundo), esto parece absurdamente lento. Resulta que el cuello de botella aquí no son las operaciones en sí, sino la verificación de tipos y las llamadas de función que CPython debe realizar en cada ciclo del bucle. Cada vez que se calcula el recíproco, Python primero examina el tipo del objeto y busca dinámicamente la función correcta para ese tipo. Si estuviéramos trabajando en código compilado, esta especificación de tipo sería conocida antes de que se ejecute el código y el resultado se podría calcular de manera mucho más eficiente. """

#------------------------------------------------------------------------------

#Vectorización de operaciones:
#Para muchos tipos de operaciones, NumPy proporciona una interfaz conveniente para este tipo de rutinas compiladas de tipo estático. Esto se conoce como una operación vectorizada. Esto se puede lograr simplemente realizando una operación en el arreglo, la cual se aplicará a cada elemento. Este enfoque vectorizado está diseñado para trasladar el bucle a la capa compilada que subyace en NumPy, lo que resulta en una ejecución mucho más rápida.

#Compara los resultados de los siguientes ejemplos:
print(compute_reciprocals(values))
print(1.0 / values)
