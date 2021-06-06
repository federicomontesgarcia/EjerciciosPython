#Crear una función que retorne las palabras de una lista de palabras que comience con una
#letra en específico. Utilizar la función filter.

def filtro_palabras(lista_palabras, letra):
    return list(filter(lambda word:word[0]==letra,lista_palabras))
filtro = filtro_palabras(['Perro', 'Gato', 'Pelota', 'Manzana', 'Libro', 'Python'], 'P')
['Perro', 'Pelota', 'Python']
print(filtro)
