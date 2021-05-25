Estudiantes = {  'Alumno1': {'nombre':'Daniel', 'edad':11, 'estatura':1.75, 'grado':'Master'},
                 'Alumno2':{'nombre':'David', 'edad':32, 'estatura':1.85, 'grado':'Doctor'}   }

print(Estudiantes)
#Comparemos los nombres de los estudiantes

if Estudiantes['Alumno1']['nombre'] == Estudiantes['Alumno2']['nombre']:
    print("Los nombres son iguales")
else:
    print('Los nombres son diferentes')

#Miremos quien es mayor

if Estudiantes['Alumno1']['edad'] > Estudiantes['Alumno2']['edad']:
    
    print(str(Estudiantes['Alumno1']['nombre']) + ' es mayor') 
    mayor = {'nombremayor':Estudiantes['Alumno1']['nombre'], 'edadmayor':Estudiantes['Alumno1']['edad'] }
    
elif Estudiantes['Alumno1']['edad'] < Estudiantes['Alumno2']['edad']:
    
    print(str(Estudiantes['Alumno1']['nombre']) + ' es menor') 
    
    mayor = {'nombremayor':Estudiantes['Alumno2']['nombre'], 'edadmayor':Estudiantes['Alumno2']['edad'] }
print(mayor)