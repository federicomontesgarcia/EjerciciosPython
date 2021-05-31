#Realizar un programa que lea los lados de n triángulos, e informar: 
# a) De cada uno de ellos, qué tipo de triángulo es: equilátero (tres lados iguales), 
# isósceles (dos lados iguales), o escaleno (ningún lado igual) 
#b) Cantidad de triángulos de cada tipo.

lado1 = []
lado2 = []
lado3 = []
triangulo = []
listaT = [lado1, lado2, lado3]

n = 0
i = 0
t = 1

print(("Ingrese la cantidad de triángulos que va a ingresar: "))
n = int(input())

while t <= n:
    lado1.append(input("ingresar valor del primer lado del triángulo: "))
    lado2.append(input("ingresar valor del segundo lado del triángulo: "))
    lado3.append(input("ingresar valor del tercer lado del triángulo: "))
    print("")
    t = t + 1

print("lados",listaT)

for m in range (len(lado1)):
    if lado1[i] == lado2[i] and lado1[i] == lado3[i]:
        triangulo.append('equilatero')
        print("El triángulo",i+1,"es",triangulo[i])

    elif lado1[i] != lado2[i] and lado1[i] != lado3[i]:
        triangulo.append('escaleno')
        print("El triángulo",i+1,"es",triangulo[i])
   
    else:
        triangulo.append('isóseles')
        print("El triángulo",i+1,"es",triangulo[i])
    
    i = i + 1
    

print("La cantidad de triángulos escalenos son:",triangulo.count('escaleno'))

print("La cantidad de triángulos equilateros son:",triangulo.count('equilatero'))

print("La cantidad de triángulos isóseles son:",triangulo.count('isóseles'))












