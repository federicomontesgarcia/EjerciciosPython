#Mostrar los múltiplos de 8 hasta el valor 500. Debe aparecer en pantalla 8 - 16 - 24, etc.
multiplos = 0
i = 1
while multiplos < 500:
    multiplos = 8 * i
    print("8 *",i,"=",multiplos)
    i = i + 1
    