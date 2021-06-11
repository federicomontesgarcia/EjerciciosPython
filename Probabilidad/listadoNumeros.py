import pandas as pd
import numpy as np

cafeterito = {
    'enero' : {
        'tarde' : { 'enero2t':'2905', 'enero4t':'6428', 'enero5t':'8006', 'enero6t':'1374', 'enero7t':'1921', 'enero8t':'4051', 'enero9t':'0568', 'enero12t':'9529',
        'enero13t':'3604', 'enero14t':'9793', 'enero15t':'0489', 'enero16t':'4620', 'enero18t':'4686', 'enero19t':'3712', 'enero20t':'4310', 'enero21t':'0178', 
        'enero22t':'2883', 'enero23t':'6058', 'enero25t':'1631', 'enero26t':'6925', 'enero27t':'9397', 'enero28t':'1279', 'enero29t':'2436', 'enero30t':'4744'}, 

        'noche' : { 'enero1n':'7940', 'enero2n':'6568', 'enero3n':'1996', 'enero4n':'1168', 'enero5n':'7891', 'enero6n':'5683','enero7n':'4913', 'enero8n':'5251', 
        'enero9n':'5766', 'enero10n':'5559', 'enero11n':'7682', 'enero12n':'2535', 'enero13n':'9619', 'enero14n':'9555', 'enero15n':'8116', 'enero16n':'6569',
        'enero17n':'6037','enero18n':'7232', 'enero19':'5529', 'enero20n':'3268', 'enero21n':'2444', 'enero22n':'7073', 'enero23n':'7907', 'enero24n':'1122',  
        'enero25n':'2556',  'enero26n':'6849', 'enero27n':'0448', 'enero28n':'1608', 'enero29n':'7504', 'enero30n':'9012', 'mayo31n':'4992'}
    },
    'febrero' : {
        'tarde' : { 'febrero1t':'3117','febrero2t':'7576','febrero3t':'3306', 'febrero4t':'5567', 'febrero5t':'1625', 'febrero6t':'2743', 'febrero8t':'6795', 'febrero9t':'8752', 'febrero10t':'1219', 'febrero11t':'3781',
        'febrero12t':'9054', 'febrero13t':'6174', 'febrero15t':'5255', 'febrero16t':'0302', 'febrero17t':'2802', 'febrero18t':'1741', 'febrero19t':'0776', 
        'febrero20t':'5395', 'febrero22t':'6351', 'febrero23t':'6863', 'febrero24t':'3930', 'febrero25t':'5758', 'febrero26t':'4361', 'febrero27t':'6628'}, 

        'noche' : { 'febrero1n':'6406', 'febrero2n':'4675', 'febrero3n':'1646', 'febrero4n':'8162', 'febrero5n':'1047', 'febrero6n':'6198','febrero7n':'3318', 
        'febrero8n':'4325', 'febrero9n':'1179', 'febrero10n':'8233', 'febrero11n':'7242', 'febrero12n':'2181', 'febrero13n':'8266', 'febrero14n':'3800', 
        'febrero15n':'6041', 'febrero16n':'1824','febrero17n':'6769','febrero18n':'2775', 'febrero19n':'8618', 'febrero20n':'3744', 'febrero21n':'8979', 
        'febrero22n':'6045', 'febrero23n':'7620', 'febrero24n':'7426', 'febrero25n':'8003',  'febrero26n':'8709', 'febrero27n':'8404', 'febrero28n':'3205'}
    },
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
    },
    'junio' : {
        'tarde' : { 'junio1t':'2074', 'junio2t':'2980', 'junio3t':'0496', 'junio4t':'6017', 'junio5t':'9297', 'junio8t':'5238'}, 

        'noche' : { 'junio1n':'8164', 'junio2n':'6692', 'junio3n':'6754', 'junio4n':'2239', 'junio5n':'3871', 'junio6n':'3657','junio7n':'7694'}
    },
}

sorteoEneroTarde = pd.DataFrame([cafeterito ['enero']['tarde']])
sorteoEneroNoche = pd.DataFrame([cafeterito ['enero']['noche']])
sorteoEneroTarde.to_csv('archivosCSV\sorteoEneroTarde.csv')
sorteoEneroNoche.to_csv('archivosCSV\sorteoEneroNoche.csv')

sorteo = pd.read_csv('archivosCSV\sorteoEneroTarde.csv')
print(sorteo)

