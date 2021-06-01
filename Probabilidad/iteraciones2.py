<<<<<<< HEAD
cafeterito = {
    'marzo' : {
        'tarde' : {'marzo1t':'4764', 'marzo2t':'9685', 'marzo3t':'5971', 'marzo4t':'6995', 'marzo5t':'9619', 'marzo6t':'6786', 'marzo8t':'3120', 'marzo9t':'4485'}, 

        'noche' : { 'marzo1n':'4106', 'marzo2n':'7793', 'marzo3n':'9201', 'marzo4n':'0601', 'marzo5n':'2753', 'marzo6n':'4817','marzo7n':'1721', 'marzo8n':'8018',}
    },
    'abril' : {
        'tarde' : { 'abril3t':'0222', 'abril5t':'3207', 'abril6t':'6109', 'abril7t':'1026', 'abril8t':'9658', 'abril9t':'5803','abril10t':'2219', 'abril12t':'7615'},

        'noche' : { 'aabril1n':'7359', 'abril2n':'7410', 'abril3n':'4289', 'abril4n':'2925', 'abril5n':'4481', 'abril6n':'3279','abril7n':'4164', 'abril8n':'8643'}
    },
    'mayo' : {
        'tarde' : { 'mayo3t':'7827', 'mayo4t':'8849', 'mayo5t':'2082', 'mayo6t':'1895', 'mayo7t':'0011', 'mayo8t':'5267','mayo10t':'6272', 'mayo11t':'9684'}, 
        
        'noche' : { 'mayo1n':'1203', 'mayo2n':'9302', 'mayo3n':'2324', 'mayo4n':'6248', 'mayo5n':'3938', 'mayo6n':'8643','mayo7n':'5978', 'mayo8n':'6843'}
    }
}

marzo3D = []
abril3D = []
dig0 = 0
dig1 = 0
dig2 = 0
D = 0
#------------------------------------------------------------
#funcion convertir diccionarios en listas 
def probabilidades(elmes, mesT, mesN, num3C):
    print("Datos mes de",elmes)

    mesTarde = []
    mesNoche = []
    mes = []

    #retorna una lista solo con los valores del diccionario
    mesTarde = mesT.values()
    mesNoche = mesN.values()

    print("lista cadenas",elmes,"tarde:",mesTarde)
    print("")
    print("lista cadenas",elmes,"noche:",mesNoche)

    print("")
    #cuenta la cantidad de elementos dentro de la lista
    print("cantidad de sorteos realizados cafetrito tarde en",elmes,":",len(mesTarde))
    print("cantidad de sorteos realizados cafetrito noche en", elmes,":",len(mesNoche))

    print()
    for numero in mesNoche:
        mes.append(numero)

    for numero in mesTarde:
        mes.append(numero)

    #"numeros guardados en lista"
    print("cantidad de sorteos realizados en",elmes,":",len(mes))
    print()
    #obteniendo numeros sin repetir
    numUnicos = set(mes)
    numUnicos = list(numUnicos)
    print("Los números de",elmes,"sin repetir caídos son:",numUnicos)
    print()
    print("cantidad de numeros sin repetir caidos en",elmes,":",len(numUnicos))
    print()

    #numeros de 3 cifras
    num3C = []
    i = 0
    n = 0
    for num in mes:
        j = 1
        num3 = ""
        nuevo = mes[i]
        for n in nuevo:
            if j < 4:
                num3 = num3 + nuevo[j]  
            j = j + 1
        num3C.append(num3) 
        i = i + 1
    print("Listado de los numeros de 3 cifras de",elmes,num3C)

#declaracion de variables globales
    global marzo3D
    marzo3D = num3C
    global abril3D
    abril3D = num3C
mesProbabilidad = (probabilidades( elmes = 'marzo', mesT = cafeterito['marzo']['tarde'], mesN = cafeterito['marzo']['noche'], num3C = 'marzo3D'))

listaTotal = []
listaTotal = marzo3D

print("-------------------------------------------------------------------------------------------------------")
mesProbabilidad = (probabilidades( elmes = 'abril', mesT = cafeterito['abril']['tarde'], mesN = cafeterito['abril']['noche'], num3C = 'abril3D'))

listaTotal = listaTotal + abril3D

#--------------------------------------------------------------------------------------------------------------------------
print("------------------------------------------------------operaciones totales-------------------------------------------------------")
print("Lista total de numeros:",listaTotal)

