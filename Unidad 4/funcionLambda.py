suma = lambda val1, val2 : val1 + val2
resta = lambda val1, val2 : val1 - val2
multiplicacion = lambda val1, val2 : val1 * val2

operacion = lambda operador, val1, val2 : operador(val1, val2)

resultado = operacion(multiplicacion, 10, 20)

print(resultado)

print()
#-------------------------------------------------------------

total = lambda precio, cantidad : precio * cantidad
descuento = lambda total : total - (total * 0.3)
print(descuento(total(1200, 5)))

#------------------------------------------------------------

con_asterisco =  lambda *args : args[1]

print(con_asterisco('hola', 'mundo', 'hoy'))

print()
#--------------------------------------------------------------

con_doble_asterisco = lambda **kwargs : kwargs.get('apellido')

print(con_doble_asterisco(nombre ='pedro', apellido ='gomez'))

