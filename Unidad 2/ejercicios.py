#1. Leer un número entero y determinar si es un número terminado en 4.
numero = 6754784

ultimoNumero = int(str(numero)[-1])

if ultimoNumero == 4:
    print("1. El numero",numero,"SI termina en 4")
else:
    print("1. El numero",numero,"NO termina en 4")

#___________________________________________________________
#2. Leer un número entero y determinar si tiene 3 dígitos.
numero = 749
numero = str(numero)
cant = (len(numero))

if cant == 3:
    print("2. El numero",numero,"SI tiene 3 dígitos")
else:
    print("2. El numero",numero,"NO tiene 3 dígitos")

#__________________________________________________________
#3. Leer un número entero de dos dígitos y determinar si ambos dígitos son pares.
numero = 88

if numero > 0 and numero < 100:
    numero = str(numero)
    num1 = numero[0]
    num2 = numero[1]
    mod1 = int(num1) % 2
    mod2 = int(num2) % 2
    if mod1 == 0 and mod2 == 0:
        print("3. Los 2 dígitos de",numero,"SI son pares")
    else:
        print("3. Los 2 dígitos de",numero,"NO son pares")
else:
     print("3. El numero",numero,"no es valido")
#_____________________________________________________________
#4. Leer un número entero de dos dígitos menor que 20 y determinar si es primo.
numero = 9
if numero > 0 and numero < 20:
    contador = 0
    flag= False
    for i in range(1,numero+1):
        if (numero% i)==0:
            contador = contador + 1
        if contador >= 3:
            flag=True
            break

    if contador==2 or flag==False:
        print("4. El número",numero,"SI es primo")
    else: print("4. El número",numero,"NO es primo")
else:
    print("4. El número ingresado es inválido")
#_____________________________________________________________
#5. Leer un número entero de dos dígitos y determinar si es primo y además si es negativo.
num = -9
if num < 0 and num > -100:
    numero = abs(num)
    flag= False
    contador = 0
    for i in range(1,numero+1):
        if (numero% i)==0:
            contador = contador + 1
        if contador >= 3:
            flag=True
            break

    if contador==2 or flag==False:
        print("5. El número",num,"SI es primo y es Negativo")
    else: print("5. El número",num,"NO es primo pero es Negativo")

elif num > 0 and num < 100:
    numero = num
    flag= False
    contador = 0
    for i in range(1,numero+1):
        if (numero% i)==0:
            contador = contador + 1
        if contador >= 3:
            flag=True
            break

    if contador==2 or flag==False:
        print("5. El número",num,"SI es primo y es Positivo")
    else: print("5. El número",num,"NO es primo pero es Positivo")

else:
    print("5. El numero ingresado no es válido")


#_________________________________________________________________   
#6. Leer un número entero de dos dígitos y determinar si los dos dígitos son iguales.
numero = 33

if numero > 0 and numero < 100:
    numero = str(numero)
    num1 = numero[0]
    num2 = numero[1]
    if num1 == num2:
        print("6. Los 2 dígitos de",numero,"SI son iguales")
    else:
        print("6. Los 2 dígitos de",numero,"NO son iguales")
else:
     print("6. El numero",numero,"no es valido")

#________________________________________________________________
#7. Leer dos números enteros y determinar cuál es el mayor.
numero1 = 73
numero2 = 45

if numero1 > numero2:
    print("7. El número",numero1,"es el mayor de los dos")
else:
    print("7. El número",numero2,"es el mayor de los dos")

#_______________________________________________________________
#8. Leer dos números enteros de dos dígitos y determinar a cuánto es igual la suma de todos los dígitos.
numero1 = 75
numero2 = 25

if numero1 > 0 and numero1 < 100 and numero2 > 0 and numero2 < 100:
    suma = numero1 + numero2
    print("8. La suma de",numero1,"y",numero2,"es:",suma)
else:
     print("8. hay almenos un numero no valido")
#_______________________________________________________________
#9. Leer un número entero de tres dígitos y determinar en qué posición está el mayor dígito.
numero = 369

if numero > 0 and numero < 999:
    numero = str(numero)
    num1 = numero[0]
    num2 = numero[1]
    num3 = numero[2]
    if num1 > num2 and num1 > num3:
        print("9. El mayor dígito (",num1,") se encuentra en la posición 0")
    elif num2 > num1 and num2 > num3:
        print("9. El mayor dígito (",num2,") se encuentra en la posición 1")
    elif num3 > num1 and num3 > num2:
        print("9. El mayor dígito (",num3,") se encuentra en la posición 2")
    else:
        print("9. no hay numero mayor")
