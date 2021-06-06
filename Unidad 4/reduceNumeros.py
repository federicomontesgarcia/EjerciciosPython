#Crear una función que tome una lista de dígitos y devuelva al número al que corresponden.
#Por ejemplo [1,2,3] corresponde a el número ciento veintitrés (123). Utilizar la función
#reduce.

from functools import reduce
def digitos_a_numero(digitos):
 return reduce(lambda x,y:x*10 + y,digitos)
dig = digitos_a_numero([4,3,9,2])
print(dig)

print(4*10)