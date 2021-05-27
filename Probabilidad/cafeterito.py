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
    }
}

#marzo
marzo = []
marzoTarde = []
marzoNoche = []

#retorna una lista solo con los valores del diccionario
marzoTarde = cafeterito['marzo']['tarde'].values()
marzoNoche = cafeterito['marzo']['noche'].values()

print("lista cadenas marzo tarde:",marzoTarde)
print("")
print("lista cadenas marzo noche:",marzoNoche)
print("")
print("lista cadenas marzo:",marzo)
print("")
#cuenta la cantidad de elementos dentro de la lista
print("cantidad de sorteos realizados cafetrito tarde en marzo:",len(marzoTarde))
print("cantidad de sorteos realizados cafetrito noche en marzo:",len(marzoNoche))

for numero in marzoNoche:
    marzo.append(numero)

for numero in marzoTarde:
    marzo.append(numero)

print("numeros guardados en lista:",marzo)
print("cantidad de sorteos realizados en marzo:",len(marzo))

print(marzo[0])

#-------------------------------------------------------------------------------------
#abril

abril = []
abrilTarde = []
abrilNoche = []

#retorna una lista solo con los valores del diccionario
abrilTarde = cafeterito['abril']['tarde'].values()
abrilNoche = cafeterito['abril']['noche'].values()

print("lista cadenas abril tarde:",abrilTarde)
print("")
print("lista cadenas abril noche:",abrilNoche)
print("")
print("lista cadenas abril:",abril)
print("")
#cuenta la cantidad de elementos dentro de la lista
print("cantidad de sorteos realizados cafetrito tarde en abril:",len(abrilTarde))
print("cantidad de sorteos realizados cafetrito noche en abril:",len(abrilNoche))

for numero in abrilNoche:
    abril.append(numero)

for numero in abrilTarde:
    abril.append(numero)

print("numeros guardados en lista:",abril)
print("cantidad de sorteos realizados en abril:",len(abril))

print(abril[0])

#----------------------------------------------------------------------------------------------------------



#------------------------------------------------------------------------------------
#ejemplo de como hallar la cantidad de veces que un numero se repite

original = [2,3,3,8,4,7,2,9,9,2,3,4,7,7,2,4,8,9,9]
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
         
#------------------------------------------------------------------------------------------