else:
    print("9. El numero",numero,"no es valido")

#__________________________________________________________
#10. Leer un número entero de tres dígitos y determinar si algún dígito es múltiplo de los otros.
numero = 139

if numero > 0 and numero < 999:
    numero = str(numero)
    num1 = numero[0]
    num2 = numero[1]
    num3 = numero[2]
    if int(num1)%int(num2) == 0:
        print("10. El dígito",num1,"es múltiplo de",num2)
    else:
        print("10.",num1,"no es múltiplo de",num2)
    if  int(num1)%int(num3) == 0:
        print("10. El dígito",num1,"es múltiplo de",num3)
    else:
        print("10.",num1,"no es múltiplo de",num3)
    if int(num2)%int(num1) == 0:
        print("10. El dígito",num2,"es múltiplo de",num1)
    else:
        print("10.",num2,"no es múltiplo de",num1)
    if int(num2)%int(num3) == 0:
        print("10. El dígito",num2,"es múltiplo de",num3)
    else:
        print("10.",num2,"no es múltiplo de",num3)
    if int(num3)%int(num1) == 0:
        print("10. El dígito",num3,"es múltiplo de",num1)
    else:
        print("10.",num3,"no es múltiplo de",num1)
    if int(num3)%int(num2) == 0:
        print("10. El dígito",num3,"es múltiplo de",num2)
    else:
        print("10.",num3,"no es múltiplo de",num2)
else:
    print("10. El numero",numero,"no es valido")

#_______________________________________________________________
#11. Leer tres números enteros de dos dígitos cada uno y determinar en cuál de ellos se encuentra el mayor dígito.
numero1 = 95
numero2 = 788
numero3 = 12

if numero1 > 0 and numero1 < 100 and numero2 > 0 and numero2 < 100 and numero3 > 0 and numero3 < 100:
    numero1 = str(numero1)
    numero2 = str(numero2)
    numero3 = str(numero3)
    num1 = numero1[0]
    num2 = numero1[1]
    num3 = numero2[0]
    num4 = numero2[1]
    num5 = numero3[0]
    num6 = numero3[1]
    digitos = [num1, num2, num3, num4, num5, num6]
    
    mayor = digitos[0]
    for i in range(1, len(digitos)):
        if digitos [i]> mayor:
                mayor = digitos[i]
    print("11. El digito mayor es el",mayor)
else:
    print("11. Algún número ingresado no es valido")

#__________________________________________________________
#12. Leer un número entero de suma de los otros dos.
num1 = 45
num2 = 95
num3 = num1 + num2
print("12. La suma de los dos números es:",num3)

#__________________________________________________________
#13. Leer un número entero menor que 50 y positivo y determinar si es un número primo.
numero = 9
if numero > 0 and numero < 50:
    contador = 0
    flag= False
    for i in range(1,numero+1):
        if (numero% i)==0:
            contador = contador + 1
        if contador >= 3:
            flag=True
            break

    if contador==2 or flag==False:
        print("13. El número",numero,"SI es primo")
    else: print("13. El número",numero,"NO es primo")
else:
    print("13. El número ingresado es inválido")

#___________________________________________________________
#14. Leer un número entero de cuatro dígitos y determinar si el segundo dígito es igual al penúltimo.
numero = 3494

if numero > 1000 and numero < 9999:
    numero = str(numero)
    num1 = numero[0]
    num2 = numero[1]
    num3 = numero[2]
    num4 = numero[3]
    if num2 == num4:
        print("14. El segundo y cuarto dígito SI son iguales")
    else:
        print("14. El segundo y cuarto dígito NO son iguales")
else:
    print("9. El numero",numero,"no es valido")
#________________________________________________________________
#15. Leer un número entero y determinar si es múltiplo de 7.
numero = 29
num = numero % 7
if num == 0:
    print("15. El",numero,"es múltiplo de 7")
else:
    print("15. El",numero,"no es múltiplo de 7")
#________________________________________________________________
#16. Leer un número entero menor que mil y determinar cuántos dígitos tiene.
numero = 987
if numero > 0 and numero < 1000:
    num = str(numero)
    print("16. El numero",numero,"tiene",len(num),"digitos")
