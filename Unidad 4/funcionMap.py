def cuadrado(elemento = 0):
    return elemento * elemento

lista = [1,2,3,4,5,6,7,8,9,10]
#---------------------------------

resultado = list(map(cuadrado, lista))
print("con map",resultado)

print()
#---------------------------------

resultado = list( map( lambda elemento : elemento * elemento, lista))
print("con map y lambda",resultado)

print()
#----------------------------------
from math import pow
print(pow(2,3))

numeros = [2,3,4]
potencias = [3,2,4]

potenciados = float
potenciados = map(pow, numeros, potencias)
resultado = list(potenciados)
print(resultado)