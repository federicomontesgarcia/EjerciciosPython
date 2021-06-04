def mayor_a_cinco(elemento):
    return elemento > 5

tupla = (5,2,6,7,8,10,77,55,2,1,30,4,22,3)
#-------------------------------

resultado = tuple(filter(mayor_a_cinco, tupla))
print("con filter",resultado)

print()
#---------------------------------

resultado = tuple(filter( lambda elemento : elemento > 5, tupla))
print("con filter y lambda:",resultado)

#--------------------------------
items = [1,2,3,4,5,6,7,8,9]

pares = filter(lambda x: x % 2 == 0, items)
print(pares)