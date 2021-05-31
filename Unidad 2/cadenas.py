fruta = 'kamiesunafresabella'
letra = fruta[9]

print(letra)
longitud = len(fruta)
print(longitud)
ultimo = fruta[longitud-1]
print(ultimo)
print(fruta[0:9])
print(fruta[9:])

saludo = '¡Hola, mundo!'
nuevo_saludo = 'J' + saludo[1:]
print(nuevo_saludo)

if fruta < 'banana':
    print('Tu palabra,' + fruta + ', viene antes de banana')
elif fruta > 'banana':
    print('Su palabra,' + fruta + ', viene después de banana.')
else:
    print('Está bien, su palabra es banana')

Cadena = 'Hola mundo'
print(type(Cadena))
#print(dir(Cadena))
#print(help(str.capitalize))

palabra = 'banana'
palabra_nueva = palabra.upper()
print(palabra_nueva)

palabra = 'banana'
index = palabra.find('na')
print(index)

linea = '        Aquí vamos            '
print(linea.strip())

data = 'De stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008'
enlaposicion = data.find('@')
print(enlaposicion)

camellos = 42
texto = 'He visto %d camellos' % camellos
print(texto)

# Saldrán dos líneas en pantalla, una con Hola, la otra con Mundo
cadena = "\tHola\nMundo"  
print(cadena)

cadena = "un uno, un dos, un tres"

print (cadena.count("un"))        # Saca 4, hay 4 "un" en cadena.
print (cadena.count("un",10))     # Saca 1, hay 1 "un" a partir de la posición 10 de cadena.
print (cadena.count("un",0,10))   # Saca 3, hay 3 "un" entre la posición 0 y la 10.

cadena = "un uno, un dos, un tres"

print (cadena.replace("un", "XXX"))        # saca por pantalla "XXX XXXo, XXX dos, XXX tres"
print (cadena.replace("un", "XXX", 2))     # Sólo reemplaza 2 "un", así que saca por pantalla "XXX XXXo, un dos, un tres"

# saca "El valor es 12
print ("El valor es {}".format(12))

# Tres conjuntos {}, el primero para el primer parámetro de format(), el segundo para el segundo
# y así sucesivamente.
# saca "Los valores son 1, 2 y 3"
print ("Los valores son {}, {} y {}".format(1,2,3))

# Entre las llaves podemos poner la posición del parámetro. {2} es el tercer parámetro de format()
# {0} es el primer parámetro de format.
# saca "Los valores son 3, 2 y 1"
print ("Los valores son {2}, {1} y {0}".format(1,2,3))

# saca "2 y 1"
print ("{pepe} y {juan}".format(juan=1, pepe=2))

mensaje1 = 'Hola' + ' ' + 'Mundo'
print(mensaje1)

mensaje2a = 'Hola ' * 3
mensaje2b = 'Mundo'
print(mensaje2a + mensaje2b)

mensaje3 = 'Hola'
mensaje3 += ' '
mensaje3 += 'Mundo'
print(mensaje3)