#ordenar la lista
swapped = True
while swapped:
    swapped = False
    for i in range(len(listaTotal) - 1):
        if listaTotal[i] > listaTotal[i + 1]:
            swapped = True
            listaTotal[i], listaTotal[i + 1] = listaTotal[i + 1], listaTotal[i]

#print("lista de numeros totales ordenada",listaTotal)
#-----------------------
listaSinRepetidos = set(listaTotal)
listaSinRepetidos = list(listaSinRepetidos)
print()
#ordenar la lista
swapped = True
while swapped:
    swapped = False
    for i in range(len(listaSinRepetidos) - 1):
        if listaSinRepetidos[i] > listaSinRepetidos[i + 1]:
            swapped = True
            listaSinRepetidos[i], listaSinRepetidos[i + 1] = listaSinRepetidos[i + 1], listaSinRepetidos[i]
print()
print("lista de numeroso ordenada",listaSinRepetidos)
#print("Los números sin repetir en lista son:",listaSinRepetidos)


print()
#----------------------------
i = 0
k = 0
num = []
rep = []
numRep = [num, rep]
for l in range (len(listaSinRepetidos)):
    num.append(listaSinRepetidos[i])
    cant = 0
    j = 0
    for k in range (len(listaTotal)):
        if int(listaSinRepetidos[i]) == int(listaTotal[j]):
            cant = cant + 1
        j = j + 1
    rep.append(cant)
    i = i + 1 
print()
print("listado de numeros sin repetir y veces que se repiten",numRep)
#Imprimir la cantidad de veces que un numero se repite 
i = 0
j = 0
for numero in num:
    print("el numero",num[i],"se repite",rep[j],"veces")
    i = i + 1
    j = j + 1

#----------------------------------------------------------------
#convertir la lista con numeros de 3 cifras a 3 listas con numeros de 1 cifra
print()
total1D0 = []
total1D1 = []
total1D2 = []
i = 0
n = 0
for num in listaTotal:
    j = 0
    num1 = ""
    nuevo = listaTotal[i]
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

#--------------------------------------------------------------------
#numeros que mas se repiten de 1 cifra

def calcularNumUnicos(digito, num1Digito, dig):
    global total1D0 
    global total1D1 
    global total1D2 
    
    
    listaSinRepetidos = set(num1Digito)
    listaSinRepetidos = list(listaSinRepetidos)
    print()
    print("Los números del",digito,"dígito sin repetir son:",listaSinRepetidos)

    #ordenar la lista
    swapped = True
    while swapped:
        swapped = False
        for i in range(len(listaSinRepetidos) - 1):
            if listaSinRepetidos[i] > listaSinRepetidos[i + 1]:
                swapped = True
                listaSinRepetidos[i], listaSinRepetidos[i + 1] = listaSinRepetidos[i + 1], listaSinRepetidos[i]
    print()
    #print("lista de numeroso ordenada",listaSinRepetidos)
        

    #----------------------------
    i = 0
    k = 0
    num = []
    rep = []
    numRep = [num, rep]
    for l in range (len(listaSinRepetidos)):
        num.append(listaSinRepetidos[i])
        cant = 0
        j = 0
        for k in range (len(num1Digito)):
            if int(listaSinRepetidos[i]) == int(num1Digito[j]):
                cant = cant + 1
            j = j + 1
        rep.append(cant)
        i = i + 1 
    print()
    print("listado de numeros sin repetir del",digito,"dígito y las veces que se repiten",numRep)
    #Imprimir la cantidad de veces que un numero se repite 
    i = 0
    j = 0
    for numero in num:
        print("el numero",num[i],"se repite",rep[j],"veces")
        i = i + 1
        j = j + 1
    
    #buscar el numero que se repite mas veces
    global dig0
    dig = 0
    global dig1
    dig = 0
    global dig2
    dig = 0

    mayor = rep[0]

    for i in range(1, len(rep)):
       if rep [i]> mayor:
            mayor = rep[i]
            dig = num[i]
    
    dig0 = dig
    dig1 = dig
    dig2 = dig
    print()
    print("el número",dig,"es el que mas veces se repite:",mayor,"veces")

    
