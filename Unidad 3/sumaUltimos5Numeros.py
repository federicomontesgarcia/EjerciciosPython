#Desarrollar un programa que solicite la carga de 10 números e imprima la suma de los últimos 5 valores ingresados.

numeros = []
numeros2 = []

for num in range(10):
    numeros.append(int(input("Ingrese un numero: ")))
print("lista de los 10 números ingresados:",numeros)

numeros.reverse()
i = 0
while i <= 4:    
    numeros2.append(numeros[i])
    i = i + 1
print("los ultimos 5 números ingresados son:",numeros2)

j = 0
suma = 0
for num in numeros2:
    suma = suma + num
print("La suma de los ultimos 5 números es:",suma)    


