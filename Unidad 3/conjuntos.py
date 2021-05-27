s = set()

s = {True, 3.14, None, False, "Hola mundo", (1, 2)}

print(s)

#los elementos de la lista se insertan en un conjunto
s1 = set([1, 2, 3, 4])

s2 = set(range(10))
print(s1)
print(s2)

#convirtiendo conjunto en lista
print(list({1, 2, 3, 4}))
#convirtiendo lista en conjunto
print(set([1, 2, 2, 3, 4]))

# Crea un conjunto con una serie de elementos entre llaves
# Los elementos repetidos se eliminan
c = {1, 3, 2, 9, 3, 1}
print(c)
# Crea un conjunto a partir de un string
# Los caracteres repetidos se eliminan
a = set('Hola Pythonista')
print(a)
# Crea un conjunto a partir de una lista
# Los elementos repetidos de la lista se eliminan
unicos = set([3, 5, 6, 1, 5])
print(unicos)