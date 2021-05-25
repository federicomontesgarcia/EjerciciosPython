#listas compuestas

lista = [[1,2,3], [4,5,6], [7,8,9], [10,11,12]]
print(lista)

for k in range (len(lista)):
    for x in range (len(lista[k])):
        print(lista[k][x])

