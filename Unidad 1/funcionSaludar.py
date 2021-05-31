nombre = input("ingrese el nombre: ")
apellido = input("ingrese el apellido: ")

def saludar(nombre, apellido):
    saludo = "Hola " + nombre + " " + apellido
    return saludo

el_saludo = saludar(nombre, apellido)

print(el_saludo)