numerosUnDigito = (calcularNumUnicos( digito = 'primer', num1Digito = total1D0, dig = dig0 ))
primo = dig0
print()
numerosUnDigito = (calcularNumUnicos( digito = 'segundo', num1Digito = total1D1, dig = dig1 ))
secondo = dig1
print()
numerosUnDigito = (calcularNumUnicos( digito = 'tercero', num1Digito = total1D2, dig = dig2 ))
terzo = dig2
print()
print()
print("El numero recomendado para jugar es el:",primo,secondo,terzo)
=======
cafeterito = {
    'marzo' : {
        'tarde' : {'marzo1t':'4764', 'marzo2t':'9685', 'marzo3t':'5971', 'marzo4t':'6995', 'marzo5t':'9619', 'marzo6t':'6786', 'marzo8t':'3120', 'marzo9t':'4485'}, 

        'noche' : { 'marzo1n':'4106', 'marzo2n':'7793', 'marzo3n':'9201', 'marzo4n':'0601', 'marzo5n':'2753', 'marzo6n':'4817','marzo7n':'1721', 'marzo8n':'8018',}
    },
    'abril' : {
        'tarde' : { 'abril3t':'0222', 'abril5t':'3207', 'abril6t':'6109', 'abril7t':'1026', 'abril8t':'9658', 'abril9t':'5803','abril10t':'2219', 'abril12t':'7615'},

        'noche' : { 'aabril1n':'7359', 'abril2n':'7410', 'abril3n':'4289', 'abril4n':'2925', 'abril5n':'4481', 'abril6n':'3279','abril7n':'4164', 'abril8n':'8643'}
    },
    'mayo' : {
        'tarde' : { 'mayo3t':'7827', 'mayo4t':'8849', 'mayo5t':'2082', 'mayo6t':'1895', 'mayo7t':'0011', 'mayo8t':'5267','mayo10t':'6272', 'mayo11t':'9684'}, 
        
        'noche' : { 'mayo1n':'1203', 'mayo2n':'9302', 'mayo3n':'2324', 'mayo4n':'6248', 'mayo5n':'3938', 'mayo6n':'8643','mayo7n':'5978', 'mayo8n':'6843'}
    }
}

marzo3D = []
abril3D = []
dig0 = 0
dig1 = 0
dig2 = 0
D = 0
#------------------------------------------------------------
#funcion convertir diccionarios en listas 
def probabilidades(elmes, mesT, mesN, num3C):
    print("Datos mes de",elmes)

    mesTarde = []
    mesNoche = []
    mes = []

    #retorna una lista solo con los valores del diccionario
    mesTarde = mesT.values()
    mesNoche = mesN.values()

    print("lista cadenas",elmes,"tarde:",mesTarde)
    print("")
    print("lista cadenas",elmes,"noche:",mesNoche)

    print("")
    #cuenta la cantidad de elementos dentro de la lista
    print("cantidad de sorteos realizados cafetrito tarde en",elmes,":",len(mesTarde))
    print("cantidad de sorteos realizados cafetrito noche en", elmes,":",len(mesNoche))

    print()
    for numero in mesNoche:
        mes.append(numero)

    for numero in mesTarde:
        mes.append(numero)

    #"numeros guardados en lista"
    print("cantidad de sorteos realizados en",elmes,":",len(mes))
    print()
    #obteniendo numeros sin repetir
    numUnicos = set(mes)
    numUnicos = list(numUnicos)
    print("Los números de",elmes,"sin repetir caídos son:",numUnicos)
    print()
    print("cantidad de numeros sin repetir caidos en",elmes,":",len(numUnicos))
    print()

    #numeros de 3 cifras
    num3C = []
    i = 0
    n = 0
    for num in mes:
        j = 1
        num3 = ""
        nuevo = mes[i]
        for n in nuevo:
            if j < 4:
                num3 = num3 + nuevo[j]  
            j = j + 1
        num3C.append(num3) 
        i = i + 1
    print("Listado de los numeros de 3 cifras de",elmes,num3C)

#declaracion de variables globales
    global marzo3D
    marzo3D = num3C
    global abril3D
    abril3D = num3C
mesProbabilidad = (probabilidades( elmes = 'marzo', mesT = cafeterito['marzo']['tarde'], mesN = cafeterito['marzo']['noche'], num3C = 'marzo3D'))

listaTotal = []
listaTotal = marzo3D

print("-------------------------------------------------------------------------------------------------------")
mesProbabilidad = (probabilidades( elmes = 'abril', mesT = cafeterito['abril']['tarde'], mesN = cafeterito['abril']['noche'], num3C = 'abril3D'))

listaTotal = listaTotal + abril3D

#--------------------------------------------------------------------------------------------------------------------------
print("------------------------------------------------------operaciones totales-------------------------------------------------------")
print("Lista total de numeros:",listaTotal)

#ordenar la lista
swapped = True
while swapped:
    swapped = False
    for i in range(len(listaTotal) - 1):
        if listaTotal[i] > listaTotal[i + 1]:
            swapped = True
            listaTotal[i], listaTotal[i + 1] = listaTotal[i + 1], listaTotal[i]

