#Escribir un programa que solicite ingresar 10 notas de alumnos y nos informe cuántos 
#tienen notas mayores o iguales a 7 y cuántos menores.


listaNotas = []
for x in range(10):
        Nota = input("ingrese una nota: ")
        listaNotas.append(Nota)
print(listaNotas)

menores = 0
mayores = 0
i = 0
for i in range (len(listaNotas)):
    if int(listaNotas[i]) > 6:
        mayores = mayores + 1
    else:
        menores = menores + 1

print("las notas mayores o iguales a 7 son:",mayores)
print("las notas menores a 7 son:",menores)



