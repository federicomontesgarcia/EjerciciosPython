original = ['201','300','398','821','447','723','206','909','909','201','338','424','748','765','201','463','821','909','909','300']
print("todos los numeros caidos son:",original)
caidos = set(original)
caidos = list(caidos)
print("Los números caídos en lista son:",caidos)
print()

#funcion para sacar lista de numeros sin repetir y las veces que se repite
def calcularNumerosUnicos(mes):
    i = 0
    k = 0
    num = []
    rep = []
    numRep = [num, rep]

    for l in range (len(mes)):
        num.append(caidos[i])
        cant = 0
        j = 0
        for k in range (len(original)):
            if int(mes[i]) == int(original[j]):
                cant = cant + 1
            j = j + 1
        
        rep.append(cant)
        i = i + 1 

    print("Listado de numeros y las veces que se repiten",numRep)

#Imprimir la cantidad de veces que un numero se repite 
    i = 0
    j = 0
    for numero in num:
        print("el numero",num[i],"se repite",rep[j],"veces")
        i = i + 1
        j = j + 1


NumerosUnicos = (calcularNumerosUnicos(mes = caidos))
