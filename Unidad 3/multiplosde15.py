# Se realiza la carga de 10 valores enteros por teclado. Se desea conocer: a) La cantidad de valores ingresados negativos. 
# b) La cantidad de valores ingresados positivos. c) La cantidad de múltiplos de 15. d) El valor acumulado de los números 
# ingresados que son pares.

num = []
num2 = []

for n in range (10):
    num.append(input("Ingrese un numero, positivo o negativo: "))
    n = n + 1

print("Lista de 10 números:",num)

num2 = num.copy()
print(num2)

numNegativo = 0
numPositivo = 0
mult = 0
mult1 = 0
for m in num:
    if int(m) > 0:
        if (int(m)%15) == 0:
            #print("El numero",m,"SI es múltiplo de 15")
            numPositivo = numPositivo + 1
            mult = mult + 1
    
    if int(m) < 0:
        num = num * (-1)
        if (int(m)%15) == 0:
            #print("El numero",m,"SI es múltiplo de 15")
            numNegativo = numNegativo + 1
            mult1 = mult1 + 1
    
print()
print("La cantidad de números negativos múltiplos de 15 son:",numNegativo)


print("La cantidad de números positivos múltiplos de 15 son:",numPositivo)

multiplos = mult + mult1
print("La cantidad de números múltiplos de 15 son:",multiplos)

numPar = 0
numPar1 = 0

for numero in num2:
    if int(numero) > 0:
        if (int(numero)%2) == 0:
            #print("El numero",numero,"SI es par")
            numPar = numPar + 1
    
    if int(numero) < 0:
        num2 = num2 * (-1)
        if (int(numero)%2) == 0:
            #print("El numero",numero,"SI es par")
            numPar1 = numPar1 + 1

par = numPar + numPar1
print("La cantidad de números pares son:",par)