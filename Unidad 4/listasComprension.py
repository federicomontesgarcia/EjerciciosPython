mi_lista = []
for x in range(4, 31, 2):
    if x%3 == 0:
        mi_lista.append(x**2)

print(mi_lista)

print()
#---------------------------
mi_lista = [x**2 for x in range(4, 31, 2) if x%3 == 0]
print(mi_lista)

#---------------------------
print()

mi_diccionario = dict()
for y in range(3, 11):
    mi_diccionario[(y, y**3)] = []
    for x in range(4, 31, 2):
        if x%y == 0:
            mi_diccionario[(y, y**3)].append(x**2)

print(mi_diccionario)

print()

#---------------------------

mi_diccionario = { (x, x**3) : [ y**2 for y in range(4,31,2) if y%x == 0 ] for x in range(3, 11) }
print(mi_diccionario)

print()

#--------------------------

print( [x for x in range(4, 31, 2)] )

#--------------------------
print()

print( [x**2 for x in range(4, 31, 2) if x%3 == 0] )

