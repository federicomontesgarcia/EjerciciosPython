set_mutable1 = set([4, 3, 11, 7, 5, 2, 1, 4])
print(set_mutable1)
#agregar elemento
set_mutable1.add(22.000001)
print(set_mutable1)

set_mutable1 = set([4, 3, 11, 7, 5, 2, 1, 4])
print(set_mutable1)
#borrar los elementos
set_mutable1.clear()
print(set_mutable1)

set_mutable = set([4.0, 'Carro', True])
#copia los elementos
otro_set_mutable = set_mutable.copy()
set_mutable == otro_set_mutable

#verifica la diferencia entre 2 conjuntos
set_mutable1 = set([4, 3, 11, 7, 5, 2, 1, 4])
set_mutable2 = set([11, 5, 9, 2, 4, 8])
print(set_mutable1)
print(set_mutable2)
print(set_mutable1.difference(set_mutable2))
print(set_mutable2.difference(set_mutable1))

a = {1, 2, 3, 4}
b = {2, 3}
c = a - b
print(c)

#completa la diferencia
proyecto1 = {'python', 'Zope2', 'ZODB3', 'pytz'}
print(proyecto1)
proyecto2 = {'python', 'Plone', 'diazo'}
print(proyecto2)
proyecto1.difference_update(proyecto2)
print(proyecto1)

#elimina elementos
paquetes = {'python', 'zope', 'plone', 'django'}
print(paquetes)
paquetes.discard('django')
print(paquetes)
paquetes = {'python', 'zope', 'plone', 'django'}
paquetes.discard('php')

#interseccion de conjuntos
set_mutable1 = set([4, 3, 11, 7, 5, 2, 1, 4])
set_mutable2 = set([11, 5, 9, 2, 4, 8])
print(set_mutable1)
print(set_mutable2)
print(set_mutable1.intersection(set_mutable2))
print(set_mutable2.intersection(set_mutable1))

set_intersection = set_mutable1 & set_mutable2
print(set_intersection)

#elemento comun entre los 3 proyectos y actualiza
proyecto1 = {'python', 'Zope2', 'pytz'}
print(proyecto1)
proyecto2 = {'python', 'Plone', 'diazo', 'z3c.form'}
print(proyecto2)
proyecto3 = {'python', 'django', 'django-filter'}
print(proyecto3)
proyecto3.intersection_update(proyecto1, proyecto2)
print(proyecto3)

#devuelve true or false, verifica si hay elemetos comunes
set_mutable1 = set([4, 3, 11, 7, 5, 2, 1, 4])
set_mutable2 = set([11, 5, 9, 2, 4, 8])
set_mutable1 = set([4, 3, 11, 7, 5, 2, 1, 4])
set_mutable2 = set([11, 5, 9, 2, 4, 8])
print(set_mutable1)
print(set_mutable2)
print(set_mutable1.isdisjoint(set_mutable2))

#determina si hay subconjuntos de otros
set_mutable1 = set([4, 3, 11, 7, 5, 2, 1, 4])
set_mutable2 = set([11, 5, 9, 2, 4, 8])
set_mutable3 = set([11, 5, 2, 4])
print( set_mutable1)
print(set_mutable2)
print(set_mutable3)
print(set_mutable2.issubset(set_mutable1))
print(set_mutable3.issubset(set_mutable1))

#devuelve true si el conjunto es superconjunto
set_mutable1 = set([4, 3, 11, 7, 5, 2, 1, 4])
set_mutable2 = set([11, 5, 9, 2, 4, 8])
set_mutable3 = set([11, 5, 2, 4])
print(set_mutable1)
print(set_mutable2)
print(set_mutable3)
print(set_mutable1.issuperset(set_mutable2))
print(set_mutable1.issuperset(set_mutable3))

#elimina elementos arbitrariamente
paquetes = {'python', 'zope', 'plone', 'django'}
paquetes
print("Valor aleatorio devuelto es:", paquetes.pop())

#elimina elementos de forma especifica
paquetes = {'python', 'zope', 'plone', 'django'}
paquetes
paquetes.remove('django')
paquetes

#devuleve elementos, diferente a la interseccion
set_mutable1 = set([4, 3, 11, 7, 5, 2, 1, 4])
set_mutable2 = set([11, 5, 9, 2, 4, 8])
print(set_mutable1)
print(set_mutable2)
print(set_mutable1.symmetric_difference(set_mutable2))

#actualiza la variable
proyecto1 = {'python', 'plone', 'django'}
print(proyecto1)
proyecto2 = {'django', 'zope', 'pyramid'}
print(proyecto2)
proyecto1.symmetric_difference_update(proyecto2)
print(proyecto1)

#union de conjuntos
set_mutable1 = set([4, 3, 11, 7, 5, 2, 1, 4])
set_mutable2 = set([11, 5, 9, 2, 4, 8])
print(set_mutable1)
print(set_mutable2)
print(set_mutable1.union(set_mutable2))

#otra forma de union de conjuntos
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}
c = a | b
print(c)

#actualiza valores
version_plone_dev = set([5.1, 6])
print(version_plone_dev)
versiones_plone = set([2.1, 2.5, 3.6, 4])
print(versiones_plone)
versiones_plone.update(version_plone_dev)
print(versiones_plone)

cadena = 'abc'
print(cadena)
conjunto = {1, 2}
conjunto.update(cadena)
print(conjunto)

diccionario = {'key': 1, 2:'lock'}
diccionario.items()
conjunto = {'a', 'b'}
conjunto.update(diccionario)
print(conjunto)