else:
    print("16. El número ingresado no es válido")
#________________________________________________________________
#17. Leer un número entero de 4 dígitos y determinar si tiene mas dígitos pares o impares.
numero = 2491
par = 0
impar = 0
i = 0
if numero > 1000 and numero < 9999:
    numero = str(numero)
    while i < 4:
        if int(numero[i]) % 2 == 0:
            par = par + 1
        else:
            impar = impar + 1
        i = i + 1
    if par > impar:
        print("17. hay más dígitos pares")
    elif impar > par:
        print("17. hay más dígitos impares")
    else:
        print("17. hay igual cantidad de numeros pares e impares")
else:
    print("17. El numero",numero,"no es valido")


#18. Leer tres números enteros y determinar si el último dígito de los tres números es igual.
numero1 = 98
numero2 = 788
numero3 = 18

numero1 = str(numero1)
numero2 = str(numero2)
numero3 = str(numero3)

if int(numero1[-1]) == int(numero2[-1]) and int(numero1[-1]) == int(numero3[-1]) and int(numero2[-1]) == int(numero3[-1]):
    print("18. Los tres últimos dígitos SI son iguales")
else:
    print("18. Los tres últimos dígitos NO son iguales")


#19. A un trabajador le pagan según sus horas trabajadas por una tarifa de pago por hora. Si 
# la cantidad de horas trabajadas es mayor 40 horas. La tarifa se incrementa en un 50% para 
# las horas extras. Calcular el salario del trabajador dadas las horas trabajadas y la tarifa 
# ingresadas por el usuario.

def calcularSueldo(tarifa, horasTrabajadas):
    nuevaTarifa = tarifa * 0.5
    valorHoras = tarifa + nuevaTarifa
    horasExtras = horasTrabajadas - 40
    if horasTrabajadas > 40:
        sueldo = (tarifa * 40) + (valorHoras * horasExtras) 
    else: 
        sueldo = tarifa * horasTrabajadas 
    return sueldo

sueldoTrabajado = calcularSueldo(1000, 50)
print("19. El valor a Pagar son:",sueldoTrabajado,"de pesos")

#_________________________________________________________________
#20. Hacer un algoritmo que calcule el total a pagar por la compra de camisas. Si se compran 
# tres camisas o más se aplica un descuento del 20% sobre el total de la compra y si son menos 
# de tres camisas un descuento del 10%
def CompraCamisas(valor, cantidad):
    if cantidad > 2:
        valorCamisas = (valor * cantidad) 
        descuento = valorCamisas * 0.2
        ValorConDescuento = valorCamisas - descuento
        return ValorConDescuento
    else:
        valorCamisas = (valor * cantidad) 
        descuento = valorCamisas * 0.1
        ValorConDescuento = valorCamisas - descuento
        return ValorConDescuento
        
valorCompra = CompraCamisas(10000, 5) 
print("20. El valor de la compra es:", valorCompra)
    
#21. Hacer un programa que pida al usuario las tres notas de un alumno (deben estar entre 0 y 5 
# y pueden tener decimales) y calcule el promedio e indique mediante un mensaje si aprobó o no 
# (aprueba con nota mayor a 3). Se debe validar que las notas introducidas estén dentro del rango permitido.



#22. Verificar si un texto que termina en punto es un palíndromo (capicúa). Un texto es palíndromo si se 
# lee lo mismo de izquierda a derecha o de derecha a izquierda. Ej: “Amor a roma”.



#23. Diseñe una calculadora que sume, reste, multiplique y divida, la cual le pida al usuario mediante input 
# el valor del primer número, el valor del segundo número y la operación a realizar, hay que tener en cuenta 
# la validación de los valores de entrada, por ejemplo:
#Si el programa pide el primer valor, y el usuario ingresa una letra, combinaciones de números y letras o 
# caracteres no numéricos se debe mostrar un mensaje mediante otro input requiriendo que ingrese nuevamente 
# el numero e indicándole al usuario que el carácter ingresado debe ser numérico.
#En el caso que uno de los valores ingresados sea 0 y el usuario ingrese la opción de División, debe imprimir 
# un mensaje donde se indique que no se pude dividir entre cero o que el cero no puede ser dividido.
# Recomendaciones para la validación: buscar información en Google sobre valores ASCII y tabla ASCII investigue 
# el funcionamiento de la función ord()"""  """