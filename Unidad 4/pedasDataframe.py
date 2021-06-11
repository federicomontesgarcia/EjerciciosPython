import pandas as pd

datos = { 'manzanas' : [ 3 , 2 , 0 , 1 ], 'naranjas' : [ 0 , 3 , 7 , 2 ] }
print(datos)
print()

compras = pd.DataFrame( datos )
print(compras)