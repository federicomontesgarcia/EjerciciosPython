# Confeccionar un programa que lea n pares de datos, cada par de datos corresponde a la medida 
# de la base y la altura de un triángulo. El programa deberá informar: a) De cada triángulo la 
# medida de su base, su altura y su superficie. b) La cantidad de triángulos cuya superficie es mayor a 12.
base = []
altura = []
superficie = []
listaT = [base, altura, superficie]

n = 1
m = 1
i = 0
j = 0
a = 0
b = 0
c = 0
y = 0

print(("Ingrese la cantidad de par de datos que va a ingresar: "))
t = int(input())

while n <= t:
    base.append(input("ingresar valor de la base del triángulo: "))
    altura.append(input("ingresar valor de la altura del triángulo: "))
    print("")
    n = n + 1

print(listaT)

for m in range (len(base)):
    superficie.append(((int(base[i]))*(int(altura[j])))/2)
    i = i + 1
    j = j + 1
print(listaT)

for o in range (len(base)):
    o = o + 1
    print("triangulo",o,"tiene base =",base[a],",tiene altura =",altura[b],"y superficie =",superficie[c])
    a = a + 1
    b = b + 1
    c = c + 1

suma = 0
for x in range (len(base)):
    if superficie[y] > 12:
        suma = suma + 1
    y = y + 1
print("la cantidad de triángulos con superficie mayor a 12 son:",suma)












