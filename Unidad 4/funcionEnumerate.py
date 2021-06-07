#Realizar una función que tome una lista y retorne un diccionario que contenga los valores de
#la lista como clave y el índice como el valor. Utilizar la función enumerate.

def d_list(L):
    return {key:value for value,key in enumerate(L)}
lista = d_list(['a','b','c','d','e'])
print(lista)
