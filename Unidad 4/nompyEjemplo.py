import numpy as np
a = np.array([34, 25, 7])
print(type(a))

a = np.array([34,25,7])
print("la suma de los elementos es:",a.sum())

matriz = np.zeros((3,3))   # Crear una matriz de todos los ceros
print(matriz) 
print()

x = np.array([[1,2],[3,4]], dtype=np.float64)
y = np.array([[5,6],[7,8]], dtype=np.float64)

#Suma de elementos; ambos producen la matriz
# [[ 6.0  8.0]
#  [10.0 12.0]]
print(x + y)
print("suma de matrices")
print(np.add(x, y))
print("resta de matrices")
print(np.subtract(x, y))
print("multiplicacion de elementos")
print(np.multiply(x, y))
print("division de elementos")
print(np.divide(x, y))
print("raiz cuadrada")
print(np.sqrt(x))