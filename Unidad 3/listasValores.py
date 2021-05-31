#Realizar un programa que permita cargar dos listas de 15 valores cada una. Informar 
#con un mensaje cuál de las dos listas tiene un valor acumulado mayor 
#(mensajes "Lista 1 mayor", "Lista 2 mayor", "Listas iguales")

lista1 = []
lista2 = []
i = 1
j = 1
for i in range (3):
    lista1.append(input("ingresar valor a la primera lista: "))

for j in range (3):
    lista2.append(input("ingresar valor a la segunda lista: "))

print("lista1:",lista1)
print("lista2:",lista2)

sumaLista1 = 0
sumaLista2 = 0
for k in lista1:
    l = int(k)
    sumaLista1 = sumaLista1 + l  

for m in lista2:
    n = int(m)
    sumaLista2 = sumaLista2 + n   

print("Suma Lista1:",sumaLista1)
print("Suma Lista2:",sumaLista2)

if lista1 > lista2:
    print("Lista 1 mayor")
elif lista2 > lista1:
    print("Lista 1 mayor")
else:
    print("Listas iguales")