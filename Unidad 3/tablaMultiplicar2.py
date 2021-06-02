# Confeccionar un programa que permita ingresar un valor del 1 al 10 y nos muestre la tabla de multiplicar 
#del mismo (los primeros 12 términos) Ejemplo: Si ingreso 3 deberá aparecer en pantalla los 
#valores 3, 6, 9, hasta el 36.

n = input("Ingrese un numero entre el 1 y el 10: ")
n = int(n)

mult = 1
i = 1
while i <= 12:
    mult = n * i
    print("la multiplicación de",n,"*",i,"es igual a:",mult)
    i = i + 1
    
else:
    print("la multiplicación terminó")
    