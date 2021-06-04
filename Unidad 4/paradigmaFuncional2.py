def crear_Funcion(operador):
    if operador == '+':
        def suma(val1 = 0, val2 = 0):
            return val1 + val2
        return suma
    if operador == '-':
        def resta(val1 = 0, val2 = 0):
            return val1 - val2
        return resta

def operacion (funcion, val1 = 0, val2 = 0):
    return funcion(val1, val2)

operador = input("seleccione la operacion: (- o + ): ")
num1 = int(input("digite el numero 1: "))
num2 = int(input("digite el numero 2: "))
resultado = operacion(crear_Funcion(operador), num1, num2)
print(resultado)