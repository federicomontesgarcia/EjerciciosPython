import pandas as pd

datos = { 'manzanas' : [ 3 , 2 , 0 , 1 ], 'naranjas' : [ 0 , 3 , 7 , 2 ] }
compras = pd.DataFrame( datos , index = [ 'Juno' , 'Robert' , 'Lily' , 'David' ])   
print(compras)
#Las etiquetas de filas y de columnas -los índices- son accesibles a través de los atributos index y columns, respectivamente:
print()
print(compras)

print()
print(compras.index)
print(compras.columns)

compras.index.name = "Clientes"
compras.columns.name = "Frutas"
print()
print(compras)
