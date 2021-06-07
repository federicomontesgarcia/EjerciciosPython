import math

#p_ancho = 346p_largo = 495b_ancho = 40b_largo = 60

print("Programa para calcular la cantidad de baldosas necesarias\n")

def calcularCantidadBaldosas(p_ancho:int, p_largo:int, b_ancho:int, b_largo:int):
    areaPiso = p_ancho * p_largo
    areaBaldosa = b_ancho * b_largo
    cantidadBaldosas = areaPiso / areaBaldosa
    return cantidadBaldosas

cantidad = math.ceil(calcularCantidadBaldosas(p_ancho=346, p_largo=495, b_ancho=40, b_largo=60))

print("Es necesario adquirir",cantidad , "baldosas")

#pruebas
cantidad = math.ceil(calcularCantidadBaldosas(p_ancho=346, p_largo=495, b_ancho=70, b_largo=70))

print("Es necesario adquirir",cantidad , "baldosas")