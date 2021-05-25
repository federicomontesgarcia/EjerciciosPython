Informacion = {  'Alumno1': {'nombre':'Daniel', 'edad':11, 'estatura':1.75, 'grado':'Master'},
                 'Alumno2':{'nombre':'David', 'edad':32, 'estatura':1.85, 'grado':'Doctor'}   }

# print(Estudiantes)
# 
# if Estudiantes['Alumno1']['nombre'] == Estudiantes['Alumno2']['nombre']:
    # print("Los nombres son iguales")
# else:
    # print('Los nombres son diferentes')

if Informacion['Alumno1']['edad'] > Informacion['Alumno2']['edad']:
    
    print(str(Informacion['Alumno1']['nombre']) + ' es mayor') 
    mayor = {'nombremayor':Informacion['Alumno1']['nombre'], 'edadmayor':Informacion['Alumno1']['edad'] }
    
elif Informacion['Alumno1']['edad'] < Informacion['Alumno2']['edad']:
    
    print(str(Informacion['Alumno1']['nombre']) + ' es menor') 
    
    mayor = {'nombremayor':Informacion['Alumno2']['nombre'], 'edadmayor':Informacion['Alumno2']['edad'] }
print(mayor)