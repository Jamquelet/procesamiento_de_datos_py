#Broadcasting

#Recordemos que para arreglos del mismo tamaño, las operaciones binarias se realizan elemento por elemento:
import numpy as np
a = np.array([0, 1, 2])
b = np.array([5, 5, 5])
a + b
#array([5, 6, 7])

#El broadcasting permite que este tipo de operaciones binarias se realicen en arreglos de diferentes tamaños; por ejemplo, podemos sumar un escalar (pensado como un arreglo de dimensiones cero) a un arreglo:
a + 5
#array([5, 6, 7])

#Podemos pensar en esta operación como una extensión o duplicación del valor 5 en el arreglo [5, 5, 5] y luego se suman los resultados.

#De manera similar, podemos extender esta idea a arreglos de dimensiones superiores.
#Ejemplo: Sumando un arreglo unidimensional a un arreglo bidimensional:
M = np.ones((3, 3))
M
""" 
array([[1., 1., 1.],
       [1., 1., 1.],
       [1., 1., 1.]]) """
M + a
""" 
array([[1., 2., 3.],
       [1., 2., 3.],
       [1., 2., 3.]]) """

#Aquí, el arreglo unidimensional a se estira o expande a lo largo de la segunda dimensión para que coincida con la forma de M.

#El broadcasting también se puede aplicar a ambos operandos, por ejemplo:
a = np.arange(3)
b = np.arange(3)[:, np.newaxis]

print(a)
print(b)
""" 
[0 1 2]
[[0]
 [1]
 [2]] """

a + b
""" 
array([[0, 1, 2],
       [1, 2, 3],
       [2, 3, 4]]) """
#Al igual que antes, hemos estirado o expandido un valor para que coincida con la forma del otro arreglo. En este caso, hemos estirado tanto a como b para que tengan una forma común, un arreglo bidimensional

