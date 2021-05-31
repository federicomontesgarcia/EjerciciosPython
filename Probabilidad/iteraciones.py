#ejemplo de como hallar la cantidad de veces que un numero se repite

original = ['201','300','398','821','447','723','206','909','909','201','338','424','748','765','201','463','821','909','909','300']
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

print("Listado de numeros y las veces que se repiten",numRep)

#Imprimir la cantidad de veces que un numero se repite 
i = 0
j = 0
for numero in num:
    print("el numero",num[i],"se repite",rep[j],"veces")
    i = i + 1
    j = j + 1
         
#------------------------------------------------------------
## convertir los numeros de 3 cifras en 1 cifra
total1D = []
total1D0 = []
total1D1 = []
total1D2 = []
i = 0
n = 0
for num in original:
    j = 0
    num1 = ""
    nuevo = original[i]
    for n in nuevo:
        if j == 0:
            num1 = nuevo[j]  
            total1D0.append(num1)
        if j == 1:
            num1 = nuevo[j]  
            total1D1.append(num1)
        if j == 2:
            num1 = nuevo[j]  
            total1D2.append(num1)
        j = j + 1
    i = i + 1

print("listado de numeros primer dígito:",total1D0)
print()
print("listado de numeros segundo dígito:",total1D1)
print()
print("listado de numeros tercer dígito:",total1D2)

#para el primer digito: obtener listado de numeros sin repetir y verificar cuantas veces se repite

listaSinRepetidos1D0 = list(set(total1D0))

#listaSinRepetidos1D = list(listaSinRepetidos1D)
print("Los números caídos en lista son:",listaSinRepetidos1D0)

i = 0
k = 0
num = []
rep = []
numRep1D0 = [num, rep]

for l in range (len(listaSinRepetidos1D0)):
    num.append(listaSinRepetidos1D0[i])
    cant = 0
    j = 0
    for k in range (len(total1D0)):
        if int(listaSinRepetidos1D0[i]) == int(total1D0[j]):
            cant = cant + 1
        j = j + 1
        
    rep.append(cant)
    i = i + 1 

print(numRep1D0)

#Imprimir la cantidad de veces que un numero se repite 
i = 0
j = 0
print("listado de numeros del primer digito")
for numero in num:
    print("el numero",num[i],"se repite",rep[j],"veces")
    i = i + 1
    j = j + 1

#para el segundo digito: obtener listado de numeros sin repetir y verificar cuantas veces se repi

listaSinRepetidos1D1 = list(set(total1D1))

#listaSinRepetidos1D = list(listaSinRepetidos1D)
print("Los números caídos en lista son:",listaSinRepetidos1D1)

i = 0
k = 0
num = []
rep = []
numRep1D1 = [num, rep]

for l in range (len(listaSinRepetidos1D1)):
    num.append(listaSinRepetidos1D1[i])
    cant = 0
    j = 0
    for k in range (len(total1D1)):
        if int(listaSinRepetidos1D1[i]) == int(total1D1[j]):
            cant = cant + 1
        j = j + 1
        
    rep.append(cant)
    i = i + 1 

print(numRep1D1)

#Imprimir la cantidad de veces que un numero se repite 
i = 0
j = 0
print("listado de numeros del primer digito")
for numero in num:
    print("el numero",num[i],"se repite",rep[j],"veces")
    i = i + 1
    j = j + 1

#para el tercer digito: obtener listado de numeros sin repetir y verificar cuantas veces se repi

listaSinRepetidos1D2 = list(set(total1D2))

#listaSinRepetidos1D = list(listaSinRepetidos1D)
print("Los números caídos en lista son:",listaSinRepetidos1D2)

i = 0
k = 0
num = []
rep = []
numRep1D2 = [num, rep]

for l in range (len(listaSinRepetidos1D2)):
    num.append(listaSinRepetidos1D2[i])
    cant = 0
    j = 0
    for k in range (len(total1D2)):
        if int(listaSinRepetidos1D2[i]) == int(total1D2[j]):
            cant = cant + 1
        j = j + 1
        
    rep.append(cant)
    i = i + 1 

print(numRep1D2)

#Imprimir la cantidad de veces que un numero se repite 
i = 0
j = 0
print("listado de numeros del primer digito")
for numero in num:
    print("el numero",num[i],"se repite",rep[j],"veces")
    i = i + 1
    j = j + 1