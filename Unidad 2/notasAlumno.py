#21. Hacer un programa que pida al usuario las tres notas de un alumno (deben estar entre 0 y 5 
# y pueden tener decimales) y calcule el promedio e indique mediante un mensaje si aprobó o no 
# (aprueba con nota mayor a 3). Se debe validar que las notas introducidas estén dentro del rango permitido.
Notas = ['Notas1', 'Notas2', 'Notas3']
Notas1 = float(input("Ingrese la primera nota: "))
Notas2 = float(input("Ingrese la segunda nota: "))
Notas3 = float(input("Ingrese la tercera nota: "))
print(Notas1)
print(Notas2)
print(Notas3)

if Notas1 >= 0 and Notas1 <= 5 and Notas2 >= 0 and Notas2 <= 5 and Notas3 >= 0 and Notas3 <= 5:  
    Promedio = round((Notas1 + Notas2 + Notas3)/3,2)
    if Promedio >= 3.0:
        print("El promedio de las notas es:",Promedio,",el estudiante SI aprobó")
    else:
        print("El promedio de las notas es:",Promedio,",el estudiante NO aprobó")
else:
    print("valor o valores ingresados no validos")