# El restaurante Donde Monty ha decidido implementar un software que le permita ingresar los datos del pedido 
# del almuerzo de sus clientes, ingresando cada uno de los platos de acuerdo a su categoría y teniendo en cuenta 
# descuentos especiales si el cliente incluye algunos elementos en su pedido, para así generar el valor de la cuenta.

def realizarPedido(sopa:str, plato_principal:str, bebida:str, postre:str)->dict:
    dict = {'sopa' : {'Sopa de pastas':3000, '':0}, 
        'plato_principal' : {'Pollo apanado':7000, 'Albóndigas en salsa':8000, '':0}, 
        'bebida' : {'Jugo de uva':2000, 'Limonada':1500, '':0}, 
        'postre' : {'Merengón':5000, 'Leche asada':4000, '':0} }

    platos = ['sopa', 'plato principal', 'bebida', 'postre', 'total']
    producto = []
    valor = []
    
    producto.append(sopa)
    uno = dict['sopa'].get(sopa)
    valor.append(uno)

    producto.append(plato_principal)
    uno = dict['plato_principal'].get(plato_principal)
    valor.append(uno)
    
    producto.append(bebida)
    uno = dict['bebida'].get(bebida)
    valor.append(uno)    
    
    producto.append(postre)
    uno = dict['postre'].get(postre)
    valor.append(uno)   

    if 'Merengón' in producto and 'Pollo apanado' in producto or 'Merengón' in producto and 'Sopa de pastas' in producto:
        suma = 0
        descuento = 0
        total = 0
        for i in valor:
            i = float(i) 
            suma = suma + i
            descuento = suma * 0.3
            total = suma - descuento
            total = int(total)
        producto.append(total)

    else:
        suma = 0
        total = 0
        for i in valor:
            i = int(i) 
            suma = suma + i
            total = int(suma)
        producto.append(total)
    
    nuevoDict = {platos[i]: producto[i] for i in range(len(platos))}
    return(nuevoDict)
    
lista = realizarPedido(sopa ='Sopa de pastas', plato_principal = 'Pollo apanado', bebida = 'Jugo de uva', postre = 'Merengón')
print(lista)

# pruebas
print(realizarPedido('', 'Albóndigas en salsa', 'Limonada', 'Leche asada'))

print(realizarPedido('Sopa de pastas', 'Albóndigas en salsa', 'Limonada', 'Merengón'))