#print("lista de numeros totales ordenada",listaTotal)
#-----------------------
listaSinRepetidos = set(listaTotal)
listaSinRepetidos = list(listaSinRepetidos)
print()
#ordenar la lista
swapped = True
while swapped:
    swapped = False
    for i in range(len(listaSinRepetidos) - 1):
        if listaSinRepetidos[i] > listaSinRepetidos[i + 1]:
            swapped = True
            listaSinRepetidos[i], listaSinRepetidos[i + 1] = listaSinRepetidos[i + 1], listaSinRepetidos[i]
print()
print("lista de numeroso ordenada",listaSinRepetidos)
#print("Los números sin repetir en lista son:",listaSinRepetidos)


print()
#----------------------------
i = 0
k = 0
num = []
rep = []
numRep = [num, rep]
for l in range (len(listaSinRepetidos)):
    num.append(listaSinRepetidos[i])
    cant = 0
    j = 0
    for k in range (len(listaTotal)):
        if int(listaSinRepetidos[i]) == int(listaTotal[j]):
            cant = cant + 1
        j = j + 1
    rep.append(cant)
    i = i + 1 
print()
print("listado de numeros sin repetir y veces que se repiten",numRep)
#Imprimir la cantidad de veces que un numero se repite 
i = 0
j = 0
for numero in num:
    print("el numero",num[i],"se repite",rep[j],"veces")
    i = i + 1
    j = j + 1

#----------------------------------------------------------------
#convertir la lista con numeros de 3 cifras a 3 listas con numeros de 1 cifra
print()
total1D0 = []
total1D1 = []
total1D2 = []
i = 0
n = 0
for num in listaTotal:
    j = 0
    num1 = ""
    nuevo = listaTotal[i]
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

#--------------------------------------------------------------------
#numeros que mas se repiten de 1 cifra

def calcularNumUnicos(digito, num1Digito, dig):
    global total1D0 
    global total1D1 
    global total1D2 
    
    
    listaSinRepetidos = set(num1Digito)
    listaSinRepetidos = list(listaSinRepetidos)
    print()
    print("Los números del",digito,"dígito sin repetir son:",listaSinRepetidos)

    #ordenar la lista
    swapped = True
    while swapped:
        swapped = False
        for i in range(len(listaSinRepetidos) - 1):
            if listaSinRepetidos[i] > listaSinRepetidos[i + 1]:
                swapped = True
                listaSinRepetidos[i], listaSinRepetidos[i + 1] = listaSinRepetidos[i + 1], listaSinRepetidos[i]
    print()
    #print("lista de numeroso ordenada",listaSinRepetidos)
        

    #----------------------------
    i = 0
    k = 0
    num = []
    rep = []
    numRep = [num, rep]
    for l in range (len(listaSinRepetidos)):
        num.append(listaSinRepetidos[i])
        cant = 0
        j = 0
        for k in range (len(num1Digito)):
            if int(listaSinRepetidos[i]) == int(num1Digito[j]):
                cant = cant + 1
            j = j + 1
        rep.append(cant)
        i = i + 1 
    print()
    print("listado de numeros sin repetir del",digito,"dígito y las veces que se repiten",numRep)
    #Imprimir la cantidad de veces que un numero se repite 
    i = 0
    j = 0
    for numero in num:
        print("el numero",num[i],"se repite",rep[j],"veces")
        i = i + 1
        j = j + 1
    
    #buscar el numero que se repite mas veces
    global dig0
    dig = 0
    global dig1
    dig = 0
    global dig2
    dig = 0

    mayor = rep[0]

    for i in range(1, len(rep)):
       if rep [i]> mayor:
            mayor = rep[i]
            dig = num[i]
    
    dig0 = dig
    dig1 = dig
    dig2 = dig
    print()
    print("el número",dig,"es el que mas veces se repite:",mayor,"veces")

    
numerosUnDigito = (calcularNumUnicos( digito = 'primer', num1Digito = total1D0, dig = dig0 ))
primo = dig0
print()
numerosUnDigito = (calcularNumUnicos( digito = 'segundo', num1Digito = total1D1, dig = dig1 ))
secondo = dig1
print()
numerosUnDigito = (calcularNumUnicos( digito = 'tercero', num1Digito = total1D2, dig = dig2 ))
terzo = dig2
print()
print()
print("El numero recomendado para jugar es el:",primo,secondo,terzo)
>>>>>>> 1264039b393ab93d7c86e6a7c7edadcd298c8fed
