#Desarrollar un programa que permita cargar n números enteros y luego nos informe cuántos valores 
#fueron pares y cuántos impares. Emplear el operador “%” en la condición de la estructura condicional 
#(este operador retorna el resto de la división de dos valores, por ejemplo 11%2 retorna un 1): if valor%2==0:
numero = 0
par = 0
impar = 0
numero = int(input("ingrese un número: "))
while numero != -1:
    if (numero % 2) == 0:
        par = par + 1
    else:
        impar = impar + 1
    numero = int(input("ingrese un número: "))
print("cantidad de numeros pares =",par)
print("cantidad de numeros impares =",impar)

