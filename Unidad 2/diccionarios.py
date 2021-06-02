diccionario = {"total": 55}
print(diccionario)
otrodiccionario = {"copia": 123.23}
print(otrodiccionario)

print("\n")

diccionario = {"total": 55, "descuento": True, 15: "15"}

print(diccionario)

diccionarioEjemploExcel ={"nombre":5+2,"telefono":3363692, "edad":33, "ciudad":"Pereira"}

print(diccionarioEjemploExcel)

print("\n")

usuario = {
    'nombre': 'Nombre del usuario',
    'edad' : 23, 
    'curso': 'Curso de Python',
    'skills':{
        'programacion' : True,
        'base_de_datos': False
    },
    'No medallas' : 10
}

print(usuario)

print(usuario['curso'])
print(usuario['skills'])
print(usuario['skills']['base_de_datos'])

print("\n")

diccionario = dict(total=55, descuento=True, descuento5=True, subtotal="15")

print(diccionario)
print(diccionario['subtotal'])

diccionario = dict()
print(diccionario)

print("\n")

diccionario['marca'] = 'Mazda'
print(diccionario['marca'])

diccionario['marca'] = 'Subaru'
print(diccionario['marca'])

print(diccionario)

print("\n")

diccionario = {'Eduardo': 1, 'Fernando':2, 'Uriel':3, 'Rafael': 4}
print(diccionario)
print(diccionario.keys())
print(diccionario.values())

print("\n")

versiones = dict(python=2.7, zope=2.13, plone=5.1)
print(versiones)
versiones.clear()
print(versiones)

print("\n")

versiones = dict(python=2.7, zope=2.13, plone=5.1)
otra_versiones = versiones.copy()
print(versiones == otra_versiones)
print(versiones)
print(otra_versiones)

print("\n")

secuencia = ('python', 'zope', 'plone')
versiones = dict.fromkeys(secuencia)
print("Nuevo Diccionario : %s" %  str(secuencia))
print("Nuevo Diccionario : {}".format(str(versiones)))
versiones = dict.fromkeys(secuencia, 0.1)
print("Nuevo Diccionario : %s" %  str(versiones))

print("\n")

versiones = dict(python=2.7, zope=2.13, plone=5.1)
versiones.get('plone')
print(versiones.get('plone'))

print("\n")

versiones = dict(python=2.7, zope=2.13, plone=5.1)
print(versiones.items())

print("\n")

versiones = dict(python=2.7, zope=2.13, plone=5.1)
print(versiones)
print(versiones.pop('zope'))
print(versiones)

print("\n")

versiones = dict(python=2.7, zope=2.13, plone=5.1)
print(versiones)
versiones_adicional = dict(django=2.1)
print(versiones_adicional)
versiones.update(versiones_adicional)
print(versiones)

print("\n")

usuario = {
    'nombre': 'Nombre del usuario',
    'edad' : 23, 
    'curso': 'Curso de Python',
    'skills':{
        'programacion' : True,
        'base_de_datos': False
    },
    'No medallas' : 10
}

print(len(usuario))

print("\n")

versiones = dict(python=2.7, zope=2.13, plone=5.1, django=2.1)
print(versiones)
{'python': 2.7, 'zope': 2.13, 'plone': 5.1, 'django': 2.1}
del versiones["python"]
print(versiones)











































