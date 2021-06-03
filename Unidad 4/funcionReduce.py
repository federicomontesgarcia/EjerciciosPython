from functools import reduce

lista = [1,2,3,4]

def funcion_acumulador(acumulador = 0, elemento = 0):
    return acumulador + elemento

resultado = reduce(funcion_acumulador, lista)
print("con reduce",resultado)

print()
#--------------------------

resultado = reduce(lambda acumulador = 0, elemento = 0 : acumulador + elemento, lista)
print("con reduce y lambda",resultado)

print()
#----------------------------

lista = ['python', 'java', 'ruby', 'elixir']

resultado = reduce(lambda acumulador = '', elemento = '' : acumulador + ' ' + elemento, lista)
print(resultado)

print()
#----------------------------

items = [1,2,3,4,5,6,7,8,9,10]
suma10 = reduce(lambda x, y: x + y, items, 10)
print(suma10)






