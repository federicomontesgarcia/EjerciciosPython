def suma (val1 = 0, val2 = 0):
    return val1 + val2

def resta (val1 = 0, val2 = 0):
    return val1 - val2

def multiplicacion (val1 = 0, val2 = 0):
    return val1 * val2

def operacion (function, val1 = 0, val2 = 0):
    return function(val1, val2)

resultado = operacion(multiplicacion, 10, 20)
print(resultado)
