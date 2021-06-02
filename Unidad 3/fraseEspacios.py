# Cargar una oración por teclado. Mostrar luego cuantos espacios en blanco se ingresaron. 
# Tener en cuenta que un espacio en blanco es igual a " ", en cambio una cadena vacía es ""

frase = []
frase = input("ingrese una frase: ")
print(len(frase))
fraseMod = frase.replace(" ","")
print(fraseMod)
print(len(fraseMod))
cantidad = len(frase) - len(fraseMod)
print("la cantidad de espacios en blanco son:",cantidad)
