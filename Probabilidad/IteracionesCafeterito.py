cafeterito = {
    'marzo' : {
        'tarde' : {'marzo1t':'4764', 'marzo2t':'9685', 'marzo3t':'5971', 'marzo4t':'6995', 'marzo5t':'9619', 'marzo6t':'6786', 'marzo8t':'3120', 'marzo9t':'4485',
        'marzo10t':'9467', 'marzo11t':'1356','marzo12t':'2825', 'marzo13t':'0302', 'marzo15t':'8414', 'marzo16t':'3562', 'marzo17t':'5285', 'marzo18t':'8009',
        'marzo19t':'5746', 'marzo20t':'8588', 'marzo23t':'6006', 'marzo24t':'5157', 'marzo25t':'6365', 'marzo26t':'4590', 'marzo27t':'3082', 'marzo29t':'0361',
        'marzo30t':'4303', 'marzo31t':'9824'}, 

        'noche' : { 'marzo1n':'4106', 'marzo2n':'7793', 'marzo3n':'9201', 'marzo4n':'0601', 'marzo5n':'2753', 'marzo6n':'4817','marzo7n':'1721', 'marzo8n':'8018',
        'marzo9n':'9862', 'marzo10n':'6939', 'marzo11n':'1373', 'marzo12n':'8486', 'marzo13n':'0054', 'marzo14n':'5595', 'marzo15n':'1741', 'marzo16n':'3530', 
        'marzo17n':'6376', 'marzo18n':'7424', 'marzo19n':'3859','marzo20n':'1744','marzo21n':'0735', 'marzo22n':'5750', 'marzo23n':'5150', 'marzo25n':'5665', 
        'marzo26n':'1822', 'marzo27n':'5247', 'marzo28n':'9344',  'marzo29n':'9242',  'marzo30n':'1516',  'marzo31n':'3491'}
    },
    'abril' : {
        'tarde' : { 'abril3t':'0222', 'abril5t':'3207', 'abril6t':'6109', 'abril7t':'1026', 'abril8t':'9658', 'abril9t':'5803','abril10t':'2219', 'abril12t':'7615',
        'abril13t':'3058', 'abril14t':'3934', 'abril15t':'5662', 'abril16t':'1683', 'abril17t':'6781', 'abril19t':'7504', 'abril20t':'6241', 'abril21t':'2663', 
        'abril22t':'6089', 'abril23t':'9352', 'abril24t':'9836', 'abril26t':'7898', 'abril27t':'4487', 'abril28t':'9145', 'abril29t':'9771', 'abril30t':'7038'},

        'noche' : { 'aabril1n':'7359', 'abril2n':'7410', 'abril3n':'4289', 'abril4n':'2925', 'abril5n':'4481', 'abril6n':'3279','abril7n':'4164', 'abril8n':'8643',
        'abril9n':'4177', 'abril10n':'6354', 'abril11n':'4631', 'abril12n':'1669', 'abril13n':'9724', 'abril14n':'1291', 'abril15n':'4443', 'abril16n':'2746', 
        'abril17n':'9932', 'abril18n':'8634', 'abril19n':'1639','abril20n':'0164','abril21n':'0936', 'abril22n':'8869', 'abril23n':'1294', 'abril24n':'7020', 
        'abril25n':'3266', 'abril26n':'4221', 'abril27n':'4578',  'abril28n':'4452',  'abril29n':'1763',  'abril30n':'1934'}
    },
    'mayo' : {
        'tarde' : { 'mayo3t':'7827', 'mayo4t':'8849', 'mayo5t':'2082', 'mayo6t':'1895', 'mayo7t':'0011', 'mayo8t':'5267','mayo10t':'6272', 'mayo11t':'9684', 
        'mayo12t':'6140', 'mayo13t':'3940', 'mayo14t':'8313', 'mayo15t':'9433', 'mayo18t':'0159', 'mayo19t':'8275', 'mayo20t':'4741', 'mayo21t':'9056', 
        'mayo22t':'0539', 'mayo24t':'1113', 'mayo25t':'6132', 'mayo26t':'8872', 'mayo27t':'1244', 'mayo28t':'8199', 'mayo29t':'9972', 'mayo31':'3296'}, 
        
        'noche' : { 'mayo1n':'1203', 'mayo2n':'9302', 'mayo3n':'2324', 'mayo4n':'6248', 'mayo5n':'3938', 'mayo6n':'8643','mayo7n':'5978', 'mayo8n':'6843', 
        'mayo9n':'3452', 'mayo10n':'8516', 'mayo11n':'3788', 'mayo12n':'1098', 'mayo13n':'1005', 'mayo14n':'6390', 'mayo15n':'5627', 'mayo16n':'9801',
        'mayo17n':'2100','mayo18n':'8951', 'mayo19n':'1028', 'mayo20n':'2896', 'mayo21n':'1296', 'mayo22n':'0783', 'mayo23n':'3961', 'mayo24n':'9509',  
        'mayo25n':'0749',  'mayo26n':'1523', 'mayo27n':'9430', 'mayo28n':'5621', 'mayo29n':'5051', 'mayo30n':'5189', 'mayo31':'9044'}
    }
}

marzo3D = []
abril3D = []
mayo3D = []
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
    global mayo3D
    mayo3D = num3C
#---------------------------------------------------------------------------------------------------------------    
mesProbabilidad = (probabilidades( elmes = 'marzo', mesT = cafeterito['marzo']['tarde'], mesN = cafeterito['marzo']['noche'], num3C = 'marzo3D'))

listaTotal = []
listaTotal = marzo3D

print("-------------------------------------------------------------------------------------------------------")
mesProbabilidad = (probabilidades( elmes = 'abril', mesT = cafeterito['abril']['tarde'], mesN = cafeterito['abril']['noche'], num3C = 'abril3D'))

listaTotal = listaTotal + abril3D

print("-------------------------------------------------------------------------------------------------------")
mesProbabilidad = (probabilidades( elmes = 'mayo', mesT = cafeterito['mayo']['tarde'], mesN = cafeterito['mayo']['noche'], num3C = 'mayo3D'))

listaTotal = listaTotal + mayo3D


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