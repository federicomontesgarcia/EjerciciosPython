def matricularCurso(estudiantes):

    i = 0
    j = 0
    k = 0
    for n in range (len(estudiantes)):
        if int(estudiantes[k][2]) <= 30:
            estudiantes[k].append('A-Principiante')

        if int(estudiantes[k][2]) > 30 and (estudiantes[k][2] <= 70):
            estudiantes[k].append('B-Intermedio')

        if int(estudiantes[k][2]) > 70:
            estudiantes[k].append('C-Avanzado')
        k = k + 1
        i = i + 1

    return("Identificación\tNombre\tPuntaje\tGrupo\n"
    "\n{0}\t{1}\t{2}\t{3}"
    "\n{4}\t{5}\t{6}\t{7}"
    "\n{8}\t{9}\t{10}\t{11}"
    .format(estudiantes[0][0], estudiantes[0][1], estudiantes[0][2], estudiantes[0][3],estudiantes[1][0], 
    estudiantes[1][1], estudiantes[1][2], estudiantes[1][3], estudiantes[2][0], estudiantes[2][1], estudiantes[2][2], 
    estudiantes[2][3]))

matricula = matricularCurso([['1110033495', 'Violeta Murcia', 63], ['1110783206', 'Claudia Gallego', 77], ['1110953217', 'Manuel Gonzalez', 45]])
print(matricula)