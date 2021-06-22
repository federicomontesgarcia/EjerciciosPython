import numpy as np

def generarResultados(datos):
    
    participante1 = []
    participante2 = []
    participante3 = []
    part1 = []
    part2 = []
    part3 = []

    participante1 = datos[0]
    participante2 = datos[1]
    participante3 = datos[2]
# 
    def newDatos(participante, part):    
        for i in range (len(participante)):
            if participante[i] < 6:
                part.append(5)
            else:
                part.append(participante[i])
            i = i + 1
    
    new = newDatos(participante1, part1)
    new = newDatos(participante2, part2)
    new = newDatos(participante3, part3)

    sumaPart1 = np.array(part1)
    sum1 = sumaPart1.sum()
    prom1 = round(sumaPart1.mean(), 2)
    
    sumaPart2 = np.array(part2)
    sum2 = sumaPart2.sum()
    prom2 = round(sumaPart2.mean(), 2)
    
    sumaPart3 = np.array(part3)
    sum3 = sumaPart3.sum()
    prom3 = round(sumaPart3.mean(), 2)
    
    promTotal = round(((prom1 + prom2 + prom3)/3), 2)
    
    #--------------------------
    resultados = [sum1, sum2, sum3]
    mayor = np.array(resultados)
    numMayor = (np.amax(mayor))
    
    resulPartic = {'1':sum1, '2':sum2, '3':sum3}
    resul = dict(filter(lambda x: x[1] == numMayor, resulPartic.items()))
    
    for i in resul.keys():
        ganador = int(i)

    resultJurados = {'puntaje promedio':promTotal, 'puntaje participante 1':sum1, 'puntaje participante 2':sum2, 'puntaje participante 3':sum3, 'participante ganador':ganador}
    return resultJurados

resultados = generarResultados(datos = [[6,8,9], [10,7,8], [4,5,7]])
print(resultados)