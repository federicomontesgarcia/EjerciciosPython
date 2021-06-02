#Escribir un programa que pida ingresar coordenadas (x,y) que representan puntos en el plano. Informar 
#cuántos puntos se han ingresado en el primer, segundo, tercer y cuarto cuadrante. Al comenzar el programa 
#se pide que se ingrese la cantidad de puntos a procesar.

n = 0
t = 0
i = 0

coorX = []
coorY = []
cuadrante = []
coordenadas = [coorX, coorY]


print(("Ingrese la cantidad de coordenadas (x,y) que va a ingresar: "))
n = int(input())

for t in range (n):
    coorX.append(int(input("ingresar valor de X: ")))
    coorY.append(int(input("ingresar valor de Y: ")))
    print("")
    t = t + 1
print(coordenadas)

for i in range (n):
    if coorX[i] > 0 and coorY[i] > 0:
        cuadrante.append('primero')
        print("La coordenada",i+1,"pertenece al",cuadrante[i],"cuadrante")

    elif coorX[i] < 0 and coorY[i] > 0:
        cuadrante.append('segundo')
        print("La coordenada",i+1,"pertenece al",cuadrante[i],"cuadrante")

    elif coorX[i] < 0 and coorY[i] < 0:
        cuadrante.append('tercero')
        print("La coordenada",i+1,"pertenece al",cuadrante[i],"cuadrante")
        
    elif coorX[i] > 0 and coorY[i] < 0:
        cuadrante.append('cuarto')
        print("La coordenada",i+1,"pertenece al",cuadrante[i],"cuadrante")
    
    i = i + 1
    
print("La cantidad de coordenadas en el primer cuadrante:",cuadrante.count('primero'))

print("La cantidad de coordenadas en el segundo cuadrante:",cuadrante.count('segundo'))

print("La cantidad de coordenadas en el tercer cuadrante:",cuadrante.count('tercero'))

print("La cantidad de coordenadas en el cuarto cuadrante:",cuadrante.count('cuarto'))
