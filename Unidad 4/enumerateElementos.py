#Realizar una función que retorne el recuento de la cantidad de elementos en la lista cuyo
#valor es igual a su índice. Utilizar la función enumerate.

def count_match_index(L):
    return len([num for count,num in enumerate(L) if num==count])
count = count_match_index([0,2,2,1,5,5,6,10])
print(count)