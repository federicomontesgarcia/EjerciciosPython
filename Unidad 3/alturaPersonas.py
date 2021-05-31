#Se ingresan un conjunto de n alturas de personas por teclado. Mostrar la altura promedio de las personas.

alturasP = set()
n = 1
i = 0
sumAlturas = 0
while n < 6:
    alturasP.add(input("Ingrese alturas de personas: "))  
    k = int(len(alturasP))
    n = n + 1

for i in alturasP:
    j = int(i)
    sumAlturas = sumAlturas + j  

promAlturas = sumAlturas/k
print("las alturas ingresadas son:",alturasP)
print("El promedio de alturas es:",promAlturas,"metros")