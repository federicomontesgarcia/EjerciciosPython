# En una empresa trabajan n empleados cuyos sueldos oscilan entre $100 y $500, realizar 
# un programa que lea los sueldos que cobra cada empleado e informe cuántos empleados 
# cobran entre $100 y $300 y cuántos cobran más de $300. Además el programa deberá 
# informar el importe que gasta la empresa en sueldos al personal.
sueldo = 0
cuentaMas = 0
cuentaMenos = 0
sumaSueldo = 0
print("Ingrese sueldos no mayores a 500, con (-1) sale del programa")
#sueldo = int(input("ingrese sueldo del empleado: "))
while sueldo != -1:
    sumaSueldo = sumaSueldo + sueldo
    if sueldo >= 100 and sueldo <= 300:
        cuentaMenos = cuentaMenos + 1
    if sueldo > 300 and sueldo <= 500:
        cuentaMas = cuentaMas + 1
    sueldo = int(input("ingrese sueldo del empleado: "))
print("El importe total de sueldos es:",sumaSueldo,"pesos")
print("los sueldos menores de 300 son:",cuentaMenos)
print("los sueldos mayores de 300 son:",cuentaMas)