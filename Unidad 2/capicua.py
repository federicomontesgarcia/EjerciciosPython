#22. Verificar si un texto que termina en punto es un palíndromo (capicúa). Un texto es palíndromo si se 
# lee lo mismo de izquierda a derecha o de derecha a izquierda. Ej: “Amor a roma”.
i = 0
j = -2
palabra = input("ingrese una palabra o frase: ")
palabra = palabra.replace(" ", "")
palabra = palabra.lower()

print(palabra)
while i < (len(palabra)-1):
    if ord(palabra[i]) == ord(palabra[j]):
        i = i + 1
        j = j - 1
        
    else:
        print("la palabra o frase NO es capicúa")
        break
else:
    print("La palabra SI es capicúa")