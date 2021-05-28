#ejemplo de como hallar la cantidad de veces que un numero se repite

original = ['2','3','3','8','4','7','2','9','9','2','3','4','7','7','2','4','8','9','9']
print("todos los numeros caidos son:",original)
caidos = set(original)
print("Los números caídos en conjunto son:",caidos)
caidos = list(caidos)
print("Los números caídos en lista son:",caidos)

i = 0
k = 0
num = []
rep = []
numRep = [num, rep]

for l in range (len(caidos)):
    num.append(caidos[i])
    cant = 0
    j = 0
    for k in range (len(original)):
        if int(caidos[i]) == int(original[j]):
            cant = cant + 1
        j = j + 1
        
    rep.append(cant)
    i = i + 1 

print(numRep)

#Imprimir la cantidad de veces que un numero se repite 
i = 0
j = 0
for numero in num:
    print("el numero",num[i],"se repite",rep[j],"veces")
    i = i + 1
    j = j + 1
         