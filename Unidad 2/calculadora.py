
try:
    operaciones = { 43:'suma', 45:'resta', 42:'multiplicación', 47:'división' }
    valor1 = int(input("ingrese el primer numero: "))
    valor2 = int(input("ingrese el segundo numero: "))
    op = int(ord(input("ingrese el tipo de operacion: ")))
    
    def CalcularOperacion(valor1, valor2):
    
        if op == 43:
            operacion = valor1 + valor2
            return operacion
            
        elif op == 45:
            operacion = valor1 - valor2
            return operacion
            
        elif op == 42:
            operacion = valor1 * valor2
            return operacion
            
        elif op == 47 and valor2 != 0:
            operacion = valor1 / valor2
            return operacion
            
        else:
            print("la operacion no se puede realizar")

    resultado = CalcularOperacion(valor1, valor2)
    print("El resultado de la", operaciones[op], "es:",resultado)

except ValueError:
    print("Ingresó un dato no válido,vuelva a intentarlo")
        
    

