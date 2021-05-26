cafeterito = {
    'marzo' : {
        'tarde' : { 'marzo1t':'4764', 'marzo2t':'9685', 'marzo3t':'5971', 'marzo4t':'6995', 'marzo5t':'9619', 'marzo6t':'6786', 'marzo8t':'3120', 'marzo9t':'4485',
        'marzo10t':'9467', 'marzo11t':'1356','marzo12t':'2825', 'marzo13t':'0302', 'marzo15t':'8414', 'marzo16t':'3562', 'marzo17t':'5285', 'marzo18t':'8009',
        'marzo19t':'5746', 'marzo20t':'8588', 'marzo23t':'6006', 'marzo24t':'5157', 'marzo25t':'6365', 'marzo26t':'4590', 'marzo27t':'3082', 'marzo29t':'0361',
        'marzo30t':'4303', 'marzo31t':'9824' }, 

        'noche' : { 'marzo1n':'4106', 'marzo2n':'7793', 'marzo3n':'9201', 'marzo4n':'0601', 'marzo5n':'2753', 'marzo6n':'4817','marzo7n':'1721', 'marzo8n':'8018',
        'marzo9n':'9862', 'marzo10n':'6939', 'marzo11n':'1373', 'marzo12n':'8486', 'marzo13n':'0054', 'marzo14n':'5595', 'marzo15n':'1741', 'marzo16n':'3530', 
        'marzo17n':'6376', 'marzo18n':'7424', 'marzo19n':'3859', 'marzo21n':'0735', 'marzo22n':'5750', 'marzo23n':'5150', 'marzo25n':'5665', 'marzo26n':'1822',
        'marzo27n':'5247', 'marzo28n':'9344',  'marzo29n':'9242',  'marzo30n':'1516',  'marzo31n':'3491'}
    }
}

marzo = []
marzoTarde = []
marzoNoche = []

#retorna una lista solo con los valores del diccionario
marzoTarde = cafeterito['marzo']['tarde'].values()
marzoNoche = cafeterito['marzo']['noche'].values()

print("lista cadenas marzo tarde:",marzoTarde)
print("")
print("lista cadenas marzo noche:",marzoNoche)

print("cantidad de sorteos realizados cafetrito tarde en marzo:",len(marzoTarde))
print("cantidad de sorteos realizados cafetrito tarde en marzo:",len(marzoNoche))

#convierte la lista que tiene elementos cadena en elementos enteros
#marzoInt = list(map(int, marzo))

#ordena los elementos enteros de menor a mayor
#marzoInt.sort()
#print("lista enteros ordenada:",marzoInt)

#devuelve un valor del diccionario
#print(cafeterito['marzo'].get('marzo5t'))

