
# Se cuenta con la siguiente información: Las edades de 5 estudiantes del turno mañana. Las edades de 6 estudiantes 
# del turno tarde. Las edades de 11 estudiantes del turno noche. Las edades de cada estudiante deben ingresarse por 
# teclado. a) Obtener el promedio de las edades de cada turno (tres promedios) b) Imprimir dichos promedios 
# (promedio de cada turno) c) Mostrar por pantalla un mensaje que indique cuál de los tres turnos tiene un promedio 
# de edades mayor.

turnoManana = []
turnoTarde = []
turnoNoche = []

i = 0
j = 0
k = 0
suma1 = 0
suma2 = 0
suma3 = 0
for m in range (5):
    turnoManana.append(input("ingrese edad de estudiante para el turno de la mañana "))

for n in turnoManana:
    suma1 = suma1 + int(turnoManana[i])
    i = i + 1
promedioManana = suma1 / len(turnoManana)
print("edades del turno de la manana:",turnoManana)
print("el promedio de edades de estudiantes del turno de la manana es:",promedioManana)
print()

for m in range (6):
    turnoTarde.append(input("ingrese edad de estudiante para el turno de la tarde "))
    

for n in turnoTarde:
    suma2 = suma2 + int(turnoTarde[j])
    j = j + 1
promedioTarde = suma2 / len(turnoTarde)
print("edades del turno de la manana:",turnoTarde)
print("el promedio de edades de estudiantes del turno de la manana es:",promedioTarde)
print()

for m in range (11):
    turnoNoche.append(input("ingrese edad de estudiante para el turno de la noche "))
    
for n in turnoNoche:
    suma3 = suma3 + int(turnoNoche[k])
    k = k + 1
promedioNoche = suma3 / len(turnoNoche)
print("edades del turno de la manana:",turnoNoche)
print("el promedio de edades de estudiantes del turno de la manana es:",promedioNoche)

if promedioManana > promedioTarde and promedioManana > promedioNoche:
    print("el turno con mayor promedio de edad es el Turno de la manana")
if promedioTarde > promedioNoche and promedioTarde > promedioManana:
    print("el turno con mayor promedio de edad es el Turno de la tarde")
if promedioNoche > promedioManana and promedioNoche > promedioTarde:
    print("el turno con mayor promedio de edad es el Turno de la noche")