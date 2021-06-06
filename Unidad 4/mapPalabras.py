#Utilizar la función incorporada map() para crear una función que retorne una lista con la
#longitud de cada palabra (separadas por espacios) de una frase. La función recibe una cadena
#de texto y retornará una lista.

def longitud(palabra:str):
    lista = []
    
    lista = palabra.split()
    print(lista)
  
    for p in range (len(lista)):
        long = []
        i = 0
        for q in range (len(lista)):
            long.append(len(lista[i]))
            i = i + 1
        return(long)

cant =(longitud("la misteriosa llama de la reina loana"))
print(cant)

palabra = "la misteriosa llama de la reina loana"
print()
#-----------------------------------------------------------
def longitud(frase):
    palabra = list(map(len, frase.split()))
    return(palabra)
    
l = longitud("una columna de fuego")
print(l)
#-----------------------------------------
print()
def longitud_palabras(frase): # Función
    palabra_len = list(map(len, frase.split())) # Longitud de cada palabra
    return palabra_len # Retornar resultado
l = longitud_palabras('Hola Luis, como estas?') # Prueba de la función
print(l)